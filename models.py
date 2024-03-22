from sqlalchemy import MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    second_name = Column(String(100), nullable=False)
    hobbie = Column(String(255), nullable=False)
    birth_year = Column(DateTime(), nullable=False)
    marks = Column(Integer, default=0)