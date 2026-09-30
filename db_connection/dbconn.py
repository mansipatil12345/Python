import sqlite3;

def db_conn():
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    return conn,cursor




