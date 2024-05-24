# Katka - ETL
This repository contains the documentation and code for the challenge focuses on developing an ETL pipeline using Python to process and analyze datasets from 5 csv about happiness world.
***
# Objective
The main goals of this workshop are:

1. **Load Data**: Transfer data from CSV files to a relational database.
2.	**Perform Exploratory Data Analysis (EDA)**: to understand the characteristics and relationships in the data.
3.	Select the **most relevant features** for the model.
4.	Implement a **real-time data streaming** solution using Kafka.
5.	Apply the **trained regression model** to predict the values of the test data set.
6.	**Evaluate and compare** the characteristics of data from different years as they may vary.
***
# Technologies Used
  * <img src="https://github.com/sslo12/Workshop-1-ETL/assets/115416417/b23a91ab-151a-4dd8-b421-fc87111e3481" alt="Looker Studio" width="21px" height="21px"> Python
  * <img src="https://cdn.icon-icons.com/icons2/2667/PNG/512/jupyter_app_icon_161280.png" alt="Looker Studio" width="21px" height="21px"> Jupyter Notebook
  * <img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/mysql_original_wordmark_logo_icon_146417.png" alt="Looker Studio" width="21px" height="21px"> Relational database (MySQL)
  * <img src="https://w7.pngwing.com/pngs/991/165/png-transparent-docker-hd-logo-thumbnail.png" alt="Docker" width="21px" height="21px"> Docker
  * <img src="https://cdn.icon-icons.com/icons2/2248/PNG/512/apache_kafka_icon_138937.png" alt="Kafka" width="21px" height="21px"> Kafka
  * <img src="https://i.pinimg.com/736x/7a/f2/1e/7af21eaf89a449831a1e12d640b54fae.jpg" alt="Looker Studio" width="21px" height="21px"> Power BI Desktop
***
# Data Information
It can be noted that the above datasets each present a variety of metrics that are used to assess happiness and well-being in different countries.
***
# Implementation Instructions
### Step 1: Clone the Repository
    git clone https://github.com/sslo12/Workshop-3

### Step 2: Create config.init
In the kafka_conf folder Create a config.ini file and copy the credentials of your MySQL database into it.
  ```
  [mysql]
host = your host
user = your user
password = your password
database = your database
  ```

### Step 4: Virtual Environment
Open your terminal and install and activate your virtual environment with the following code:
```
python3 -m venv nombre_del_entorno
```
### Step 5: Activate Virtual Environment
```
nombre_del_entorno/Scripts/activate
```
### Step 6: Install Dependencies
Run the following command in your terminal to install the dependencies needed to run this project:
```
pip install -r requirements.txt
```
### Step 7: Setting up Kafka
Run Docker Compose
```
docker-compose up
```

After Access Kafka Container
```
docker exec -it kafka bash
```

Create Kafka Topic
```
kafka-topics --bootstrap-server kafka --create --topic kafka-new_happy
```
This command sets up a Kafka topic that will be used for streaming happiness data.

### Step 8: Running the Streming:
Once you have set up Kafka, open two new terminals and run the following command in each terminal:
```
python kafka_consumer.py
```
```
python kafka_producer.py
```
Note: Run the consumer first.
Then, in to the Kafka dashboard, find the data in the dashboard that we configured in the api link

### Step 9: Graphics
To set up the dashboard and connect PowerBI to Kafka, you can follow the instructions in [this video](https://www.youtube.com/watch?v=B0nwAalcU7w&t=1s).
