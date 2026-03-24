from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home_page():
    return {"Hello": "World"}

@app.get("/data/")
def get_data():
    return {
        "ID": 1,
        'Name': 'Sivamani',
        "Email": 'sivamani@gmail.com',
        "Phone": '9848032919'
    }