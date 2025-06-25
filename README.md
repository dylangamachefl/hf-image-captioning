---
title: Image Captioning Tool (Transformers)
emoji: 🖼️
colorFrom: green 
colorTo: yellow  
sdk: streamlit
app_file: app.py
pinned: false 
---

# 🖼️ Image Captioning Tool (using Transformers library)

An interactive web application that generates descriptive captions for uploaded images. This version **directly utilizes the Hugging Face `transformers` library** to load and run a state-of-the-art image captioning model locally within the application's environment. This is the fourth project in a 4-week AI project portfolio building challenge.

**Live Demo:** [Link to your Deployed App on Hugging Face Spaces]

**Project Repository:** `https://github.com/dylangamachefl/hf-image-captioning`

## 📖 Overview

This application allows users to:
1.  Upload an image (JPEG, PNG).
2.  Receive an automatically generated textual caption describing the contents of the image.

This project now demonstrates loading and running sophisticated AI models (specifically for Computer Vision and NLP) directly using the `transformers` library, including handling model caching and dependencies like PyTorch.

## 🎯 Problem Solved

Generating relevant captions for images has applications in accessibility, content indexing, and visual data understanding. This tool showcases this capability by running a powerful model within the app, offering more control and potentially faster inference (after initial model load) compared to relying solely on external public APIs for every request, especially when such APIs might not be available for specific desired models.

## ✨ Skills Showcased

*   **AI/ML Implementation:**
    *   **Loading and running pre-trained Computer Vision/NLP models directly with the Hugging Face `transformers` library.**
    *   Utilizing the `pipeline` abstraction for ease of use.
*   **Python:** Core programming language for backend logic, image processing, and model interaction.
*   **ML Libraries:** Direct use of `transformers` and `torch` (PyTorch).
*   **Model Caching:** Implementing efficient model loading using Streamlit's `@st.cache_resource`.
*   **Data Handling:** Processing image uploads and preparing them for the model.
*   **CV (using local models):** Practical application of Computer Vision for image understanding and description.
*   **Web Development (UI):** Building an interactive user interface with Streamlit, including file uploading.
*   **Libraries:** Use of `Pillow` for image manipulation.
*   **Dependency Management:** Managing larger dependencies like `torch` and `transformers` in `requirements.txt`.
*   **Version Control:** Git and GitHub for project management.
*   **Deployment:** Deploying the application (with its model dependencies) to Hugging Face Spaces.
*   **Documentation:** Creating clear and concise project documentation (this README).
*   **Adaptability & Problem Solving:** Pivoting from an API-based approach to a library-based approach when API limitations were encountered.

## 🛠️ How It Works

1.  **Model Loading (on App Startup):**
    *   When the Streamlit application starts, a function decorated with `@st.cache_resource` is called to load an image captioning model (e.g., `Salesforce/blip-image-captioning-base`) using the `transformers.pipeline("image-to-text", ...)` utility.
    *   The model is downloaded (if not already cached by `transformers`) and loaded into memory. This happens only once thanks to caching, making subsequent uses fast.
2.  **Image Upload:** The user selects an image file (JPEG or PNG) using the Streamlit file uploader.
3.  **Image Preparation:**
    *   The uploaded file is read, and `Pillow` (PIL) is used to open it as a PIL Image object.
    *   The uploaded image is displayed in the UI.
4.  **Caption Generation:** When the "Generate Caption" button is clicked:
    *   The PIL Image object is passed directly to the loaded `transformers` pipeline (e.g., `captioner(pil_image_object)`).
    *   The pipeline handles all necessary pre-processing of the image, feeds it to the model, and performs post-processing on the model's output.
5.  **Display Output:**
    *   The pipeline returns a list containing a dictionary with the `generated_text` (the caption).
    *   This caption is extracted and displayed to the user. Error handling is in place for issues during model inference.

## 💻 Technologies Used

*   **Programming Language:** Python 3.x
*   **Core AI/ML Libraries:**
    *   **Hugging Face `transformers`:** For loading and running the image captioning model.
    *   **`torch` (PyTorch):** As the backend deep learning framework for the model.
*   **Image Captioning Model (example):** `Salesforce/blip-image-captioning-base` (or other compatible models).
*   **Python Libraries:**
    *   `streamlit`: For building the web application UI.
    *   `Pillow` (PIL): For image processing and handling.
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
    (Activate your shared `ai-portfolio` environment or create a dedicated one)
    ```bash
    # Example for activating shared venv:
    # macOS/Linux: source ../venv/bin/activate
    # Windows: ..\venv\Scripts\activate 
    ```

3.  **Install dependencies:**
    This project has significant dependencies.
    ```bash
    pip install -r requirements.txt 
    # Ensure requirements.txt includes: streamlit, Pillow, transformers, torch
    ```
    *(Note: `torch` can be a large download. If you have a specific CUDA version for a GPU, you might install PyTorch separately following instructions from [pytorch.org](https://pytorch.org/) before `pip install -r requirements.txt` to ensure compatibility, though the default CPU version usually works fine for CPU inference.)*

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    *   **First Run Note:** The first time you run the app, the `transformers` library will download the specified model (e.g., `Salesforce/blip-image-captioning-base`), which can take several minutes and consume significant disk space (usually in `~/.cache/huggingface/hub/`). Subsequent runs will be much faster as the model will be cached.
    *   The application should open in your web browser.

## 🖼️ Screenshot

![Screenshot 2025-06-25 at 13-39-47 Image Captioning Tool (Transformers)](https://github.com/user-attachments/assets/38fba30e-eca8-4dbb-91da-7617f131cc40)

## 🔮 Future Enhancements (Optional)

*   **Allow model selection:** Let users choose from a few different locally available captioning models.
*   **More detailed error reporting:** For model loading or inference failures.
*   **Explore quantization or smaller models:** For faster performance or reduced resource usage, especially if deploying to resource-constrained environments.

## 🙏 Acknowledgements

*   The Hugging Face team for their `transformers` library, models, and Spaces platform.
*   The developers of PyTorch for the underlying deep learning framework.
*   The developers of Streamlit and Pillow.

---
