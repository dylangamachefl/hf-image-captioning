# app.py (for hf-image-captioning)

import streamlit as st
import requests
import os
from dotenv import load_dotenv
from PIL import Image  # Pillow library for image manipulation
import io  # For handling byte streams

# Load environment variables
# Assuming .env is in the parent 'ai-portfolio' directory
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=dotenv_path)

API_TOKEN = os.getenv("HF_TOKEN")

# Define the model API URL
MODEL_ID = "Salesforce/blip-image-captioning-base"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

# Headers for the API request
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query_hf_image_captioning_api(image_bytes):
    """
    Sends image data to the Hugging Face Inference API for image captioning.
    """
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


# --- Streamlit UI ---
st.set_page_config(layout="wide", page_title="Image Captioning Tool")

st.title("🖼️ Image Captioning Tool")
st.markdown(
    f"""
Upload an image and this app will generate a caption for it using the 
`{MODEL_ID}` model from Hugging Face.
"""
)

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # To read file as bytes:
    image_bytes = uploaded_file.getvalue()

    # Display the uploaded image
    try:
        image = Image.open(io.BytesIO(image_bytes))
        st.image(
            image, caption="Uploaded Image.", use_container_width=True
        )  # Corrected parameter
    except Exception as e:
        st.error(f"Error displaying image: {e}")
        # Don't proceed if image can't be displayed/opened
        uploaded_file = None

if uploaded_file and st.button("Generate Caption"):
    if not API_TOKEN:
        st.error(
            "Hugging Face API token not found. Please set HUGGING_FACE_API_TOKEN in your .env file."
        )
    else:
        with st.spinner(
            f"Generating caption with {MODEL_ID}... (This might take a moment for large models)"
        ):
            try:
                result = query_hf_image_captioning_api(image_bytes)

                st.subheader("Generated Caption:")
                if isinstance(result, list) and result:
                    caption = result[0].get(
                        "generated_text", "Caption not found in response."
                    )
                    st.success(caption)
                elif isinstance(result, dict) and "error" in result:
                    st.error(f"API Error: {result['error']}")
                    if "estimated_time" in result:
                        st.info(
                            f"The model might be loading. Estimated time: {result['estimated_time']:.2f} seconds. Please try again shortly."
                        )
                else:
                    st.error("Received an unexpected response format from the API.")
                    st.json(result)

            except requests.exceptions.RequestException as e:
                st.error(f"API Request Failed: {e}")
                if e.response is not None:
                    st.error(f"Response content: {e.response.text}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

st.markdown("---")
