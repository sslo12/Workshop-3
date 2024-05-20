from json import  dumps, loads
import joblib
from kafka import KafkaProducer, KafkaConsumer
import pandas as pd
from kafka_conf.db_config import insert_data

def kafka_producer(row):
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

    message = row.to_dict()
    producer.send('kafka-new_happy', value=message)
    print("Message sent")

joblib_file = "./Model/RFR_Model.pkl"
model = joblib.load(joblib_file)

def kafka_consumer():
    consumer = KafkaConsumer(
        'kafka-new_happy',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    for message in consumer:
        df = pd.json_normalize(data=message.value)
        df['happiness_prediction'] = model.predict(df[["gdp_per_capita", "social_support", "freedom", "healthy_life_expectancy"]])
        insert_data(df.iloc[0])
        print("Data inserted into database MySQL:\n", df)