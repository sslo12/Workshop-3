# Katka - ETL
This repository contains the documentation and code for the challenge focuses on developing an ETL pipeline using Python to process and analyze datasets from 5 csv about happiness world.
***
# Objective
The main goals of this workshop are:

1. **Load Data**: Transfer data from CSV files to a relational database.
2. **Create an ETL Pipeline**: Extract, transform, and merge data, storing the results in a database and as a CSV file in Google Drive.
3. **Airflow**: A DAG is configured to orchestrate data extraction, transformation and loading tasks, scheduling their execution, error handling and notifications, thus ensuring workflow automation and efficiency.
4. **Data Visualization**: Display data through chart visualizations that pull information directly from the database, not the CSV files.
***
# Technologies Used
  * <img src="https://github.com/sslo12/Workshop-1-ETL/assets/115416417/b23a91ab-151a-4dd8-b421-fc87111e3481" alt="Looker Studio" width="21px" height="21px"> Python
  * <img src="https://cdn.icon-icons.com/icons2/2667/PNG/512/jupyter_app_icon_161280.png" alt="Looker Studio" width="21px" height="21px"> Jupyter Notebook
  * <img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/mysql_original_wordmark_logo_icon_146417.png" alt="Looker Studio" width="21px" height="21px"> Relational database (MySQL)
  * <img src="https://d1.awsstatic.com/acs/characters/Logos/Docker-Logo_Horizontel_279x131.b8a5c41e56b77706656d61080f6a0217a3ba356d.png" alt="Docker" width="21px" height="21px"> Docker
  * <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Apache_kafka.svg/1200px-Apache_kafka.svg.png" alt="Kafka" width="21px" height="21px"> Kafka
  * <img src="https://i.pinimg.com/736x/7a/f2/1e/7af21eaf89a449831a1e12d640b54fae.jpg" alt="Looker Studio" width="21px" height="21px"> Power BI Desktop
***
# Data Information
The dataset the_grammy_awards contains information about the Grammy Awards, including details such as year, category, nominee, artist/group, and whether or not they won.
This is a dataset of Spotify tracks over a range of 125 different genres. Each track has some audio features associated with it. The data is in CSV format which is tabular and can be loaded quickly.
***
# Workflow
![image](https://github.com/sslo12/Workshop-2/assets/115416417/bdfdcc6a-434b-4d2c-ba7f-b7a6e3d90e36)
***

# Implementation Instructions
### Step 1: Clone the Repository
    git clone https://github.com/sslo12/Workshop-2

### Step 2: Create config.init
In the Config_db folder Create a config.ini file and copy the credentials of your MySQL database into it.
  ```
  [mysql]
host = your host
user = your user
password = your password
database = your database
  ```
### Step 3: API Configuration - DRIVE
Para que el enlace sea más pequeño en tu README, puedes usar texto en lugar de la URL completa. Aquí tienes una forma de hacerlo:

**Creating credentials to use the Google Drive API**  
The `credentials_module.json` file must be placed inside the `./Airflow_ETL` folder to obtain the necessary credentials. 
Follow the instructions in [video](https://www.youtube.com/watch?v=ZI4XjwbpEwU) to obtain them.

### Step 4: Virtual Environment
Open your linux terminal and install and activate your virtual environment with the following code:
```
python3 -m venv nombre_del_entorno
```
### Step 5: Activate Virtual Environment
```
source nombre_del_entorno/bin/activate
```
### Step 6: Install Dependencies
Run the following command in your terminal to install the dependencies needed to run this project:
```
pip install -r requirements.txt
```
### Step 7: Install Apache Airflow
Install Airflow in your repository folder
```
pip install apache-airflow
```

After installing Airflow, you must run the following command while in the repository root to set the AIRFLOW_HOME environment variable:
```
export AIRFLOW_HOME=$(pwd)
```

You need to adjust the settings in the `airflow.cfg` file. In the `dags_folder` section, make sure to indicate the location of the DAGs. Change `dags` to `Airflow_ETL` to look like this:
```
dags_folder = /root/Workshop-2/Airflow_ETL
```
### Step 8: Running the DAG in Airflow:
Once you have set up Airflow and your DAGs are in the correct location, start Airflow using the following command from the repository root:
```
airflow standalone
```
Then, log in to the Airflow dashboard, find the DAG named `dags_workshop2`," and execute it to begin the ETL process.
Note: Ensure that all preceding steps have been successfully completed before running the DAG in Airflow.

### Step 9: Graphics
To set up the dashboard and connect PowerBI to Drive, you can follow the instructions in [this video](https://www.youtube.com/watch?v=ufrVf6BTLKc&t=359s).
