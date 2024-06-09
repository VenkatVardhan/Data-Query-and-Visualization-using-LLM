import sys
from faker import Faker
import random
import mysql.connector


#mysql connection code with password and database
mydb = mysql.connector.connect(host="localhost",user="root",password="Sreeneves@1",database="vardhan")
if mydb.is_connected():
    print("Connection is established")
mycursor = mydb.cursor()

mycursor.execute('''CREATE TABLE IF NOT EXISTS CompanyExpenditure (
    ExpenditureID INT AUTO_INCREMENT PRIMARY KEY,
    CompanyName VARCHAR(50) NOT NULL,
    ExpenseType VARCHAR(50) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Year INT NOT NULL,
    Department VARCHAR(20) NOT NULL,
    PaymentMethod VARCHAR(10) NOT NULL,
    AnnualIncome DECIMAL(10, 2)
);''')

sql_insert = '''
INSERT INTO CompanyExpenditure (CompanyName, ExpenseType, Amount, Year, Department, PaymentMethod, AnnualIncome) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
'''

data = [
    ('Apple Inc.', 'Office Supplies', 500.00, 2022, 'HR', 'CreditCard', 1000000.00),
    ('Microsoft Corporation', 'Marketing', 1200.00, 2021, 'Marketing', 'Cash', 1500000.00),
    ('Google LLC', 'Travel', 800.00, 2023, 'Finance', 'Check', 2000000.00),
    ('Amazon.com Inc.', 'Utilities', 700.00, 2020, 'IT', 'CreditCard', 1800000.00),
    ('Facebook Inc.', 'Marketing', 1500.00, 2022, 'Sales', 'Check', 2200000.00),
    ('Tesla, Inc.', 'Office Supplies', 600.00, 2021, 'HR', 'Cash', 1700000.00),
    ('Alphabet Inc.', 'Travel', 900.00, 2023, 'Finance', 'CreditCard', 2500000.00),
    ('Oracle Corporation', 'Utilities', 800.00, 2020, 'IT', 'Check', 1900000.00),
    ('Walmart Inc.', 'Marketing', 1300.00, 2022, 'Sales', 'Cash', 2300000.00),
    ('Johnson & Johnson', 'Office Supplies', 700.00, 2021, 'HR', 'CreditCard', 1600000.00),
    ('Apple Inc.', 'Office Supplies', 450.00, 2022, 'IT', 'Cash', 1000000.00),
    ('Microsoft Corporation', 'Marketing', 1100.00, 2021, 'Sales', 'CreditCard', 1500000.00),
    ('Google LLC', 'Travel', 750.00, 2023, 'HR', 'Check', 2000000.00),
    ('Amazon.com Inc.', 'Utilities', 650.00, 2020, 'Marketing', 'CreditCard', 1800000.00),
    ('Facebook Inc.', 'Marketing', 1400.00, 2022, 'Finance', 'Cash', 2200000.00),
    ('Tesla, Inc.', 'Office Supplies', 550.00, 2021, 'IT', 'Check', 1700000.00),
    ('Alphabet Inc.', 'Travel', 850.00, 2023, 'Sales', 'Cash', 2500000.00),
    ('Oracle Corporation', 'Utilities', 750.00, 2020, 'HR', 'CreditCard', 1900000.00),
    ('Walmart Inc.', 'Marketing', 1200.00, 2022, 'Marketing', 'Check', 2300000.00),
    ('Johnson & Johnson', 'Office Supplies', 650.00, 2021, 'Finance', 'Cash', 1600000.00)
]
try:

    mycursor.executemany(sql_insert, data)


    mydb.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as err:
    print("Error:", err)
