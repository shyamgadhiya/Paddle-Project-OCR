from paddleocr import PaddleOCR

class OCRManager:
    def __init__(self):
        # Configuration is handled here during initialization
        # use_angle_cls=True handles the orientation logic previously triggered by cls=True
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')

    def get_text_with_confidence(self, img_path):
        # Call ocr without the 'cls' keyword argument to fix the TypeError
        result = self.ocr.ocr(img_path)
        
        full_results = []
        # PaddleOCR 3.x returns results in a nested list format
        if result and isinstance(result, list) and result[0] is not None:
            for line in result[0]:
                text = line[1][0]
                confidence = line[1][1]
                full_results.append({"text": text, "confidence": confidence})
        return full_results
