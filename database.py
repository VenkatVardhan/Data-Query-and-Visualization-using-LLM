from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME
from urllib.parse import quote_plus

password = quote_plus(DB_PASSWORD)

Base = declarative_base()

class CompanyExpenditure(Base):
    __tablename__ = 'expenditure'

    ExpenditureID = Column(Integer, primary_key=True, autoincrement=True)
    Month = Column(String(20), nullable=False)
    Year = Column(Integer, nullable=False)
    RnDSpend = Column(Float, nullable=False)
    AdministrationSpend = Column(Float, nullable=False)
    MarketingSpend = Column(Float, nullable=False)
    TotalSpend = Column(Float, nullable=False)

    def __init__(self, Month, Year, RnDSpend, AdministrationSpend, MarketingSpend, TotalSpend):
        self.Month = Month
        self.Year = Year
        self.RnDSpend = RnDSpend
        self.AdministrationSpend = AdministrationSpend
        self.MarketingSpend = MarketingSpend
        self.TotalSpend = TotalSpend

class Customer(Base):
    __tablename__ = 'customers'

    CustomerID = Column(Integer, primary_key=True, autoincrement=True)
    CustomerName = Column(String(50), nullable=False)
    CustomerEmail = Column(String(50), nullable=False)
    CustomerPhone = Column(String(15), nullable=False)
    CustomerAddress = Column(String(100), nullable=False)

    def __init__(self, CustomerName, CustomerEmail, CustomerPhone, CustomerAddress):
        self.CustomerName = CustomerName
        self.CustomerEmail = CustomerEmail
        self.CustomerPhone = CustomerPhone
        self.CustomerAddress = CustomerAddress

class Product(Base):
    __tablename__ = 'products'

    ProductID = Column(Integer, primary_key=True, autoincrement=True)
    ProductName = Column(String(50), nullable=False)
    ProductPrice = Column(Float, nullable=False)
    ProductAvailableQuantity = Column(Integer, nullable=False)

    def __init__(self, ProductName, ProductPrice, ProductAvailableQuantity):
        self.ProductName = ProductName
        self.ProductPrice = ProductPrice
        self.ProductAvailableQuantity = ProductAvailableQuantity

class Order(Base):
    __tablename__ = 'orders'

    OrderID = Column(Integer, primary_key=True, autoincrement=True)
    ProductID = Column(Integer, ForeignKey('products.ProductID'), nullable=False)
    CustomerID = Column(Integer, ForeignKey('customers.CustomerID'), nullable=False)
    Quantity = Column(Integer, nullable=False)
    SaleDate = Column(Date, nullable=False)
    CustomerAddress = Column(String(100), nullable=False)

    def __init__(self, ProductID, CustomerID, Quantity, SaleDate, CustomerAddress):
        self.ProductID = ProductID
        self.CustomerID = CustomerID
        self.Quantity = Quantity
        self.SaleDate = SaleDate
        self.CustomerAddress = CustomerAddress

class Income(Base):
    __tablename__ = 'income'

    IncomeID = Column(Integer, primary_key=True, autoincrement=True)
    Month = Column(String(20), nullable=False)
    Year = Column(Integer, nullable=False)
    CustomerID = Column(Integer, ForeignKey('customers.CustomerID'), nullable=False)
    MonthlyIncome = Column(Float, nullable=False)
    PaymentMethod = Column(String(10), nullable=False)

    def __init__(self, Month, Year, CustomerID, MonthlyIncome, PaymentMethod):
        self.Month = Month
        self.Year = Year
        self.CustomerID = CustomerID
        self.MonthlyIncome = MonthlyIncome
        self.PaymentMethod = PaymentMethod

# MySQL Connection
db_uri = f"mysql+mysqlconnector://{DB_USERNAME}:{password}@{DB_HOST}/{DB_NAME}"
engine = create_engine(db_uri)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
print("success")

# Sample data
customers_data = [
    ('John Doe', 'john@example.com', '1234567890', '123 Elm Street'),
    ('Jane Smith', 'jane@example.com', '0987654321', '456 Oak Avenue'),
    ('Jim Brown', 'jim@example.com', '1112223333', '789 Pine Road')
]

products_data = [
    ('Laptop', 1000.00, 50),
    ('Smartphone', 800.00, 200),
    ('Tablet', 400.00, 150)
]

orders_data = [
    (1, 1, 2, '2022-01-15', '123 Elm Street'),
    (2, 2, 1, '2022-02-16', '456 Oak Avenue'),
    (3, 3, 3, '2022-03-17', '789 Pine Road'),
    (1, 1, 2, '2022-04-15', '123 Elm Street'),
    (2, 2, 1, '2022-05-16', '456 Oak Avenue'),
    (3, 3, 3, '2022-06-17', '789 Pine Road'),
    (1, 1, 2, '2022-07-15', '123 Elm Street'),
    (2, 2, 1, '2022-08-16', '456 Oak Avenue'),
    (3, 3, 3, '2022-09-17', '789 Pine Road'),
    (1, 1, 2, '2022-10-15', '123 Elm Street'),
    (2, 2, 1, '2022-11-16', '456 Oak Avenue'),
    (3, 3, 3, '2022-12-17', '789 Pine Road'),
    (1, 1, 2, '2023-01-15', '123 Elm Street'),
    (2, 2, 1, '2023-02-16', '456 Oak Avenue'),
    (3, 3, 3, '2023-03-17', '789 Pine Road'),
    (1, 1, 2, '2023-04-15', '123 Elm Street'),
    (2, 2, 1, '2023-05-16', '456 Oak Avenue'),
    (3, 3, 3, '2023-06-17', '789 Pine Road'),
    (1, 1, 2, '2023-07-15', '123 Elm Street'),
    (2, 2, 1, '2023-08-16', '456 Oak Avenue'),
    (3, 3, 3, '2023-09-17', '789 Pine Road'),
    (1, 1, 2, '2023-10-15', '123 Elm Street'),
    (2, 2, 1, '2023-11-16', '456 Oak Avenue'),
    (3, 3, 3, '2023-12-17', '789 Pine Road')
]
income_data = [
    ('January', 2022, 1, 5000.00, 'CreditCard'),
    ('February', 2022, 2, 6000.00, 'Cash'),
    ('March', 2022, 3, 7000.00, 'Check'),
    ('April', 2022, 1, 5000.00, 'CreditCard'),
    ('May', 2022, 2, 6000.00, 'Cash'),
    ('June', 2022, 3, 7000.00, 'Check'),
    ('July', 2022, 1, 5000.00, 'CreditCard'),
    ('August', 2022, 2, 6000.00, 'Cash'),
    ('September', 2022, 3, 7000.00, 'Check'),
    ('October', 2022, 1, 5000.00, 'CreditCard'),
    ('November', 2022, 2, 6000.00, 'Cash'),
    ('December', 2022, 3, 7000.00, 'Check'),
    ('January', 2023, 1, 5000.00, 'CreditCard'),
    ('February', 2023, 2, 6000.00, 'Cash'),
    ('March', 2023, 3, 7000.00, 'Check'),
    ('April', 2023, 1, 5000.00, 'CreditCard'),
    ('May', 2023, 2, 6000.00, 'Cash'),
    ('June', 2023, 3, 7000.00, 'Check'),
    ('July', 2023, 1, 5000.00, 'CreditCard'),
    ('August', 2023, 2, 6000.00, 'Cash'),
    ('September', 2023, 3, 7000.00, 'Check'),
    ('October', 2023, 1, 5000.00, 'CreditCard'),
    ('November', 2023, 2, 6000.00, 'Cash'),
    ('December', 2023, 3, 7000.00, 'Check')
]

expenditure_data = [
    ('January', 2022, 1000.00, 500.00, 2000.00, 3500.00),
    ('February', 2022, 1200.00, 600.00, 2500.00, 4300.00),
    ('March', 2022, 1100.00, 550.00, 2300.00, 3950.00),
    ('April', 2022, 1050.00, 525.00, 2100.00, 3675.00),
    ('May', 2022, 1150.00, 575.00, 2200.00, 3925.00),
    ('June', 2022, 1250.00, 625.00, 2400.00, 4275.00),
    ('July', 2022, 1300.00, 650.00, 2500.00, 4450.00),
    ('August', 2022, 1350.00, 675.00, 2600.00, 4625.00),
    ('September', 2022, 1400.00, 700.00, 2700.00, 4800.00),
    ('October', 2022, 1450.00, 725.00, 2800.00, 4975.00),
    ('November', 2022, 1500.00, 750.00, 2900.00, 5150.00),
    ('December', 2022, 1550.00, 775.00, 3000.00, 5325.00),
    ('January', 2023, 1600.00, 800.00, 3100.00, 5500.00),
    ('February', 2023, 1650.00, 825.00, 3200.00, 5675.00),
    ('March', 2023, 1700.00, 850.00, 3300.00, 5850.00),
    ('April', 2023, 1750.00, 875.00, 3400.00, 6025.00),
    ('May', 2023, 1800.00, 900.00, 3500.00, 6200.00),
    ('June', 2023, 1850.00, 925.00, 3600.00, 6375.00),
    ('July', 2023, 1900.00, 950.00, 3700.00, 6550.00),
    ('August', 2023, 1950.00, 975.00, 3800.00, 6725.00),
    ('September', 2023, 2000.00, 1000.00, 3900.00, 6900.00),
    ('October', 2023, 2050.00, 1025.00, 4000.00, 7075.00),
    ('November', 2023, 2100.00, 1050.00, 4100.00, 7250.00),
    ('December', 2023, 2150.00, 1075.00, 4200.00, 7425.00)
]
try:
    for customer in customers_data:
        exists = session.query(Customer).filter_by(
            CustomerName=customer[0],
            CustomerEmail=customer[1],
            CustomerPhone=customer[2],
            CustomerAddress=customer[3]
        ).first()
        if not exists:
            session.add(Customer(*customer))
    
    for product in products_data:
        exists = session.query(Product).filter_by(
            ProductName=product[0],
            ProductPrice=product[1],
            ProductAvailableQuantity=product[2]
        ).first()
        if not exists:
            session.add(Product(*product))

    for order in orders_data:
        exists = session.query(Order).filter_by(
            ProductID=order[0],
            CustomerID=order[1],
            Quantity=order[2],
            SaleDate=order[3],
            CustomerAddress=order[4]
        ).first()
        if not exists:
            session.add(Order(*order))
        
        for income in income_data:
            exists = session.query(Income).filter_by(
                Month=income[0],
                Year=income[1],
                CustomerID=income[2],
                MonthlyIncome=income[3],
                PaymentMethod=income[4]
            ).first()
            if not exists:
                session.add(Income(*income))

    for expenditure in expenditure_data:
        exists = session.query(CompanyExpenditure).filter_by(
            Month=expenditure[0],
            Year=expenditure[1],
            RnDSpend=expenditure[2],
            AdministrationSpend=expenditure[3],
            MarketingSpend=expenditure[4],
            TotalSpend=expenditure[5]
        ).first()
        if not exists:
            session.add(CompanyExpenditure(*expenditure))

    session.commit()
    print("Data inserted successfully.")
except Exception as e:
    print("Error:", e)
    session.rollback()
finally:
    session.close()
