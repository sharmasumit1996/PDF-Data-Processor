# PDF Data Processor

## Problem Statement
Many data-driven projects involve extracting data from various sources, such as CSV and XML files, and transforming it for analysis or storage. However, ensuring the quality and integrity of this data throughout the process can be challenging. Till now, we have made the ELT pipelines for extraction, schema validations and transformations. Now, the goal is to automate the entire process using AirFlow and develop API's with a user interface to give the end user the power to implement it all using single-click operations.

## Project Goals
The aim of this project is to develop a robust web application workflow for processing and extracting data from PDF files. Below is a breakdown of the tasks implemented in the flow to achieve our project objectives:

1. User Interface
Implement a user-friendly interface to handle PDF uploads and user queries.
2. Application Hosting and Containerization
Deploy Google Cloud Engines to host the web application, allowing for scalable processing power.
Utilize Docker to containerize the application, ensuring consistent environments and easy deployment across instances.
3. Automation and Processing Pipeline
Integrate Streamlit to create an interactive web interface for users to upload PDF files directly into the system.
Utilize FastAPI to build efficient and performant RESTful APIs for handling user queries and automating interactions with the processing pipeline.
4. Workflow Execution and Data Management
Implement an automated pipeline, triggered by Airflow, to manage tasks from PDF upload on S3 to deployment on GCP.
Store PDF files securely and manage them effectively using S3.
5. Data Extraction and Validation
Run snowflake_objects.sql file to create objects into snowflake required for the application.
Automate the extraction of data from PDF files using Python scripts.
Validate extracted data with Pydantic to ensure integrity and structure before further processing.
6. Data Loading and Storage
Load the validated data into Snowflake, a cloud data warehouse, for persistent storage, analysis, and reporting.
Ensure that both PDF content and metadata are handled correctly during the loading process.
The successful implementation of these tasks will result in a streamlined process for PDF data management, from the point of user interaction to data storage and analysis. Our workflow is designed to be resilient, scalable, and maintainable, with clear separation of concerns and ease of monitoring.

## Technologies Used

![STREAMLIT](https://camo.githubusercontent.com/121d8055ce25931b33557341b1397ec6721dca05b7f07978cbf3c9b9f4509b13/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53747265616d6c69742d4646344234423f7374796c653d666f722d7468652d6261646765266c6f676f3d73747265616d6c6974266c6f676f436f6c6f723d7768697465)
![PYTHON](https://camo.githubusercontent.com/9b071a101345849864a7ceb6b7f4fd417736f7cad1fe3c932bedfa09c2de43bc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3442384242453f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d79656c6c6f77)
![PANDAS](https://camo.githubusercontent.com/a38f77f5b33450d816dc95e4ac3f2fd9aad080d2bb6b4c54c85a79fcf3b8f8f8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50616e6461732d3135303435383f7374796c653d666f722d7468652d6261646765266c6f676f3d70616e646173266c6f676f436f6c6f723d7768697465)
![AIRFLOW](https://camo.githubusercontent.com/90283584a4d10128fab5d50234c7e8c51890dca9fba7a2eed2c134c4ff3d9650/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4170616368655f416972666c6f772d3030413745313f7374796c653d666f722d7468652d6261646765266c6f676f3d6170616368652d616972666c6f77266c6f676f436f6c6f723d7768697465)
![AMAZON S3](https://camo.githubusercontent.com/e2797019197ecc78e7b0b1242100f9d536442d89c10a06f8bc3813d428d7f8f3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f416d617a6f6e5f53332d4637434131383f7374796c653d666f722d7468652d6261646765266c6f676f3d616d617a6f6e2d7333266c6f676f436f6c6f723d7768697465)
![DOCKER](https://camo.githubusercontent.com/e20a054f7480fe4d651329ca4d15dc16767671ea36971dfca72ccf90413d615a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3064623765643f7374796c653d666f722d7468652d6261646765266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465)
![GOOGLE CLOUD](https://camo.githubusercontent.com/9bd9f9218a1c67f5069d37db967e8857b18e34acece18ea1a05333412951e993/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476f6f676c655f436c6f75642d3432383546343f7374796c653d666f722d7468652d6261646765266c6f676f3d676f6f676c65636c6f7564266c6f676f436f6c6f723d7768697465)
![SNOWFLAKE](https://camo.githubusercontent.com/dc35a1d40a4c61e5b08851b29a05998c1150fa48e739484e1087bdd6ac9ac6b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f536e6f77666c616b652d3239423545383f7374796c653d666f722d7468652d6261646765266c6f676f3d736e6f77666c616b65266c6f676f436f6c6f723d7768697465)
[![FastAPI](https://camo.githubusercontent.com/d9fcef32b07a52e62acde87c779d3a33b6c0d7111149031c2cef1ec24f9c802c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f666173746170692d3130393938393f7374796c653d666f722d7468652d6261646765266c6f676f3d46415354415049266c6f676f436f6c6f723d7768697465)](https://fastapi.tiangolo.com/) 

## Related Links:

- [![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1rR8MdTSyWoAmdOa4enqDqAAH6V3XI_wwgrctNUDVrQQ/edit#4)

Pre-requisites
Before running this project, ensure you have the following prerequisites set up:

Python: Ensure Python is installed on your system.

Docker: Ensure Docker-desktop is installed on your system.

Virtual Environment: Set up a virtual environment to manage dependencies and isolate your project's environment from other Python projects. You can create a virtual environment using virtualenv or venv.

requirements.txt: Install the required Python dependencies by running the command:

pip install -r requirements.txt
Config File: Set up the configurations file with the necessary credentials and configurations.

Snowflake: Use airflow/dags/load/snowflake_objects.sql to define the queries on snowflake. Also, ensure you have the necessary credentials and configurations set up in the configurations file for connecting to Snowflake.

Google Cloud Platform: Create a Google Cloud Engine. Ensure you have the necessary credentials and configurations set up in the configurations.properties file.

## Project Structure
```
📦 Assignment04
├─ .gitignore
├─ Makefile
├─ README.md
├─ docker-compose.yaml
├─ streamlit
│  ├─ .gitignore
│  ├─ __init__.py
│  ├─ config
│  ├─ dockerfile
│  ├─ main.py
│  └─ requirements.txt
├─ fastapi
│  ├─ .gitignore
│  ├─ dockerfile
│  ├─ main.py
│  └─ requirements.txt
├─ airflow
│  ├─ airflow.cfg
│  ├─ dockerfile
│  ├─ docker-compose.yaml
│  ├─ logs
│  │  └─ scheduler
│  │     └─ latest
│  └─ dags
│     └─ pdf_processing_dag.py
├─ FastAPI2
│  ├─ .gitgnore
│  ├─ dockerfile
│  ├─ main.py
│  └─ requirements.txt
└─ diagrams
   ├─ airflow.png
   ├─ architecture-diagram.ipynb
   ├─ data_architecture_diagram.png
   ├─ docker.png
   ├─ fastapi.png
   ├─ pydantic-logo.png
   ├─ snowflake.png
   ├─ sqlalchemy.png
   └─ streamlit.png
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

**How to Run the Application Locally**
To run the application locally, follow these steps:

Clone the repository to get all the source code on your machine.

Use source/venv/bin/activate to activate the environment.

Create a .env file in the root directory with the following variables:

[AWS]
access_key = 
secret_key = 
region_name = 

[s3-bucket]
bucket = 

[SNOWFLAKE]
user = 
password = 
account =
warehouse =
database =
schema =
role =
content_table_name =
content_stage_name =
metadata_table_name =
metadata_stage_name =
pdf_data_file_format =

[MONGODB]
MONGODB_URL = 
DATABASE_NAME = 
COLLECTION_USER = 
COLLECTION_USER_FILE = 
 
[AIRFLOW]
AIRFLOW_URL =
AIRFLOW_DAG_ID = 
AIRFLOW_USERNAME = 
AIRFLOW_PASSWORD = 

Once you have set up your environment variables, Use docker-compose up - build to run the application

Access the Airflow UI by navigating to http://localhost:8080/ in your web browser.

Once the DAGs have run successfully, view the Streamlit application

Access the Streamlit UI by navigating to http://localhost:8503/ in your web browser.

## Learning Outcomes
**By completing this assignment, you will:**

**Cloud Services Deployment:**
- Deploy and manage applications on GCP Engines.
- Understand the benefits of using cloud services for scalability and reliability.

**Containerization with Docker:**
- Create, manage, and deploy Docker containers to encapsulate application environments.
- Utilize Docker for ensuring consistent deployments and isolating dependencies.

**Interactive Web Interface Creation:**
- Design and implement interactive web interfaces using frameworks like Streamlit.
- Handle file uploads and user input in a web application context.

**API Development:**
- Build RESTful APIs with FastAPI to handle web requests and automate backend processes.
- Integrate API endpoints with the user interface and processing pipeline.

**Automated Workflow Management:**
- Use Apache Airflow to automate and manage the workflow pipeline.
- Understand how to trigger and schedule tasks based on events or conditions.

**Data Extraction Techniques:**
- Develop scripts to extract data from PDF documents.
- Automate the process of extracting structured data from various document formats.

**Data Warehousing and ETL Processes:**
- Load and transform data into a data warehouse like Snowflake.
- Appreciate the role of ETL (Extract, Transform, Load) processes in data analytics.

**Data Security and Storage:**
- Manage secure storage of files using appropriate file storage solutions.
- Understand the considerations for data security in cloud-based storage.

These outcomes will equip learners with the skills and knowledge necessary to architect and implement scalable and efficient data processing systems in a cloud environment, with a focus on containerized applications and automated workflows.
