from paddleocr import PaddleOCR

class OCRManager:
    def __init__(self):
        # use_angle_cls=True ensures text is read correctly if the label is rotated [cite: 50]
        # lang='en' is the target language for these waybills [cite: 16, 17]
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

    def get_text_with_confidence(self, img_path):
        # Standard call for PaddleOCR 2.x/3.x
        result = self.ocr.ocr(img_path, cls=True)
        
        full_results = []
        if result and result[0]:
            for line in result[0]:
                # line[1][0] is extracted text; line[1][1] is confidence [cite: 60]
                text = line[1][0]
                confidence = line[1][1]
                full_results.append({"text": text, "confidence": confidence})
        return full_results
