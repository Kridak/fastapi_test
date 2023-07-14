from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Test for PEGA GPT"}

@app.get("/name")
async def root(Name:str):
    return {f"Hello: {Name}"}

