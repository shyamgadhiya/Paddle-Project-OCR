import re

def extract_target_line(ocr_results):
    """
    Extracts the line containing the pattern '_1_'
    Example Target: 163233702292313922_1_IWV
    """
    pattern = r".*_1_.*"
    
    for item in ocr_results:
        text = item['text']
        if re.search(pattern, text):
            return text, item['confidence']
    
    return None, 0.0
