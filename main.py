from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from queries import *


app = FastAPI(title="CRUD for users and books", description="API for CRUD", version="1.0.0")

class UserCreate(BaseModel):
    username:str
    email:str
    password:str


class UserResponse(BaseModel):
    id:int
    username:str
    email:str
    password:str
    

@app.get("/user/{user_id}", response_model=dict, summary="Your id")
async def get_user_endpoint(user_id:int):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Not Found")
    return user



app.post("/create_user/", response_model=UserResponse, summary="Create new user")
async def create_user_endpoint(user:UserCreate):
    user_id = await create_user(user.username, user.email, user.password    )
    return UserResponse(id = user_id, username= user.username, email = user.email, password=user.password)


@app.get("/list_user/", response_model=list[dict], summary="All Users")
async def list_users_endpoint():
    user = await get_user()
    return user


@app.put("/user/{user_id}", response_model=UserResponse, summary="update user")
async def update_user_endpoint(user_id:int, user:UserCreate):
    updated = await update_user(user_id, user.username, user.email, user.password)
    if not updated:
        return HTTPException(status_code=404, detail="user not found")
    return {"message":"user updated"}

@app.delete("/user/{user_id}", summary="delete user")
async def deleted_user_endpoint(user_id:int):
    deleted = await delete_user(user_id)
    if not deleted:
        return HTTPException(status_code=404, detail="USER NOT FOND")
    return {"message":"user deleted"}




class BookCreate(BaseModel):
    title:str
    description:str
    price:str
    user_id:int


class BookResponse(BaseModel):
    id:int
    title:str
    description:str
    price:str
    user_id:int



@app.get("/book/{book_id}", response_model=dict, summary="Your id for book")
async def get_book_endpoint(book_id:int):
    book = await get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")
    return book


app.post("/create_book/", response_model=UserResponse, summary="Create new book")
async def create_book_endpoint(book:BookCreate):
    book_id = await create_book(book.title,  book.description, book.price, book.user_id)
    return BookResponse(id=book_id, title=book.title, description=book.description, price=book.price, user_id=book.user_id)


@app.get("/list_book/", response_model=list[dict], summary="All Users")
async def list_books_endpoint():
    books = await get_books()
    return books



@app.put("/book_update/{book_id}", response_model=BookResponse, summary="update book")
async def update_book_endpoint(book_id:int, book:BookCreate):
    updated = await update_book(book_id, book.title, book.description, book.price, book.user_id)
    if not updated:
        return HTTPException(status_code=404, detail="book not found")
    return {"message":"book updated"}

@app.delete("/deleted_book/{book_id}", summary="delete book")
async def deleted_book_endpoint(book_id:int):
    deleted = await delete_book(book_id)
    if not deleted:
        return HTTPException(status_code=404, detail="BOOK NOT FOND")
    return {"message":"Book deleted"}