from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional


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
    id : Optional[int] = None
    title : str = Field(min_length=3)
    author : str = Field(min_length=1)
    description : str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)



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
    # print(type(new_book))
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
