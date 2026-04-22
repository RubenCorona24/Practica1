from fastapi import FastAPI #importamos fastapi

app = FastAPI(
    title='Mi primera appi',
    description="Aprendiendo FastApi",
    version= '0.1.0'
)

@app.get("/")
async def root():
    return {"message": "Hola Mundo!"}

@app.get("/items/")
async def read_items():
    return [{"name":"Item 1"},{"name":"Item 2"}]
