from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "Hello World"}

# pass parameter's variable to pass within the url to test


@app.get('/greet')
async def greet_name(name: str) -> dict:
    return {"message": f"Hello World {name}"}
