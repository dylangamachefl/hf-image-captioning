---
title: Image Captioning Tool
emoji: 🖼️ # Or any emoji you like
colorFrom: green # Example color
colorTo: yellow   # Example color
sdk: streamlit
app_file: app.py
pinned: false 
---

# 🖼️ Image Captioning Tool

An interactive web application that generates descriptive captions for uploaded images using Hugging Face's state-of-the-art image captioning models via the Inference API. This is the fourth project in a 4-week AI project portfolio building challenge.

**Live Demo:** [Link to your Deployed App on Hugging Face Spaces]

**Project Repository:** `https://github.com/dylangamachefl/hf-image-captioning`

## 📖 Overview

This application allows users to:
1.  Upload an image (JPEG, PNG).
2.  Receive an automatically generated textual caption describing the contents of the image.

The project demonstrates the integration of Computer Vision capabilities through pre-trained models, showcasing how AI can understand and describe visual information.

## 🎯 Problem Solved

Generating relevant and accurate descriptions for images automatically has numerous applications, from aiding accessibility (e.g., alt text for visually impaired users) to content indexing and understanding visual data at scale. This tool provides a simple demonstration of this powerful AI capability, making advanced image understanding models accessible through a user-friendly interface.

## ✨ Skills Showcased

*   **AI/ML Implementation:** Utilizing pre-trained Computer Vision models for image captioning.
*   **Python:** Core programming language for backend logic, image processing, and API interaction.
*   **ML Libraries (Conceptual):** Understanding the role and use of Hugging Face Transformers for multimodal tasks (image and text).
*   **API Integration:** Connecting to and consuming the Hugging Face Inference API for image-based tasks.
*   **Data Handling:**
    *   Processing image uploads.
    *   Sending image data (bytes) to the API.
    *   Parsing JSON responses containing generated captions.
*   **CV (using APIs):** Practical application of Computer Vision for image understanding and description.
*   **Web Development (UI):** Building an interactive user interface with Streamlit, including file uploading.
*   **Libraries:** Use of `Pillow` for image manipulation and `python-dotenv` for API key management.
*   **Version Control:** Git and GitHub for project management.
*   **Deployment:** Deploying the application to Hugging Face Spaces.
*   **Documentation:** Creating clear and concise project documentation (this README).

## 🛠️ How It Works

1.  **Image Upload:** The user selects an image file (JPEG or PNG) using the Streamlit file uploader.
2.  **Image Processing (Client-side):**
    *   The uploaded file is read as bytes.
    *   `Pillow` (PIL) is used to open and validate the image from these bytes.
    *   The uploaded image is displayed in the UI.
3.  **API Call Preparation:** When the "Generate Caption" button is clicked:
    *   The raw image bytes are prepared for the API request.
4.  **Hugging Face API Interaction:**
    *   A POST request is made to the Hugging Face Inference API endpoint for a selected image captioning model (e.g., `Salesforce/blip-image-captioning-large` or `microsoft/git-base-coco`).
    *   The image bytes are sent directly in the request body.
    *   The Hugging Face API token (loaded securely from environment variables) is included in the request headers for authentication.
5.  **Image Captioning:** The Hugging Face model processes the input image and generates a textual description (caption).
6.  **Response Handling:** The application receives the API's JSON response, which typically contains a list with a dictionary, including the `generated_text` (the caption).
7.  **Display Output:** The generated caption is extracted from the response and displayed to the user in the Streamlit interface. Error handling is implemented for API issues, model loading times, or unexpected responses.

## 💻 Technologies Used

*   **Programming Language:** Python 3.x
*   **AI Models/API:**
    *   Hugging Face Hub
    *   Hugging Face Inference API (Free Tier)
    *   Image Captioning Models (e.g., `Salesforce/blip-image-captioning-large`, `microsoft/git-base-coco`, `nlpconnect/vit-gpt2-image-captioning`)
*   **Python Libraries:**
    *   `streamlit`: For building the web application UI.
    *   `requests`: For making HTTP requests to the Hugging Face API.
    *   `Pillow` (PIL): For image processing and handling.
    *   `python-dotenv`: For managing environment variables (like the API token) locally.
*   **Version Control:** Git & GitHub
*   **Deployment:** Hugging Face Spaces
*   **Development Environment:** Visual Studio Code (or your preferred IDE), Python Virtual Environment (`venv` or `conda`)

## 🚀 Setup and Local Development

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/[Your GitHub Username]/hf-image-captioning.git
    cd hf-image-captioning
    ```

2.  **Set up a Python virtual environment:**
    (Assuming you have a shared `venv` or `conda` environment in a parent `ai-portfolio` directory as per the overall plan)
    ```bash
    # From within hf-image-captioning directory:
    # Example for venv:
    # For macOS/Linux:
    source ../venv/bin/activate 
    # For Windows (Git Bash or PowerShell):
    # source ../venv/Scripts/activate
    # For Windows (Command Prompt):
    # ..\venv\Scripts\activate

    # Example for conda (if your shared env is named 'ai_env'):
    # conda activate ai_env 
    ```
    If you don't have the shared environment or prefer a dedicated one:
    ```bash
    python -m venv venv # Or: conda create -n hf_img_caption_env python=3.9
    # Activate it:
    # macOS/Linux: source venv/bin/activate
    # Windows: venv\Scripts\activate
    # Conda: conda activate hf_img_caption_env
    ```

3.  **Install dependencies:**
    Make sure `Pillow` is included in your environment. If starting fresh or it's not in your shared venv:
    ```bash
    pip install -r requirements.txt 
    # Ensure requirements.txt includes: streamlit, requests, python-dotenv, Pillow
    ```

4.  **Set up your Hugging Face API Token:**
    *   Ensure you have a `.env` file in the root of your main `ai-portfolio` project directory (i.e., one level above this `hf-image-captioning` project).
    *   Add your Hugging Face API token to the `.env` file:
        ```
        HUGGING_FACE_API_TOKEN="your_hf_api_token_here"
        ```
    *   *Note: The `app.py` is configured to look for `.env` in the parent directory. If your `.env` file is elsewhere, you might need to adjust the `load_dotenv()` path in `app.py`.*

5.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    The application should open in your web browser.

## 🖼️ Screenshot

<!-- Add your screenshot here once the app is working -->
![Application Screenshot](images/image-captioning-screenshot.png) 
<!-- Make sure to create an 'images' folder and add your screenshot, 
     or adjust the path if it's different. -->

## 🔮 Future Enhancements (Optional)

*   **Multiple caption suggestions:** Some models can generate multiple candidate captions; display a few options.
*   **Confidence scores:** If the API provides them, display confidence scores for captions.
*   **Batch image captioning:** Allow users to upload multiple images or a zip file.
*   **Model selection:** Allow users to choose between different available image captioning models.

## 🙏 Acknowledgements

*   The Hugging Face team for their incredible models, Inference API, and Spaces platform.
*   The developers of Streamlit for making web app creation in Python so accessible.
*   The developers of Pillow for the essential image manipulation library.

---