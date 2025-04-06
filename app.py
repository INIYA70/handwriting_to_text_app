import streamlit as st
from ocr_helper import extract_text
from PIL import Image

st.set_page_config(page_title="Handwriting to Text App ✍️", layout="centered")

st.title("📝 Handwriting to Text Converter")
st.markdown("Upload a handwritten image and extract the text using AI (EasyOCR)!")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    with st.spinner("Extracting text..."):
        extracted_text = extract_text(uploaded_file)

    st.subheader("🧾 Extracted Text")
    st.text_area("Result", extracted_text, height=200)
