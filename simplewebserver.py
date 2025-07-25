# from fastapi import FastAPI, Header
# from typing import Optional
# from pydantic import BaseModel
# app = FastAPI()


# @app.get('/')
# async def read_root():
#     return {"message": "Hello World"}

# # pass parameter's variable to pass within the url to test

# # passing with query paramter /greet/?name=lucas
# # mix of variable nad query = greet/lucas?age=21
# # http://127.0.0.1:8000/greet?name=jona&age=21


# @app.get('/greet')
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name}", "age": age}

# # serialtion


# class BookCreateModel(BaseModel):
#     title: str
#     author: str


# @app.post('/create_book')
# async def create_boook(book_data: BookCreateModel):
#     return {
#         "title": book_data.title,
#         "author": book_data.author
#     }


# @app.get('/get_headers', status_code=201)
# async def get_headers(
#     accept: str = Header(None),
#     content_type: str = Header(None),
#     user_agent: str = Header(None),
#     host: str = Header(None)
# ):
#     request_headers = {}

#     request_headers["Accept"] = accept
#     request_headers["Content-Type"] = content_type
#     request_headers["User_Agent"] = user_agent
#     request_headers["Host"] = host
#     return request_headers

from src.config import Config

print(Config.DATABASE_URL)
