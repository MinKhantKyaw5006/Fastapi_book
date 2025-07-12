from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

version = 'v1'


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 App is starting")
    yield
    print("🛑 App is shutting down")

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
    lifespan=lifespan
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])

# http://127.0.0.1:8000/api//v1/book
