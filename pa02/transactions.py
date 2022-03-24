import sqlite3


def data_to_dict(data):
    return {'item #': data[0], 'amount': data[1], 'category': data[2], 'date': data[3], 'desc': data[4]}


def data_to_list(data):
    return [data_to_dict(row) for row in data]


class Transaction:

    def __init__(self, filename):
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS transactions")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS transactions (item int, amount int, category text, date text, description text)")
        con.commit()
        con.close()
        self.db = filename

    def select_all(self):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("SELECT * from transactions")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return data_to_list(rows)

    def delete(self, item):
        """ delete a transaction from the transactions table with a given rowid
        """
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                           WHERE item=(?);
        ''', item)
        con.commit()
        con.close()

    def add(self, item):
        """ add a transaction to the transactions table.
            this returns the rowid of the inserted element
        """
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",
                    (item['item'], item['amount'], item['category'], item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def summary_by_date(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT item, sum(amount), category, date as n, description from transactions group by date order by n")
        results = cur.fetchall()
        con.commit()
        con.close()
        return results

    def summary_by_month(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT item, sum(amount), category, date as n, description from transactions group by ('%M', date) order by n")
        results = cur.fetchall()
        con.commit()
        con.close()
        return results

    def summary_by_year(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT item, sum(amount), category, date as n, description from transactions group by ('%Y', date) order by n")
        results = cur.fetchall()
        con.commit()
        con.close()
        return results

    def summary_by_category(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute(
            "SELECT item, amount, category as n, date, description from transactions group by category order by n")
        results = cur.fetchall()
        con.commit()
        con.close()
        return results
