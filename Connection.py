from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME
from urllib.parse import quote_plus


password = quote_plus(DB_PASSWORD)

Base = declarative_base()


class CompanyExpenditure(Base):
    __tablename__ = 'Expenditure'  

    ExpenditureID = Column(Integer, primary_key=True, autoincrement=True)
    CompanyName = Column(String(50), nullable=False)
    ExpenseType = Column(String(50), nullable=False)
    Amount = Column(Float(precision=2), nullable=False)
    Year = Column(Integer, nullable=False)
    Department = Column(String(20), nullable=False)
    PaymentMethod = Column(String(10), nullable=False)
    AnnualIncome = Column(Float(precision=2))

    def __init__(self, CompanyName, ExpenseType, Amount, Year, Department, PaymentMethod, AnnualIncome):
        self.CompanyName = CompanyName
        self.ExpenseType = ExpenseType
        self.Amount = Amount
        self.Year = Year
        self.Department = Department
        self.PaymentMethod = PaymentMethod
        self.AnnualIncome = AnnualIncome

# MySQL Connection
db_uri = f"mysql+mysqlconnector://{DB_USERNAME}:{password}@{DB_HOST}/{DB_NAME}"


# Encode the password

engine = create_engine(db_uri)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
print("success")

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
    for d in data:
            # Check if the record already exists
            exists = session.query(CompanyExpenditure).filter_by(
                CompanyName=d[0],
                ExpenseType=d[1],
                Amount=d[2],
                Year=d[3],
                Department=d[4],
                PaymentMethod=d[5],
                AnnualIncome=d[6]
            ).first()

            if not exists:
                company_expense = CompanyExpenditure(*d)
                session.add(company_expense)

    session.commit()
  
    print("Data inserted successfully.")
except Exception as e:
    print("Error:", e)
    session.rollback()
finally:
    session.close()
