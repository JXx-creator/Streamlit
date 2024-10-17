import os
import streamlit as st
try:
    from google.auth import default
    from google.cloud import bigquery
except ImportError:
    st.write("Reauthentication is needed.")
    st.stop()


import pandas as pd
import base64



st.set_page_config(layout="wide")
pd.set_option('display.max_columns', None)
credentials, project_id = default()
client = bigquery.Client(credentials=credentials, project="project")
st.title('Tool')
st.write('Provide the ID')
_options = ['1', '2', '3']
default_client = "1"

with st.sidebar:
    _id = st.text_input("ID:","jhjkdkjhhkjhkj")
from openai import OpenAI
from PIL import Image as PILImage

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])  # Replace with your actual key

# Function to analyze the IT product
def it_product_analysis(image_description):
    prompt = f"Identify the IT product based on this description: {image_description}"
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Streamlit layout for uploading and displaying the image
st.title("IT Product Identifier")

# Upload an image
product_image = st.file_uploader("Upload a picture of an IT product", type=["jpg", "jpeg", "png"])

if product_image is not None:
    # Open and display the uploaded image
    img = PILImage.open(product_image)
    img.thumbnail((800, 800))  # Resize the image to max 800x800 pixels
    st.image(img, caption="Uploaded IT Product Image", use_column_width=True)

    # Analyze the image for IT product identification
    if st.button("Analyze Product"):
        # Placeholder for actual image description extraction
        image_description = "Placeholder description of the uploaded IT product image."

        try:
            result = it_product_analysis(image_description)
            st.write(result)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
else:
    st.write("Please upload a picture of an IT product to identify.")
