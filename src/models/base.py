from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:Paizinho01@localhost:5432/sqlalchemy_test')

Session = sessionmaker(bind=engine)

Base = declarative_base()