queries = {
    # Total Admissions per Department
    "Total Admissions per Department": """
        SELECT D.department_name,Count(A.department_id) AS Total_Admissions
        From Admissions	A
        INNER JOIN Departments D ON A.department_id = D.department_id
        GROUP BY D.department_name
    """,

    # Hospital Stay (average duration per diagnosis)
    "Hospital Stay per Diagnosis": """
        SELECT P.diagnosis, AVG(DATEDIFF(DAY,A.admission_date,A.discharge_date)) AS Hospital_Stay
        FROM Admissions A
        INNER JOIN Patients P ON A.patient_id=P.patient_id
        GROUP BY P.diagnosis
    """,

    # Unique Admissions (only second admissions per patient)
    "Second Admission per Patient": """
        WITH Admission_CTE AS (
            SELECT P.patient_id, P.name, ROW_NUMBER() OVER (PARTITION BY P.patient_id ORDER BY P.name) AS Unique_Row
            FROM Admissions A
            INNER JOIN Patients P ON P.patient_id = A.patient_id
        )
        SELECT patient_id, name
        FROM Admission_CTE
        WHERE Unique_Row = 2
    """,

    # Top 3 departments by admissions
    "Top 3 Departments by Admissions": """
        SELECT TOP 3 D.department_name, COUNT(A.department_id) AS Total_Admissions
        FROM Admissions A
        INNER JOIN Departments D ON A.department_id = D.department_id
        GROUP BY D.department_name
        ORDER BY Total_Admissions DESC
    """,

    # Cost per Department (total and average cost)
    "Cost per Department": """
        SELECT D.department_name, SUM(A.total_cost) AS Cost_Per_Dept, ROUND(AVG(A.total_cost), 2) AS Average
        FROM Admissions A
        INNER JOIN Departments D ON A.department_id = D.department_id
        GROUP BY D.department_name
    """,

    # Admissions per Month
    "Admissions per Month": """
        SELECT DATENAME(MONTH, A.admission_date) AS Month,DATENAME(YEAR, A.admission_date) AS Year, COUNT(DATENAME(MONTH, A.admission_date)) AS Number_Of_Admissions_Per_Month
        FROM Admissions A
        GROUP BY DATENAME(MONTH, A.admission_date),DATENAME(YEAR, A.admission_date)
    """,

    # Percentage of patients with more than one admission
    "Percentage of Patients with Multiple Admissions": """
        WITH Perc_CTE AS (
            SELECT P.patient_id, P.name,count(A.admission_id) AS Number_Of_Admission
            FROM Patients P
            INNER JOIN Admissions A ON P.patient_id = A.patient_id
            GROUP BY P.patient_id,P.name
            HAVING COUNT(P.patient_id) > 1
        )
        SELECT (COUNT(C.Number_Of_Admission)*100 / (SELECT COUNT(DISTINCT patient_id) FROM Patients)) AS Percentage	
        FROM Perc_CTE C
    """,

    # Outcome per Patient (number of patients with each outcome)
    "Outcome per Patient": """
        SELECT A.outcome, COUNT(DISTINCT P.patient_id) AS Number_of_Patients
        FROM Admissions A
        INNER JOIN Patients P ON P.patient_id = A.patient_id
        GROUP BY A.outcome
    """,

    # Patients with hospital stay > 7 days
    "Patients with Hospital Stay > 7 Days": """
        SELECT P.name, A.admission_date, A.discharge_date, DATEDIFF(DAY, A.admission_date, A.discharge_date) AS Number_Of_Stay
        FROM Patients P
        INNER JOIN Admissions A ON P.patient_id = A.patient_id
        WHERE DATEDIFF(DAY, A.admission_date, A.discharge_date) > 7
    """,

    # Department with the highest total cost
    "Department with Highest Total Cost": """
        SELECT TOP 1 D.department_name, SUM(A.total_cost) AS Dept_Total_Cost
        FROM Admissions A
        INNER JOIN Departments D ON A.department_id = D.department_id
        GROUP BY D.department_name
        ORDER BY Dept_Total_Cost DESC
    """,

    # Admissions per Gender
    "Admissions per Gender": """
        SELECT P.gender, COUNT(DISTINCT P.patient_id) AS Number_of_Admissions
        FROM Admissions A
        INNER JOIN Patients P ON A.patient_id = P.patient_id
        GROUP BY P.gender
    """,

    # Admissions per Age Group (categorized)
    "Admissions per Age Group": """
        WITH AgeGroup_CTE AS (
            SELECT P.age,
            CASE 
                WHEN P.age >= 0 AND P.age <= 18 THEN '0-18'
                WHEN P.age >= 19 AND P.age <= 60 THEN '19-60'
                ELSE '61+'
            END AS Age_Groups,
            COUNT(A.admission_id) AS Number_of_admissions
            FROM Patients P
            INNER JOIN Admissions A ON A.patient_id = P.patient_id
            GROUP BY P.age
        )
        SELECT Age_Groups, SUM(Number_of_admissions) AS Number_of_admissions
        FROM AgeGroup_CTE
        GROUP BY Age_Groups
    """,

    # Most Frequent Diagnosis
    "Most Frequent Diagnosis": """
        SELECT TOP 3 P.diagnosis, COUNT(P.diagnosis) AS Number_of_diagnosis
        FROM Admissions A
        INNER JOIN Patients P ON P.patient_id = A.patient_id
        GROUP BY P.diagnosis
        ORDER BY Number_of_diagnosis DESC
    """,

    # First and Latest Admission Dates per Patient
    "First and Latest Admission Dates": """
        SELECT P.name, MIN(A.admission_date) AS First_Admission, MAX(A.admission_date) AS Latest_Admission
        FROM Admissions A
        INNER JOIN Patients P ON P.patient_id = A.patient_id
        GROUP BY P.name
    """
}
