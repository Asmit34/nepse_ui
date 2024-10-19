import pandas as pd
from sqlalchemy import create_engine
import os

# Database configuration
DB_NAME = 'stock'
DB_USER = 'postgres'
DB_PASSWORD = 'asmitoli123'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Create a connection string
connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(connection_string)

def load_csv_to_db(directory):
    # Iterate over each file in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            # Extract the table name from the file name (remove .csv extension)
            table_name = filename[:-4]  # Remove the last 4 characters (".csv")
            file_path = os.path.join(directory, filename)
            print(f'Loading {file_path} into table "{table_name}"...')

            try:
                # Read the CSV file into a DataFrame
                df = pd.read_csv(file_path)
                
                # Insert the DataFrame into the PostgreSQL table
                df.to_sql(table_name, engine, if_exists='append', index=False)
                print(f'{filename} loaded successfully into table "{table_name}".')
            
            except Exception as e:
                print(f'Error loading {filename}: {e}')

# Directory containing the CSV files
csv_directory = r'C:\Users\Asmit\Desktop\stock-management-system-main\csv'
load_csv_to_db(csv_directory)
