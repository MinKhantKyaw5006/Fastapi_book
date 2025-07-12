from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "Hello World"}

# pass parameter's variable to pass within the url to test

# passing with query paramter /greet/?name=lucas
# mix of variable nad query = greet/lucas?age=21


@app.get('/greet/{name}')
async def greet_name(name: str, age: int) -> dict:
    return {"message": f"Hello World {name}", "age": age}
