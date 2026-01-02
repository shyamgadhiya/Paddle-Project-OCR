import re

def extract_target_line(ocr_results):
    """
    Finds the line containing the pattern '_1_' as per assessment[cite: 10].
    """
    # This regex looks for '1' flanked by underscores, 
    # but allows for slight OCR noise (like spaces or dots)
    pattern = r".*[_.\s-]1[_.\s-].*"
    
    for item in ocr_results:
        text = item['text']
        if re.search(pattern, text):
            # Return the cleaned text line as required [cite: 32]
            return text.strip(), item['confidence']
    
    return None, 0.0
