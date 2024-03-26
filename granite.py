import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('granite.csv', header=None)

# Define lists to store data for each column
srno = []
companyname = []
address = []
personname = []
phone = []
mobile = []
email = []
website = []
description = []

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Assuming the data format is consistent, split the row into individual components
    data = row[0].split('\n')
    
    # Ensure the data has at least the expected number of elements
    if len(data) < 7:
        continue
    
    # Extract data into variables
    srno.append(data[0])
    companyname.append(data[1])
    
    # Extract multiline address
    address_lines = []
    for line in data[2:]:
        if ':' in line:
            break
        address_lines.append(line.strip())
    address.append('\n'.join(address_lines))
    
    personname.append(data[len(address) + 2])  # Assuming person name is always after the address
    phone.append(data[len(address) + 3].split('/')[0].strip())
    mobile.append(data[len(address) + 3].split('/')[-1].strip())
    email.append(data[len(address) + 4].split(':')[1].strip())
    website.append(data[len(address) + 5].split(':')[1].strip())
    
    # Extract multiline description
    desc_lines = []
    for line in data[len(address) + 6:]:
        desc_lines.append(line.strip())
    description.append('\n'.join(desc_lines))

# Create a new DataFrame with the organized data
new_df = pd.DataFrame({
    'srno': srno,
    'companyname': companyname,
    'address': address,
    'personname': personname,
    'phone': phone,
    'mobile': mobile,
    'email': email,
    'website': website,
    'description': description
})

# Optionally, you can save this DataFrame to a new CSV file
new_df.to_csv('organized_data.csv', index=False)
