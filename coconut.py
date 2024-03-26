import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def test_extract_info(text):
    # Simplified pattern just to see if we can match anything at all
    pattern = re.compile(r'(\d+)\s+(\d+)')
    matches = pattern.finditer(text)

    for match in matches:
        print(f"Match found: {match.group(0)}")
        return True
    return False

pdf_path = 'Coconut Exporter (1).pdf'
extracted_text = extract_text_from_pdf(pdf_path)

if not test_extract_info(extracted_text):
    print("No match found in simplified test")
else:
    print("Simplified match found, refine your regular expression based on this result")
