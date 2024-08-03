from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

DATABASE_URL = (
    "Driver={ODBC Driver 18 for SQL Server};Server=tcp:kartikay.database.windows.net,1433;Database=harit;Uid=kartikay;Pwd=Sunny439@;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
)

connection_string = URL.create("mssql+pyodbc", query={"odbc_connect": DATABASE_URL})
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
