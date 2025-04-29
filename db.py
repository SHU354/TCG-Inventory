import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models import Base

load_dotenv()

USER = os.getenv('DB_USER')
PASS = os.getenv('DB_PASS')
HOST = os.getenv('DB_HOST', '127.0.0.1')
PORT = os.getenv('DB_PORT', '3306')
NAME = os.getenv('DB_NAME')

URI = f"mysql+mysqlconnector://{USER}:{PASS}@{HOST}:{PORT}/{NAME}"
engine = create_engine(URI, echo=False)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
