import configparser
import pymysql
import pandas as pd

def create_connection():
    config = configparser.ConfigParser()
    config.read('./Kafka/config.ini')
    host = config['mysql']['host']
    user = config['mysql']['user']
    password = config['mysql']['password']
    database = config['mysql']['database']
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Successful Connection")
        cursor = conn.cursor()
        return conn, cursor
    except pymysql.Error as e:
        print("Connection Error:", e)
    return None, None

def create_table_db(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS new_happiness (          
        id serial PRIMARY KEY,
        country VARCHAR(255) NOT NULL,
        gdp_per_capita FLOAT,
        social_support FLOAT,
        healthy_life_expectancy FLOAT,
        freedom FLOAT,
        happiness_score FLOAT,
        happiness_prediction FLOAT )
                   """)
    print("Table Created Successfully")

def insert_data(df):
    conn, cursor = create_connection()
    create_table_db(cursor)
    df = pd.DataFrame()

    columns = ['country', 'happiness_score', 'gdp_per_capita', 'social_support', 'freedom', 'life_expectancy', 'happiness_prediction']
    df = df[columns]
    insert_query = f"""
        INSERT INTO awards({", ".join(columns)})
        VALUES ({", ".join(["%s"] * len(columns))})
    """
    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))
    conn.commit()
    conn.close()
    print("All Data Inserted Successfully.")


def get_query_db():
    conn, cursor = create_connection()
    cursor.execute("SELECT happiness_score, happiness_prediction FROM new_happiness;")
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    df = pd.DataFrame(rows, columns=column_names)
    return df