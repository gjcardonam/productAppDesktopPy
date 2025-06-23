import sqlite3
import os

CLOUD_DB_PATH = "cloud_products.db"

def init_cloud_db():
    conn = sqlite3.connect(CLOUD_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def upsert_product(id, name, price):
    conn = sqlite3.connect(CLOUD_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (id, name, price)
        VALUES (?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET name=excluded.name, price=excluded.price
    """, (id, name, price))
    conn.commit()
    conn.close()
