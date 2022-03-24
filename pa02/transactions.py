import sqlite3
import csv


def data_to_dict(data):
    return {'item #':data[0], 'amount':data[1], 'category':data[2], 'date': data[3], 'desc':data[4]}

def data_to_list(data):
    return [data_to_dict(row) for row in data]

class Transaction:


    def __init__(self, filename):
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS transactions")
        cur.execute("CREATE TABLE IF NOT EXISTS transactions (item int, amount int, category text, date text, description text)")
        con.commit()
        con.close()
        self.db = filename

    def select_all(self):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("select * from transactions")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return data_to_list(rows)

    def select_one(self, item):
        """ return a category with a specified rowid """
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * from transactions where item=(?)", item)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return data_to_list(tuples[0])