from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home_page():
    return {"Hello": "World"}

@app.get("/data/")
def get_data():
    return {"data": "This is sample data from the API"}