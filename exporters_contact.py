import pdfplumber
import csv

def extract_tables_from_pdf(pdf_path, csv_path):
    with pdfplumber.open(pdf_path) as pdf:
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for page in pdf.pages:
                # Extract tables from the current page
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        # Write each row of the table to the CSV file
                        writer.writerow(row)

# Path to the PDF file
pdf_path = "exporter_contact_details_2012.pdf"
# Path to the output CSV file
csv_path = "exporter_contact_details_2012.csv"

# Extract tables from PDF and write to CSV
extract_tables_from_pdf(pdf_path, csv_path)

print("Tables extracted and written to CSV successfully.")
