import asyncio
from database import get_connection

async def main():
    async with get_connection() as conn:
            await conn.execute(
    """
    CREATE TABLE IF NOT EXIST USERS(
        ID SERIAL PRIMARY KEY,
        USERNAME VARCHAR(50) NOT NULL,
        EMAIL VARCHAR(250) NOT NULL UNIQUE,
        PASSWORD VARCHAR(200) NOT NULL,
    );
    CREATE TABLE IF NOT EXIST BOOKS(
        ID SERIAL PRIMARY KEY,
        TITLE VARCHAR(150) NOT NULL,
        DESCRIPTION VARCHAR(250) ,
        PRICE INT,
        CREATED_AT DATE DEFAULT CURRENT DATE,
        USER_ID INT REFERENCES USER(ID) ON DELETE CASCADE
    );
    """
            )
            print('OK 200')

asyncio.run(main())