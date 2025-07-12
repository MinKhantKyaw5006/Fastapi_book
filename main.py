from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "Hello World"}

# pass parameter's variable to pass within the url to test

# passing with query paramter /greet/?name=lucas
# mix of variable nad query = greet/lucas?age=21


@app.get('/greet')
async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}
