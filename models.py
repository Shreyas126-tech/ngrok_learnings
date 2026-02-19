from db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True,index=True)
    email=Column(String,unique=True,index=True)
    password=Column(String)
    api_key=Column(String,unique=True,index=True)
