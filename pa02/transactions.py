import sqlite3


def data_to_dict(data):
    return {'rowid': int(data[0]), 'item': int(data[1]), 'amount': int(data[2]), 'category': data[3], 'date': data[4],
            'desc': data[5]}


def data_to_list(data):
    return [data_to_dict(row) for row in data]


class Transaction:

    def __init__(self, filename):
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS transactions (
                    item int, 
                    amount int, 
                    category text, 
                    date text, 
                    description text);
            """)
        con.commit()
        con.close()
        self.db = filename

    def select_all(self):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("""SELECT rowid, 
                              * 
                       FROM transactions;""")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return data_to_list(rows)

    def select_one(self, rowid):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("""SELECT rowid, 
                              * 
                       FROM transactions where rowid = (?);""", (rowid,))
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return data_to_list(rows)

    def delete(self, rowid):
        """ delete a transaction from the transaction table with a given rowid
        """
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("""
                    DELETE FROM transactions
                    WHERE  rowid = (?); 
        """, (rowid,))
        con.commit()
        con.close()

    def add(self, item):
        """ add a transaction to the transactions table.
            this returns the rowid of the inserted element
        """
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("""INSERT INTO transactions 
                       VALUES(?,?,?,?,?);""",
                    (item['item'], item['amount'], item['category'], item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def summary_by_date(self):
        con = sqlite3.connect(self.db)
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
        return results

    def summary_by_month(self):
        con = sqlite3.connect(self.db)
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
        return results

    def summary_by_year(self):
        con = sqlite3.connect(self.db)
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
        return results

    def summary_by_category(self):
        con = sqlite3.connect(self.db)
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
        return results
