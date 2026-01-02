from paddleocr import PaddleOCR

class OCRManager:
    def __init__(self):
        # Removed show_log=False to ensure compatibility with PaddleOCR 3.x
        # use_angle_cls=True is kept to handle various image orientations [cite: 50]
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')

    def get_text_with_confidence(self, img_path):
        # Standard OCR call without deprecated keyword arguments
        result = self.ocr.ocr(img_path, cls=True)
        
        full_results = []
        # Result structure in 3.x is a nested list [cite: 34]
        if result and result[0]:
            for line in result[0]:
                text = line[1][0]
                confidence = line[1][1]
                full_results.append({"text": text, "confidence": confidence})
        return full_results
