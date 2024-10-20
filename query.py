import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

class PostgreSQLDatabase:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST'),
            database=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD')
        )
        self.cursor = self.connection.cursor()

    def fetch_all_jobs(self):
        query = "SELECT * FROM jobs;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

def save_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return

    df = pd.DataFrame(data, columns=[
        'id', 'slug', 'language', 'languages', 'req_id', 'title', 
        'description', 'street_address', 'city', 'state', 
        'country_code', 'postal_code', 'location_type', 'latitude', 
        'longitude', 'categories', 'tags', 'tags5', 'tags6', 
        'brand', 'promotion_value', 'salary_currency', 'salary_value', 
        'salary_min_value', 'salary_max_value', 'benefits', 
        'employment_type', 'hiring_organization', 'source', 
        'apply_url', 'internal', 'searchable', 'applyable', 
        'li_easy_applyable', 'ats_code', 'meta_data', 
        'update_date', 'create_date', 'category', 
        'full_location', 'short_location'
    ])

    full_path = os.path.join(os.getcwd(), filename)  # Saves in the current working directory
    df.to_csv(full_path, index=False)
    print(f"Data saved to {full_path}")

if __name__ == "__main__":
    postgres_db = PostgreSQLDatabase()
    jobs_data = postgres_db.fetch_all_jobs()
    postgres_db.close()
    save_to_csv(jobs_data, 'jobs_data.csv')
