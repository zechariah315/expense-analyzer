from fastapi import FastAPI
from routers import expenses, users, auth


app=FastAPI()
app.include_router(users.router)
app.include_router(expenses.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return{"message":"The web server is running"}

