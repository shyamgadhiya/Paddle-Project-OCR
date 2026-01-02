import streamlit as st
import os
import json
from src.ocr_engine import OCRManager
from src.text_extraction import extract_target_line
from PIL import Image

# Set page configuration for a professional look [cite: 104]
st.set_page_config(page_title="Shipping Label OCR", page_icon="📦")

st.title("📦 Waybill OCR Extractor")
st.write("Extract specific ID patterns containing '_1_' from shipping labels.")

# Initialize OCR Engine [cite: 43]
@st.cache_resource
def load_ocr():
    return OCRManager()

ocr_tool = load_ocr()

# Image upload functionality [cite: 58]
uploaded_file = st.file_uploader("Upload Shipping Label Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Save temp file for processing [cite: 49]
    temp_path = os.path.join("temp_image.png")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display original image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Label", use_container_width=True)

    # OCR processing trigger [cite: 59]
    if st.button("Process OCR"):
        with st.spinner("Analyzing document..."):
            # Run OCR logic [cite: 9]
            results = ocr_tool.get_text_with_confidence(temp_path)
            
            # Extract target line containing "_1_" [cite: 10, 34]
            target_text, confidence = extract_target_line(results)

            st.divider()
            
            # Prepare data for JSON output 
            output_data = {
                "filename": uploaded_file.name,
                "target_line_found": target_text if target_text else "Not Found",
                "confidence_score": round(float(confidence), 4),
                "full_ocr_results": results
            }
            
            if target_text:
                st.subheader("Target Text Found")
                st.success(f"**{target_text}**") # Highlighted target line 
                st.info(f"Confidence Score: {confidence:.2f}") # Show confidence 
                
                # Display JSON result in the UI 
                st.write("### JSON Output")
                st.json(output_data)
                
                # Provide a download button for the JSON file [cite: 109]
                json_string = json.dumps(output_data, indent=4)
                st.download_button(
                    label="Download JSON Result",
                    data=json_string,
                    file_name=f"result_{uploaded_file.name}.json",
                    mime="application/json"
                )
            else:
                st.error("Target pattern '_1_' not found in this image.")
                # Still show raw JSON for the attempt
                st.json(output_data)

            with st.expander("See Raw OCR Output"):
                for res in results:
                    st.text(f"{res['text']} (Conf: {res['confidence']:.2f})")
    
    # Cleanup temp file [cite: 51]
    if os.path.exists(temp_path):
        os.remove(temp_path)
