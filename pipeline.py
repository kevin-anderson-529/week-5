# databaselanguage(postgresql)://user:password@url:port/database_name
#'postgresql://sxlpbznx:SyW8M3e9yDFH5kUSI5d7mpP5MM1zNYOv@mahmud.db.elephantsql.com/sxlpbznx'
# conn will be equal to that

import pandas as pd
import psycopg2
from os import getenv
from dotenv import load_dotenv

# Set the database URL
db_url = 'postgresql://sxlpbznx:SyW8M3e9yDFH5kUSI5d7mpP5MM1zNYOv@mahmud.db.elephantsql.com/sxlpbznx'

class PGSQL:
    def __init__(self):
        pass

    def insert_titanic_data(self):
        # Load the data from the CSV file into a pandas DataFrame
        file_path = r"C:\Users\kevin\OneDrive\Desktop\Coding Temple\Week 5 (SQL)\titanic assignment\titanic.csv"
        df = pd.read_csv(file_path)

        # Connection to the PostgreSQL database
        conn = 'postgresql://sxlpbznx:zgnDQcPbZHZu70sFP_RRnT7KOqONRqhc@lallah.db.elephantsql.com/sxlpbznx'
        
        # insert data to new table
        df.to_sql('titanic_data', conn, if_exists='replace')

        # Count rows
        num_rows = df.shape[0]
        print("Number of rows:", num_rows)

        '''887 rows'''

        # Count the number of survivors
        num_survivors = df['Survived'].sum()
        print("Number of survivors:", num_survivors)

        '''342 Survivors'''

        # Find the most frequently occurring Pclass
        most_common_pclass = df['Pclass'].mode()[0]
        print("Most common Pclass:", most_common_pclass)

        '''Passenger Class 3'''

pgsql = PGSQL()
pgsql.insert_titanic_data()