import sqlite3
import csv
class Transaction:
    def __init__(self, filename):
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS transactions")
        cur.execute("CREATE TABLE IF NOT EXISTS transactions (item_id int, amount int, category text, date text, description text)")
        con.commit()
        con.close()
