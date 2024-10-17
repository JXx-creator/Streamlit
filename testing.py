import streamlit as st
from PIL import Image as PILImage

st.title("Simple Image Uploader")

# Upload an image
product_image = st.file_uploader("Upload a picture", type=["jpg", "jpeg", "png"])

if product_image is not None:
    # Open and display the uploaded image
    img = PILImage.open(product_image)
    img.thumbnail((800, 800))  # Resize the image to max 800x800 pixels
    st.image(img, caption="Uploaded Image", use_column_width=True)
else:
    st.write("Please upload a picture.")
