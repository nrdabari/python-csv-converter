import docx
import csv
import re
def extract_contact_details(cell):
    # Function to extract contact details from the cell
    # You can modify this based on the actual structure of your contact details
    contact_details = cell.split('\n')
    phone = ''
    email = ''
    web_address = ''
    # Splitting the text using specified patterns
    contact_details = [part.strip() for part in re.split(r'(Ph:|email:|Web:)', cell) if part.strip()]
    for idx, part in enumerate(contact_details):
        if 'Ph:' in part and idx < len(contact_details) - 1:
            phone = contact_details[idx + 1].strip()
        elif 'email:' in part and idx < len(contact_details) - 1:
            email = contact_details[idx + 1].strip()
        elif 'Web:' in part and idx < len(contact_details) - 1:
            web_address = contact_details[idx + 1].strip()
    return phone, email, web_address
def docx_to_csv(input_docx, output_csv):
    doc = docx.Document(input_docx)
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        first_row = True  # Flag to track the first row
        for table in doc.tables:
            for row in table.rows:
                current_row_data = []  # To store the data of the current row
                for idx, cell in enumerate(row.cells):
                    if idx == 0:  # Sl.No.
                        current_row_data.append(cell.text)
                    elif idx == 1:  # Firm Name
                        firm_details = cell.text.split('\n', 1)
                        current_row_data.append(firm_details[0])
                        if len(firm_details) > 1:
                            current_row_data.append(firm_details[1])
                        else:
                            current_row_data.append('')  # Append empty string if no second part
                    elif idx == 2:  # Contact Details
                        phone, email, web_address = extract_contact_details(cell.text)
                        current_row_data.append(phone)
                        current_row_data.append(email)
                        current_row_data.append(web_address)
                    elif idx == 3:  # Reg No.
                        current_row_data.append(cell.text)
                    elif idx == 4:  # Product Category
                        current_row_data.append(cell.text)
                    elif idx == 5:   # Product(s)
                        current_row_data.append(cell.text)
                if current_row_data:  # Write only if there is data in the row
                    if first_row:
                        first_row = False  # Skip writing header for subsequent rows
                    else:
                        csv_writer.writerow(current_row_data)
if __name__ == "__main__":
    # input_docx_file = "Kochi.docx"
    # output_csv_file = "Kochi seafood Association1.csv"
    input_docx_file = "Gujarat.docx"
    output_csv_file = "Gujarat seafood association.csv"
    docx_to_csv(input_docx_file, output_csv_file)






# from pdf2docx import Converter


# pdf_file = 'Gujarat seafood association.pdf'
# docx_file = 'Gujarat.docx'

# # Convert PDF to DOCX
# cv = Converter(pdf_file)
# cv.convert(docx_file)
# cv.close()





