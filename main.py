import csv
import re

def clean_key(key):
    # Remove special characters from the key
    return re.sub(r'[^a-zA-Z0-9]', '', key)

def clean_value(value):
    # Remove trailing pipe if present
    return value.rstrip('|').strip()

# Input and output file paths
input_file_path = 'output7.txt'
output_file_path = 'output.csv'

# Open the input text file
with open(input_file_path, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# Initialize variables for CSV data
csv_data = []
current_row = {}
count = 0

# Process each line from the text file
for line in lines:
    # Check if the line is blank
    if line.strip() == '':
        # Add the current row to the CSV data and reset current_row
        csv_data.append(current_row)
        current_row = {}
        count = 0
    else:
        count = count + 1
        # Check if the line contains any of the specified keywords
        if count == 1:
            current_row["company_name"] = line.strip()
            print("company_name>>>>>>>", line.strip())
        elif count == 2:
            current_row["Address"] = line.strip()
        else:
            # Check if the line contains ":"
            if ":" in line:
                # Split the line into key and value parts
                key, value = map(str.strip, line.split(":", 1))

                # Clean up the key by removing special characters
                key = clean_key(key)

                # Clean up the value by removing trailing pipe
                value = clean_value(value)

                # Print the cleaned key and value
                # print("Cleaned Key:", key)
                # print("Cleaned Value:", value)

                # Assign values to the corresponding cleaned keys (ignoring case)
                if key.lower() in ["tel", "ph", "phone"]:
                    current_row["Tel"] = value
                elif key.lower() in ["mob", "mobile"]:
                    print("Mobile>>>", value)
                    current_row["Mob"] = value
                elif key.lower() in ["email", "e-mail", "emailid"]:
                    current_row["Email"] = value
                elif key.lower() == "fax":
                    current_row["fax"] = value
                else:
                    print("key not allowed>>", key)
            elif "." in line:
                # Split the line into key and value parts
                key, value = map(str.strip, line.split(".", 1))

                # Clean up the key by removing special characters
                key = clean_key(key)

                # Clean up the value by removing trailing pipe
                value = clean_value(value)

                # Print the cleaned key and value
                # print("Cleaned Key:", key)
                # print("Cleaned Value:", value)

                # Assign values to the corresponding cleaned keys (ignoring case)
                if key.lower() in ["tel", "ph", "phone"]:
                    current_row["Tel"] = value
                elif key.lower() in ["mob", "mobile"]:
                    print("Mobile>>>", value)
                    current_row["Mob"] = value
                elif key.lower() in ["email", "e-mail", "emailid"]:
                    current_row["Email"] = value
                elif key.lower() == "fax":
                    current_row["fax"] = value
                else:
                    print("key not allowed123>>", key)
            else:
                print("Line does not contain a colon.")

# Add the last row to the CSV data
csv_data.append(current_row)

# Extract unique keys from all rows
all_keys = set(key for row in csv_data for key in row)

# Write the CSV data to the output file
with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # Define the CSV column headers
    fieldnames = ["company_name", "Address", "Tel", "Mob", "Fax", "Email"]

    # Add any additional keys not present in fieldnames
    for key in all_keys - set(fieldnames):
        fieldnames.append(key)

    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header to the CSV file
    csvwriter.writeheader()

    # Write the data rows to the CSV file
    for row in csv_data:
        # Assume that "company_name" is missing, use "Email" as a substitute
        row.setdefault("company_name", row.get("Email", ""))
        csvwriter.writerow(row)

print(f'CSV file "{output_file_path}" has been created successfully.')
