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
    user_name=Column(String,unique=True,index=True)

class address(Base):
    __tablename__="addresses"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    address=Column(String)
    city=Column(String)
    state=Column(String)
    zip_code=Column(String)

class order(Base):
    __tablename__="orders"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    order_date=Column(DateTime,default=func.now())
    total_amount=Column(Integer)
    status=Column(String)