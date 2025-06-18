import sqlite3
import os

def initialize_database():
    if not os.path.exists("db"):
        os.makedirs("db")

    conn = sqlite3.connect("db/app.db")
    cursor = conn.cursor()

    # Operator login table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS operators (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
    """)

    # Preload operators
    cursor.execute("INSERT OR IGNORE INTO operators VALUES (1, 'operator1', 'pass123')")
    cursor.execute("INSERT OR IGNORE INTO operators VALUES (2, 'operator2', 'pass456')")

    # Product master
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        barcode TEXT,
        sku TEXT,
        category TEXT,
        subcategory TEXT,
        name TEXT,
        description TEXT,
        tax REAL,
        price REAL,
        unit TEXT,
        image_path TEXT
    )
    """)

    # Goods receiving
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goods_receiving (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        supplier TEXT,
        quantity INTEGER,
        rate REAL,
        tax REAL,
        total REAL
    )
    """)

    # Sales
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        customer TEXT,
        quantity INTEGER,
        rate REAL,
        tax REAL,
        total REAL
    )
    """)

    conn.commit()
    conn.close()

# Run on startup
initialize_database()
