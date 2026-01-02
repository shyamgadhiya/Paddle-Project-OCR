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
    Extracts the complete text line containing "_1_".
    Handles variations like "1_" or "_1" for degraded labels[cite: 10, 35].
    """
    # Logic: Target lines usually contain a long ID sequence followed by the pattern [cite: 32]
    # This list covers the variations you requested.
    patterns = [
        r".*_1_.*",   # Standard: underscore on both sides
        r".*_1$",     # End of line with _1
        r"^1_.*",     # Start of line with 1_
        r".*\d+_1.*"  # Any ID followed by _1 (handles 1_ or _1)
    ]
    
    for item in ocr_results:
        text = item['text'].strip()
        
        for pattern in patterns:
            if re.search(pattern, text):
                # Return the full text line and confidence score [cite: 32, 60]
                return text, item['confidence']
    
    return None, 0.0
