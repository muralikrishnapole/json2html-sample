import os
import pandas as pd
from bs4 import BeautifulSoup

# Initialize total sales variable
total_sales = 0.0

# Specify the directory where the unzipped files are located
directory_path = "/Users/guruprasadpannuru/Downloads/q2"  # Replace with the correct path

# Loop over each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".html"):
        file_path = os.path.join(directory_path, filename)
        
        # Read and parse the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            
            # Locate all tables and iterate over them
            tables = soup.find_all('table')
            for table in tables:
                # Parse the table with pandas
                df = pd.read_html(str(table))[0]
                
                # Standardize the "Type" column to handle case sensitivity and strip whitespace
                df['Type'] = df['Type'].str.strip().str.lower()
                
                # Filter rows where the type is 'gold'
                gold_rows = df[df['Type'] == 'gold']
                
                # Calculate sales (Units * Price) and add to total sales
                total_sales += (gold_rows['Units'] * gold_rows['Price']).sum()

# Print the total sales rounded to 2 decimal places
print(f"Total Gold sales: {total_sales:.2f}")