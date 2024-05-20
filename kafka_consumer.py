from kafka_conf.Kafka import kafka_consumer
from kafka_conf.db_config import create_table_db

if __name__ == "__main__":
    create_table_db()
    kafka_consumer()