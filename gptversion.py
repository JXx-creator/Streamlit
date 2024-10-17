import os
import streamlit as st 
from openai import OpenAI
import PIL.Image
import google.generativeai as genai
from google.cloud import vision

# Set up OpenAI and Gemini API keys
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Initialize Google Vision API client
vision_client = vision.ImageAnnotatorClient()

# Text model
gemini_model = genai.GenerativeModel('gemini-1.5-flash')

# Upload the image file through Streamlit
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Open the uploaded image file
    image = PIL.Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Analyze the image using Google Vision API (or a similar service)
    content = uploaded_image.read()  # Get image binary data
    image_vision = vision.Image(content=content)

    # Perform label detection to get general info about the image
    response = vision_client.label_detection(image=image_vision)
    labels = response.label_annotations

    # Extract relevant information from the labels
    prompt_description = "Identified objects: "
    for label in labels:
        prompt_description += f"{label.description} (score: {label.score:.2f}), "

    st.write("Image Description: ", prompt_description)

    # Generate a detailed description using generative model
    system_prompt = """
    You are an IT device identifier.
    Identify and describe the product in the images uploaded.
    Your objective is to identify the product in the image and describe the detailed information about the specific brand and model to assist users.
    """

    # Call the generative model with extracted labels
    chat_response = client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt_description}
        ],
    )

    # Display the response
    st.write("Generated Product Information: ", chat_response.choices[0].message.content)
