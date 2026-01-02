from paddleocr import PaddleOCR

class OCRManager:
    def __init__(self):
        # Stable initialization for PaddleOCR 2.7.x
        # use_angle_cls=True handles rotated shipping labels
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

    def get_text_with_confidence(self, img_path):
        # Standard call in 2.x series
        result = self.ocr.ocr(img_path, cls=True)
        
        full_results = []
        if result and result[0]:
            for line in result[0]:
                text = line[1][0]
                confidence = line[1][1]
                full_results.append({"text": text, "confidence": confidence})
        return full_results
