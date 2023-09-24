import streamlit as st
import pytesseract
from PIL import Image

# Set Tesseract executable path (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'D:\\tessract\\tesseract.exe'

# Streamlit app title and description
st.title("OCR Application")
st.write("Upload an image for text extraction.")

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform OCR on the uploaded image
    text = pytesseract.image_to_string(image)

    # Display the extracted text
    st.header("Extracted Text:")
    st.write(text)

# Add a square box for user input
user_input = st.text_area("Enter text here", "")

# Display user input
if user_input:
    st.header("User Input:")
    st.write(user_input)