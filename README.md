🏥 Healthcare Admissions Data Analysis (SQL + Python)
📌 Overview
This project explores a healthcare admissions dataset using SQL for data analysis and Python (Matplotlib) for visualization. The goal is to uncover insights about hospital admissions, diagnosis trends, cost distribution, and patient outcomes — all relevant to data-driven decision-making in the healthcare sector.

🔧 Tools & Technologies
SQL Server (Microsoft SQL)

SQLAlchemy + pyodbc for database connectivity

Pandas for data manipulation

Matplotlib for visualization

Jupyter Notebook or Python script for execution

🗃️ Dataset
The dataset consists of three core tables:

Patients: Patient demographics and diagnosis

Admissions: Records of hospital visits including cost, date, and outcomes

Departments: Hospital departments related to admissions

Note: Synthetic data was generated for learning purposes.

🔍 Key SQL Queries & Analysis
The project executes a series of SQL queries stored in a Python dictionary, including:

Total admissions by department

Average length of stay by diagnosis

Readmission analysis (patients with more than one visit)

Diagnosis frequency (Top 3 diagnoses)

Admissions trends over months

Cost analysis by department

Gender distribution of admissions

Patient outcomes (Recovered, Deceased, etc.)

Top costliest departments and patients

📊 Dashboard Visualizations (Matplotlib Subplots)
The following plots were generated:

🔹 Bar Chart: Top 3 Most Frequent Diagnoses

🔹 Line Chart: Admissions by Month

🔹 Pie Chart: Patient Outcomes

🔹 Bar Chart: Admissions by Age Group

🔹 Histogram: Patient Stay Duration > 7 Days

🧠 Key Insights
Certain departments have significantly higher admission volumes.

A small set of diagnoses accounts for a large share of admissions.

There are seasonal trends in hospital admissions.

A notable portion of patients are readmitted, indicating chronic issues or incomplete recovery.

Most patients recover, but cost and stay duration vary significantly.

🚀 How to Run
Ensure SQL Server is installed and database PatientAdmissions is restored.

Install Python dependencies:

bash
Copy
Edit
pip install sqlalchemy pyodbc pandas matplotlib seaborn
Update your database connection in the script:

python
Copy
Edit
connection_string = "mssql+pyodbc://localhost/PatientAdmissions?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
Run the Python script to load data and generate plots.

