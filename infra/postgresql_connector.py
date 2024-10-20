import psycopg2

class PostgreSQLConnector:
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id SERIAL PRIMARY KEY,
            slug TEXT,
            language TEXT,
            languages TEXT,
            req_id TEXT,
            title TEXT,
            description TEXT,
            street_address TEXT,
            city TEXT,
            state TEXT,
            country_code TEXT,
            postal_code TEXT,
            location_type TEXT,
            latitude FLOAT,
            longitude FLOAT,
            categories TEXT,
            tags TEXT,
            tags5 TEXT,
            tags6 TEXT,
            brand TEXT,
            promotion_value INTEGER,
            salary_currency TEXT,
            salary_value INTEGER,
            salary_min_value INTEGER,
            salary_max_value INTEGER,
            benefits TEXT,
            employment_type TEXT,
            hiring_organization TEXT,
            source TEXT,
            apply_url TEXT,
            internal BOOLEAN,
            searchable BOOLEAN,
            applyable BOOLEAN,
            li_easy_applyable BOOLEAN,
            ats_code TEXT,
            meta_data TEXT,
            update_date TEXT,
            create_date TEXT,
            category TEXT,
            full_location TEXT,
            short_location TEXT
        )
        """)
        self.conn.commit()

    def insert_job(self, item):
        try:
            self.cur.execute("""
            INSERT INTO jobs (
                slug, language, languages, req_id, title, description, street_address, city, state,
                country_code, postal_code, location_type, latitude, longitude, categories, tags,
                tags5, tags6, brand, promotion_value, salary_currency, salary_value, salary_min_value,
                salary_max_value, benefits, employment_type, hiring_organization, source, apply_url,
                internal, searchable, applyable, li_easy_applyable, ats_code, meta_data, update_date,
                create_date, category, full_location, short_location
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            """, (
                item.get('slug', None),
                item.get('language', None),
                item.get('languages', None),
                item.get('req_id', None),
                item.get('title', None),
                item.get('description', None),
                item.get('street_address', None),
                item.get('city', None),
                item.get('state', None),
                item.get('country_code', None),
                item.get('postal_code', None),
                item.get('location_type', None),
                item.get('latitude', None),
                item.get('longitude', None),
                item.get('categories', None),
                item.get('tags', None),
                item.get('tags5', None),
                item.get('tags6', None),
                item.get('brand', None),
                item.get('promotion_value', None),
                item.get('salary_currency', None),
                item.get('salary_value', None),
                item.get('salary_min_value', None),
                item.get('salary_max_value', None),
                item.get('benefits', None),
                item.get('employment_type', None),
                item.get('hiring_organization', None),
                item.get('source', None),
                item.get('apply_url', None),
                item.get('internal', None),
                item.get('searchable', None),
                item.get('applyable', None),
                item.get('li_easy_applyable', None),
                item.get('ats_code', None),
                item.get('meta_data', None),
                item.get('update_date', None),
                item.get('create_date', None),
                item.get('category', None),
                item.get('full_location', None),
                item.get('short_location', None)
            ))
            self.conn.commit()
        except Exception as e:
            # Log the error if needed, but continue processing
            print(f"Error inserting job: {e}")

    def close(self):
        self.cur.close()
        self.conn.close()
