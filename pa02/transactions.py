"""
transactions.py is an Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (rowid, item, amount, category, date, description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

"""

import sqlite3


def data_to_dict(data):
    """ this method converts a data tuple to dictionary format"""
    return {'rowid': int(data[0]), 'item': int(data[1]), 'amount': int(data[2]),
            'category': data[3], 'date': data[4], 'desc': data[5]}


def data_to_list(data):
    """ this method converts data from a list of tuples to a list of dictionaries"""
    return [data_to_dict(row) for row in data]


def summarize_by_date_formatter(data):
    """ this method converts data from a list of tuples to a list of dictionaries"""
    return [{'total': int(row[0]), 'date': row[1]} for row in data]


def summarize_by_month_formatter(data):
    """ this method converts data from a list of tuples to a list of dictionaries"""
    return [{'total': int(row[0]), 'month': row[1]} for row in data]


def summarize_by_year_formatter(data):
    """ this method converts data from a list of tuples to a list of dictionaries"""
    return [{'total': int(row[0]), 'year': row[1]} for row in data]


def summarize_by_category_formatter(data):
    """ this method converts data from a list of tuples to a list of dictionaries"""
    return [{'total': int(row[0]), 'category': row[1]} for row in data]


class Transaction:
    """ Transaction represents a table of transactions"""

    def __init__(self, filename):
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                    item INT, 
                    amount INT, 
                    category TEXT, 
                    date TEXT, 
                    description TEXT);
            """)
        con.commit()
        con.close()
        self.database = filename

    def select_all(self):
        """ return all transactions as a list of dictionary"""
        conn = sqlite3.connect(self.database)
        cur = conn.cursor()
        cur.execute("""SELECT rowid, * FROM transactions;""")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return data_to_list(rows)

    def select_one(self, rowid):
        """ return a transaction with a specified rowid """
        conn = sqlite3.connect(self.database)
        cur = conn.cursor()
        cur.execute("""SELECT rowid, * FROM transactions where rowid = (?);""", (rowid,))
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return data_to_list(rows)

    def delete(self, rowid):
        """ delete a transaction from the transaction table with a given rowid
        """
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("""
                    DELETE FROM transactions
                    WHERE  rowid = (?); 
        """, (rowid,))
        con.commit()
        con.close()

    def add(self, item):
        """ add a transaction to the transactions table
            and returns the rowid of the inserted element
        """
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("""INSERT INTO transactions VALUES(?,?,?,?,?);""",
                    (item['item'], item['amount'], item['category'],
                     item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def summary_by_date(self):
        """ this method calculates the total transaction for different dates"""
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("""
                    SELECT Sum(amount) AS total,
                           date
                    FROM   transactions
                    GROUP  BY date
                    ORDER  BY total;
        """)
        results = cur.fetchall()
        con.commit()
        con.close()
        return summarize_by_date_formatter(results)

    def summary_by_month(self):
        """ this method calculates the total transaction for different months"""
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("""
                    SELECT Sum(amount)          AS total,
                           Strftime('%m', date) AS month
                    FROM   transactions
                    GROUP  BY Strftime('%m', date)
                    ORDER  BY total; 
        """)
        results = cur.fetchall()
        con.commit()
        con.close()
        return summarize_by_month_formatter(results)

    def summary_by_year(self):
        """ this method calculates the total transaction for different years"""
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("""
                    SELECT Sum(amount)          AS total,
                           Strftime('%Y', date) AS year
                    FROM   transactions
                    GROUP  BY Strftime('%Y', date)
                    ORDER  BY total; 
        """)
        results = cur.fetchall()
        con.commit()
        con.close()
        return summarize_by_year_formatter(results)

    def summary_by_category(self):
        """ this method calculates the total transaction for different categories"""
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("""
            SELECT Sum(amount) AS total,
                   category
            FROM   transactions
            GROUP  BY category
            ORDER  BY total; 
        """)
        results = cur.fetchall()
        con.commit()
        con.close()
        return summarize_by_category_formatter(results)
