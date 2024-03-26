import pandas as pd

def extract_website_email(contact_address):
    """
    Extracts website and email from the 'Contact Address' column based on 'Website:' and 'Email:' keywords.
    """
    website = None
    email = None
    
    # Splitting the contact address based on known keywords 'Website:' and 'Email:'
    if 'Website:' in contact_address:
        website_start = contact_address.find('Website:') + len('Website:')
        website_end = contact_address.find('Email:') if 'Email:' in contact_address else len(contact_address)
        website = contact_address[website_start:website_end].strip()
        
    if 'Email:' in contact_address:
        email_start = contact_address.find('Email:') + len('Email:')
        email = contact_address[email_start:].strip()
    
    # Clean up any residual punctuation or spaces
    if website:
        website = website.strip(' ,;')
    if email:
        email = email.strip(' ,;')
    
    return website, email

# Load the CSV file
file_path = 'List_of_Major_Software_Companies_in_India.csv'  # Update this path
data = pd.read_csv(file_path)

# Apply the function to each row in the DataFrame
data['Website'], data['Email'] = zip(*data['Contact Address'].apply(lambda x: extract_website_email(x) if pd.notnull(x) else (None, None)))

# Save the updated DataFrame to a new CSV file
output_file_path = 'list.csv'  # Update this path
data.to_csv(output_file_path, index=False)

print("Data processing complete. The updated file has been saved.")
