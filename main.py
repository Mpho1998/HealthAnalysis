import pandas as pd
import pyodbc
import urllib
from SQL_Queries import queries
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

server = 'localhost'
database = 'PatientAdmissions'

# Encode the driver
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

# Create the SQLAlchemy engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
try:
    with engine.connect() as conn:
        print("✅ Connected to the database successfully.")
except Exception as e:
    print("❌ Failed to connect to the database:", e)

dataframes = {name: pd.read_sql_query(query, engine) for name, query in queries.items()}

df_monthly_admissions = dataframes['Admissions per Month']
df_admissions_dept = dataframes['Total Admissions per Department']
df_long_stays = dataframes['Patients with Hospital Stay > 7 Days']
df_top_diagnosis = dataframes['Most Frequent Diagnosis']

sns.set_style("whitegrid")
plt.figure(figsize=(16, 10))

# 1. Admissions per Department
plt.subplot(2, 2, 1)
sns.barplot(x='Total_Admissions', y='department_name', data=df_admissions_dept, palette='Blues_d',
            hue='department_name', dodge=False, legend=False)
plt.title('Admissions per Department', fontsize=14)
plt.xlabel('Total Admissions')
plt.ylabel('Department')

# 2. Monthly Admissions
plt.subplot(2, 2, 2)
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']
sns.barplot(x='Month', y='Number_Of_Admissions_Per_Month', data=df_monthly_admissions, order=month_order,
            palette='Purples_d', hue='Month', dodge=False, legend=False)
plt.title('Monthly Admissions', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Admissions')
plt.xticks(rotation=45)

# 3. Histogram: Patient Stay Duration > 7 Days
plt.subplot(2, 2, 3)
plt.hist(df_long_stays['Number_Of_Stay'], bins=10, color='darkcyan', edgecolor='black')
plt.title('Patient Stay Duration (> 7 Days)', fontsize=14)
plt.xlabel('Number of Days Stayed')
plt.ylabel('Number of Patients')

# 4. Top Diagnoses
plt.subplot(2, 2, 4)
sns.barplot(x='Number_of_diagnosis', y='diagnosis', data=df_top_diagnosis, palette='Oranges_d', hue='diagnosis',
            dodge=False, legend=False)
plt.title('Top 3 Diagnoses', fontsize=14)
plt.xlabel('Frequency')
plt.ylabel('Diagnosis')

# Layout
plt.suptitle('Patient Admissions Dashboard', fontsize=18, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
