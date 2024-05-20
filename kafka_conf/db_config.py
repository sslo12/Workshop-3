import configparser
import pymysql
import pandas as pd

def create_connection():
    config = configparser.ConfigParser()
    config.read('./kafka_conf/config.ini')
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

def create_table_db():
    conn, cursor = create_connection()
    if conn is None or cursor is None:
        print("Failed to create database connection.")
        return
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS new_happy_world;")
        cursor.execute("USE new_happy_world;")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS new_happy (          
                id serial PRIMARY KEY,
                country VARCHAR(255) NOT NULL,
                gdp_per_capita FLOAT,
                social_support FLOAT,
                healthy_life_expectancy FLOAT,
                freedom FLOAT,
                happiness_score FLOAT,
                happiness_prediction FLOAT ); 
        """)
        conn.commit()
        print("Table Created Successfully")
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()
        conn.close()

def insert_data(df_row):
    conn, cursor = create_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO new_happy (country, happiness_score, gdp_per_capita, 
    social_support, freedom, healthy_life_expectancy, happiness_prediction)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = tuple(df_row)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    print("Data successfully inserted")
    
def get_query_db():
    conn, cursor = create_connection()
    cursor.execute("SELECT happiness_score, happiness_prediction FROM new_happy;")
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    df = pd.DataFrame(rows, columns=column_names)
    return df