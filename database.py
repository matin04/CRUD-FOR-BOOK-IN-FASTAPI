import asyncpg
from contextlib import asynccontextmanager


DB_CONFIG = {
    "host":"localhost",
    "port":5432,
    "database":"Crud for book",
    "user":"postgres",
    "password":"55055904855"
}

@asynccontextmanager
async def get_connection():
    conn = await asyncpg.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        await conn.close()