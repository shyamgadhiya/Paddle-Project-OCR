import streamlit as st
import os
from src.ocr_engine import OCRManager
from src.text_extraction import extract_target_line
from PIL import Image

st.set_page_config(page_title="Shipping Label OCR")

st.title("📦 Waybill OCR Extractor")
st.write("Extract specific ID patterns containing '_1_' from shipping labels.")

# Initialize OCR Engine
@st.cache_resource
def load_ocr():
    return OCRManager()

ocr_tool = load_ocr()

uploaded_file = st.file_uploader("Upload Shipping Label Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Save temp file
    temp_path = os.path.join("temp_image.png")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display original image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Label", use_container_width=True)

    if st.button("Process OCR"):
        with st.spinner("Analyzing document..."):
            # Run OCR
            results = ocr_tool.get_text_with_confidence(temp_path)
            
            # Extract target
            target_text, confidence = extract_target_line(results)

            st.divider()
            
            if target_text:
                st.subheader("Target Text Found")
                st.success(f"**{target_text}**")
                st.info(f"Confidence Score: {confidence:.2f}")
            else:
                st.error("Target pattern '_1_' not found in this image.")

            with st.expander("See Raw OCR Output"):
                for res in results:
                    st.text(f"{res['text']} (Conf: {res['confidence']:.2f})")
