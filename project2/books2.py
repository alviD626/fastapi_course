from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()


class Book:
    id : int
    title : str
    author : str
    description : str
    rating: int


    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id : int
    title : str
    author : str
    description : str
    rating: int



BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book", 5),
    Book(2, "Be fast with FastAPI", "codingwithroby", "A great book", 5),
    Book(3, "Master Endpoints", "codingwithroby", "A awesome book", 5),
    Book(4, "HP1", "Author 1", "Description 1", 1),
    Book(5, "HP2", "Author 2", "Description 2", 2),
    Book(6, "HP3", "Author 3", "Description 3", 3),
]



@app.get("/books")
async def read_all_book():
    return BOOKS



@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(book_request)
