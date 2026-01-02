from paddleocr import PaddleOCR

class OCRManager:
    def __init__(self):
        # use_angle_cls=True is essential for shipping labels that might be rotated
        # Set show_log=False to keep the Streamlit logs clean
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

    def get_text_with_confidence(self, img_path):
        # In this stable version, cls=True is supported here
        result = self.ocr.ocr(img_path, cls=True)
        
        full_results = []
        if result and result[0]:
            for line in result[0]:
                text = line[1][0]
                confidence = line[1][1]
                full_results.append({"text": text, "confidence": confidence})
        return full_results
