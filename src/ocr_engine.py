from paddleocr import PaddleOCR

class OCRManager:
    def __init__(self):
        # Initialize PaddleOCR (using English)
        # show_log=False is removed to maintain compatibility with PaddleOCR 3.x
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')

    def get_text_with_confidence(self, img_path):
        # PaddleOCR returns a list of results
        result = self.ocr.ocr(img_path, cls=True)
        
        full_results = []
        if result and result[0]:
            for line in result[0]:
                # line[1][0] is the text, line[1][1] is the confidence score
                text = line[1][0]
                confidence = line[1][1]
                full_results.append({"text": text, "confidence": confidence})
        return full_results
