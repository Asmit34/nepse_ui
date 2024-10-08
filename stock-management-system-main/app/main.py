import pandas as pd
from sqlalchemy import create_engine

# Define the connection to PostgreSQL
db_config = {
    'user': 'postgres',
    'password': 'asmitoli123',
    'host': 'localhost',
    'port': 5432,
    'database': 'nepse'
}

# Create the database connection using SQLAlchemy
connection_string = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
engine = create_engine(connection_string)

# Read CSV file into pandas DataFrame
csv_file_path = r'C:\Users\Asmit\Desktop\stock-management-system-main\agm_reports.csv'
df = pd.read_csv(csv_file_path)

# Define the table name where you want to load the data
table_name = 'agm_reports'

# Load DataFrame to PostgreSQL table
df.to_sql(table_name, engine, if_exists='append', index=False)

print(f"Data from {csv_file_path} has been successfully loaded into {table_name} table.")
