# Ensure tabula is installed: pip install tabula-py
import tabula
import pandas as pd

# Path to the PDF file
pdf_path = "Top_100_Exporters_2022_23_pdf1257.pdf"

# Read the PDF into a list of DataFrames, specify pages='all' to read all pages
# You might need to set the lattice=True or stream=True based on the PDF's structure
# lattice is for grid-like tables, stream is for tables with spaces between columns
dfs = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# Concatenate all DataFrames into a single DataFrame
# Ensure there are actually DataFrames to concatenate
if dfs:
    df = pd.concat(dfs, ignore_index=True)
else:
    print("No tables found in the PDF.")

# Only proceed if df is created successfully
if 'df' in locals():
    # Write DataFrame to a CSV file
    csv_file_path = "Top_100_Exporters_2022_23_pdf1257.csv"
    df.to_csv(csv_file_path, index=False)

    print("Data has been written to:", csv_file_path)
else:
    print("DataFrame is empty. No CSV file created.")
