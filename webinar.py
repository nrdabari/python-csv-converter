import fitz  # PyMuPDF
import pandas as pd
import re

# Open the PDF file
try:
    with fitz.open('webinar-directory.pdf') as doc:
        text = ""
        for page in doc:
            text += page.get_text()
except Exception as e:
    print("Error occurred while processing PDF:", e)
    exit(1)

# Process the extracted text to format it into a list of dictionaries
companies = text.split('Exhibitors Profile')  # Split each exhibitor's profile
data = []

for company in companies:
    profile = {}
    try:
        profile['Company Name'] = re.search(r'Company Name\s*:\s*(.*?)\n', company).group(1).strip()
        profile['Address'] = re.search(r'Address\s*:\s*(.*?)\n', company).group(1).strip()
        
        # Extracting the entire contact details content
        contact_details_search = re.search(r'Contact Details\s*:\s*(.*?)(?:\nEmail|Website|Contact Person|$)', company, re.DOTALL)
        if contact_details_search:
            # Remove any new lines and extra spaces for clean data
            contact_details = ', '.join(contact_details_search.group(1).split())
            profile['Contact Details'] = contact_details
        
        # Extracting all email addresses
        email_search = re.search(r'Email\s*:\s*(.*?)(?:\nWebsite|Contact Person|Products|$)', company, re.DOTALL)
        if email_search:
            # Using a simple regex pattern to match email addresses
            emails = ', '.join(email_search.group(1).split())
            profile['Email'] = emails
        
        profile['Website'] = re.search(r'Website\s*:\s*(.*?)\n', company).group(1).strip()
    

        contact_person_search = re.search(r'Contact Person\s*:\s*(.*?)(?:\nProducts|$)', company, re.DOTALL)
        if contact_person_search:
            # Assuming contact persons are separated by a comma or a newline
            contact_persons = re.split(r',|\n', contact_person_search.group(1))
            # Clean up each name and join with comma
            profile['Contact Person'] = ', '.join(name.strip() for name in contact_persons if name.strip())
        
        
        
        # Extracting products
        products_search = re.search(r'Products\s*(.*?)(?:\n\Z|\n(?=Company Name\s*:))', company, re.DOTALL)
        if products_search:
            products = products_search.group(1).strip()
            # Normalize the whitespace and join the lines
            products_clean = ' '.join(products.split())
            profile['Products'] = products_clean
            
            
        data.append(profile)
    except AttributeError:
        continue

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
try:
    df.to_csv('Webinar-Directory.csv', index=False)
    print('CSV file has been created successfully.')
except Exception as e:
    print("Error occurred while saving CSV:", e)
