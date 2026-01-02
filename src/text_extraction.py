'''import re

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
''' 
import re

def extract_target_line(ocr_results):
    """
    Extracts the complete text line containing the pattern "_1_"[cite: 9].
    Updated to handle degraded text where underscores might be missing (1_ or _1).
    """
    # Logic: Look for a long sequence of digits (the ID) followed by 
    # the variations: _1_, 1_, or _1.
    # [cite: 32, 35]
    patterns = [
        r".*_1_.*",  # Standard pattern [cite: 10]
        r".*_1.*",   # Leading underscore only
        r".*1_.*",   # Trailing underscore only
        r"\d{10,}_1" # Long digit ID followed by 1 (common for degraded labels)
    ]
    
    for item in ocr_results:
        text = item['text'].strip()
        
        for pattern in patterns:
            if re.search(pattern, text):
                # Return the full line and confidence as required [cite: 32, 60]
                return text, item['confidence']
    
    return None, 0.0
