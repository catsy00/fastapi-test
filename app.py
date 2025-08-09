# app.py

import os
import mysql.connector
from fastapi import FastAPI, HTTPException

app = FastAPI()

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME")
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "Happy test"}


@app.get("/book/{book_name}")
async def read_book(book_name: str):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor(dictionary=True)
    query = "SELECT id, name, author FROM book WHERE name = %s"

    try:
        cursor.execute(query, (book_name,))
        book = cursor.fetchone()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database query failed: {err}")
    finally:
        cursor.close()
        conn.close()