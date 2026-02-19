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
    user_id=Column(Integer,ForeignKey("users.id"),index=True)
    address=Column(String,index=True)
    city=Column(String,index=True)
    state=Column(String,index=True)
    zip_code=Column(String,index=True)

class order(Base):
    __tablename__="orders"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),index=True)
    order_date=Column(DateTime,index=True)
    total_amount=Column(Integer,index=True)
    status=Column(String,index=True)