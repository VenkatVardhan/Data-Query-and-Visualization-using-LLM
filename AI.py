
import os
from dotenv import load_dotenv
from openai import OpenAI
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from database import CompanyExpenditure, Customer, Product, Order, Income

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print("'.env' file not found.")

DB_USERNAME=os.getenv('DB_USERNAME')
DB_HOST=os.getenv('DB_HOST')
DB_NAME=os.getenv('DB_NAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

password = quote_plus(DB_PASSWORD)
db_uri = f"mysql+mysqlconnector://{DB_USERNAME}:{password}@{DB_HOST}/{DB_NAME}"
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)

table_to_model = {
    'expenditure': CompanyExpenditure,
    'customers': Customer,
    'products': Product,
    'orders': Order,
    'income': Income
}

allowed_table_names = set(table_to_model.keys())

forbidden_keywords = {"alter", "delete", "drop", "update", "insert", "create", "modify"}

def generate_sql_query(user_input):
    try:
        if not any(table_name in user_input.lower() for table_name in allowed_table_names):
            return "Please provide a query related to the database tables."

        prompt = f"Convert the following natural language query into SQL:\n\"{user_input}\"\n\n"
        prompt += "The customers table has fields: CustomerID, CustomerName, CustomerEmail, CustomerPhone, CustomerAddress.\n"
        prompt += "The products table has fields: ProductID, ProductName, ProductPrice, ProductAvailableQuantity.\n"
        prompt += "The orders table has fields: OrderID, ProductID, CustomerID, Quantity, SaleDate, CustomerAddress.\n"
        prompt += "The income table has fields: IncomeID, Month, Year, CustomerID, MonthlyIncome, PaymentMethod.\n"
        prompt += "The expenditure table has fields: ExpenditureID, Month, Year, RnDSpend, AdministrationSpend, MarketingSpend, TotalSpend.\n"
        
        completion = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt + user_input,
            max_tokens=150,
            temperature=0.7
        )
        sql_query = completion.choices[0].text.strip()
        sql_query = sql_query.lstrip(":").strip()
        for table_name, model_class in table_to_model.items():
            sql_query = sql_query.replace(table_name, model_class.__tablename__)
        
        return sql_query
    except Exception as e:
        return f"Error generating SQL query: {str(e)}"

def contains_forbidden_keywords(sql_query):
    lower_query = sql_query.lower()
    return any(keyword in lower_query for keyword in forbidden_keywords)

def execute_query(sql_query):
    session = Session()
    try:
        if contains_forbidden_keywords(sql_query):
            return "Forbidden operation detected. This query cannot be executed.", []

        result = session.execute(text(sql_query))
        session.commit()
        return result.fetchall(), result.keys()
    except Exception as e:
        session.rollback()
        return f"Error executing SQL query: {str(e)}", []
    finally:
        session.close()
