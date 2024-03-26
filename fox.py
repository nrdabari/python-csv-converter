import PyPDF2
import base64
import json

def extract_data_from_pdf(pdf_path):
    page_data = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            page_info = {"text": page.extract_text(), "images": []}
            
            if '/XObject' in page['/Resources']:
                xObject = page['/Resources']['/XObject'].get_object()
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        try:
                            data = xObject[obj].get_data()  # Extract raw image data
                            base64_image = base64.b64encode(data).decode('utf-8')  # Convert to base64
                            page_info["images"].append(base64_image)
                        except:
                            pass
            
            page_data.append(page_info)
    return page_data

pdf_path = 'fox1.pdf'
page_data = extract_data_from_pdf(pdf_path)

# Save the page-wise data to a JSON file
with open('page_data.json', 'w') as json_file:
    json.dump(page_data, json_file, ensure_ascii=False, indent=4)

print(f"Extracted data from {len(page_data)} pages and saved to 'page_data.json'.")
