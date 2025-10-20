from database import get_connection
from fastapi import HTTPException
import asyncpg


async def create_user(username:str, email:str, password:str):
    async with get_connection() as conn:
        try:
            user_id = await conn.fetchval(
                "INSERT INTO USERS(USERNAME, EMAIL, PASSWORD) VALUES($1, $2, $3) RETURNING ID"
            , username, email, password)
            return user_id
        except asyncpg.UniqueViolationError:
            raise HTTPException(
                status_code=400, detail="Email mast be unique"
            )
        
    

async def get_user():
    async with get_connection() as conn:
        rows = await conn.fetch("SELECT * FROM USERS")
        return [dict(row) for row in rows]



async def get_user_by_id(id: int):
    async with get_connection() as conn:
        res = await conn.fetchrow("SELECT * FROM USERS WHERE ID = $1", id)
        if res:
            return dict(res)
        return ("does not exist")


async def update_user(id:str, username:str, email:str, password:str):
    async with get_connection() as conn:
        try:
            res = await conn.fetchrow(
                "UPDATE USERS SET USERNAME = $1, EMAIL = $2, PASSWORD = $3 WHERE ID = $4 RETURNING ID, USERNAME, EMAIL, PASSWORD"
            , username, email, password, id)
            if not res:
                raise HTTPException(status_code=404, detail="User not found")
            return dict(res)
        except asyncpg.UniqueViolationError:
            raise HTTPException(
                status_code=400, detail="Bad request"
            )


async def delete_user(id:int):
    async with get_connection() as conn:
        res = await conn.execute("DELETE FROM USERS WHERE ID = $1", id)
        if not res:
                raise HTTPException(status_code=404, detail="User not found")
        return {"message":"Successfully deleted."}



async def create_book(title:str, description:str, price:int, user_id:int):
    async with get_connection() as conn:
        try:
            book_id = await conn.fetchval(
                "INSERT INTO BOOKS(TITLE, DESCRIPTION, PRICE, USER_ID) VALUES($1, $2, $3, $4) RETURNING ID"
            , title,description, price, user_id)
            return book_id
        except asyncpg.UniqueViolationError:
            raise HTTPException(
                status_code=400, detail="Bad request"
            )


async def get_books():
    async with get_connection() as conn:
        rows = await conn.fetch("SELECT * FROM BOOKS")
        return [dict(row) for row in rows]



async def get_book_by_id(id: int):
    async with get_connection() as conn:
        res = await conn.fetchrow("SELECT * FROM BOOKS WHERE ID = $1", id)
        if res:
            return dict(res)
        return ("does not exist")


async def update_book(id:int, title:str, description:str, price:int, user_id:int):
    async with get_connection() as conn:
        try:
            res = await conn.fetchrow(
                "UPDATE BOOKS SET TITLE = $1, DESCRIPTION = $2, PRICE = $3, USER_ID = $4 WHERE ID = $5 RETURNING *"
            , title, description, price, user_id, id)
            if not res:
                raise HTTPException(status_code=404, detail="Book not found")
            return dict(res)
        except asyncpg.UniqueViolationError:
            raise HTTPException(
                status_code=400, detail="Bad request"
            )


async def delete_book(id:int):
    async with get_connection() as conn:
        res = await conn.execute("DELETE FROM BOOKS WHERE ID = $1", id)
        if not res:
                raise HTTPException(status_code=404, detail="Book not found")
        return {"message":"Successfully deleted."}

