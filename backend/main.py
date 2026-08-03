from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def read_root():
    return {"massage": "The Expnse Analizer API is running!"} 