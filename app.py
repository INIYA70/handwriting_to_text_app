import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.set_page_config(page_title="Handwriting to Text", layout="centered")

st.title("📝 Handwriting to Text App")
st.markdown("Upload a handwritten image and extract the text from it using OCR.")

uploaded_file = st.file_uploader("📂 Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Image", use_column_width=True)

    with st.spinner("🔍 Extracting text..."):
        reader = easyocr.Reader(['en'])
        img_array = np.array(image)
        result = reader.readtext(img_array, detail=0)

    extracted_text = " ".join(result)
    st.subheader("📄 Extracted Text:")
    st.write(extracted_text)

    st.download_button("⬇️ Download Text", extracted_text, file_name="extracted_text.txt")
