# 🚀 Customer Behavior ETL Pipeline  

<img width="1911" height="816" alt="airflofinal" src="https://github.com/user-attachments/assets/1a66404d-8744-46cb-a371-b52f962e042f" />


*A Production-Ready ETL Pipeline Using Airflow, Docker, Python OOP, and Postgres*

This project implements a complete **ETL (Extract–Transform–Load) pipeline** to process customer behavior data from an e-commerce website.  
It uses **Apache Airflow** for workflow orchestration, **Docker Compose** for environment setup, **Python OOP** for preprocessing logic, and **Postgres** as the data warehouse.

The ETL pipeline is fully automated and containerized – making it reproducible, scalable, and easy to deploy.

---

## 🧠 **Project Goals**

- Build a **real-world, production-style ETL pipeline**  
- Apply **data preprocessing** using clean OOP architecture  
- Automate workflows using **Airflow DAGs**  
- Load cleaned data into **Postgres**  
- Practice professional **Git branching & version control**  
- Create a portfolio-ready end-to-end data engineering project  

---

# 📊 **Pipeline Architecture**

The ETL pipeline consists of three main steps:

             ┌──────────────────────┐
             │   Raw CSV Dataset    │
             │  (Customer Behavior) │
             └──────────┬───────────┘
                        │ Extract
                        ▼
            ┌────────────────────────┐
            │  Preprocessing Layer   │
            │ (Python OOP Class)     │
            │ - Clean data           │
            │ - Validate fields      │
            │ - Handle types/nulls   │
            └──────────┬─────────────┘
                       │ Transform
                       ▼
          ┌─────────────────────────────┐
          │   Processed Clean Dataset   │
          │  (.csv saved inside /data)  │
          └───────────┬────────────────┘
                      │ Load
                      ▼
       ┌──────────────────────────────────┐
       │        Postgres Database         │
       │  (customer_behavior table)       │
       └──────────────────────────────────┘

---

# ⚙️ **Tech Stack**

| Component | Technology |
|----------|------------|
| Workflow Orchestration | Apache Airflow 3.1 |
| Containerization | Docker & Docker Compose |
| Programming | Python 3.12 |
| Data Storage | Postgres (Custom Service) |
| Data Processing | Pandas |
| Architecture | OOP-based preprocessing class |
| Version Control | Git + GitHub Flow |
| Optional Dashboard | pgAdmin (optional) |

---

# 📁 **Project Structure**

```bash
etl-customer-behavior/
│
├── dags/
│   └── customer_behavior_etl.py        # Airflow DAG
│
├── processor/
│   ├── __init__.py
│   └── preprocessing.py                # Python OOP preprocessing module
│
├── data/
│   ├── raw/                            # Raw dataset
│   │   └── online_shoppers_intention.csv
│   └── processed/                      # Cleaned dataset
│       └── online_shoppers_preprocessed.csv
│
├── docker-compose.yaml                 # Airflow core services
├── docker-compose.override.yml         # Custom Postgres service + volumes
│
└── README.md

---

#  **How to Run the Project (Step-by-Step)**
1️. Clone the Repository

git clone https://github.com/<your-username>/etl-customer-behavior.git
cd etl-customer-behavio

2️. Start the Airflow + Postgres Environment

Make sure Docker Desktop is running.
Then run:

docker-compose up -d
This command starts:
Airflow Scheduler
Airflow Webserver
Airflow Worker
Airflow Triggerer
Redis
Custom Postgres Database (etl_db)

3️. Access Airflow UI

Open:
http://localhost:8080
Login credentials (default):
Username: airflow
Password: airflow

4️. Trigger the ETL Pipeline

In Airflow:
Find the DAG: customer_behavior_etl
Toggle it ON
Click Trigger DAG

5️. Verify Load in Postgres

Enter Postgres container:
docker exec -it etl_db psql -U etl_user -d customer_behavior
Query the loaded table:
SELECT * FROM customer_behavior LIMIT 20;
---
#  **Airflow DAG Overview**

 **The DAG coordinates the ETL process:**

check_raw_file → preprocess_data → load_to_db
**check_raw_file**
Simple check to ensure dataset exists
Uses BashOperator
**preprocess_data**
Runs the OOP preprocessing pipeline
Cleans data
Validates columns
Saves clean CSV to /data/processed
**load_to_db**
Reads the processed CSV
Connects to Airflow Connection etl_postgres
Loads data into Postgres table customer_behavior

#  **Preprocessing Logic (Python OOP)**

All transformations are implemented inside:
processor/preprocessing.py

**Key Features:**
OOP class: CustomerBehaviorPreprocessor
Ensures cleaner, modular, testable code
Steps include:
Handling missing values
Converting boolean fields
Cleaning string categories
Type casting
Saving the final dataset
---
#  **Postgres Integration**

The database service is defined in:

docker-compose.override.yml

Custom database created:
DB name: customer_behavior
User: etl_user
Password: etl_password
Host (inside Airflow): etl_db
Port: 5432

Airflow connects via:

Connection ID: etl_postgres
Type: Postgres
Host: etl_db
User: etl_user
Password: etl_password
Port: 5432


Loaded table name:

customer_behavior
---
# **Author**

Nastaran Eb
Data Science & Data Engineering Enthusiast
Tampere, Finland

#⭐ **Support**

If you find this project useful, please consider giving it a GitHub Star!


