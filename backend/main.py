from fastapi import FastAPI
from models import User, Expense 
from database import engine, Base

app=FastAPI()
@app.get("/")
def read_root():
    return{"message":"The web server is running"}