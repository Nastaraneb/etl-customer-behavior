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

# 🛠 **How to Run the Project (Step-by-Step)**
1️. Clone the Repository





