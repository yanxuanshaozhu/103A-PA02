import os
import sqlite3

import pytest

from transactions import Transaction

db: Transaction


@pytest.fixture
def setup_and_teardown():
    global db
    db = Transaction('test.db')
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS transactions (item int, amount int, category text, date text, description text)")
    cur.execute("INSERT into transactions (item, amount, category, date, description) values "
                "(1, 2, 'test1', '2022-03-21', 'This is a test')")
    cur.execute("INSERT into transactions (item, amount, category, date, description) values "
                "(2, 2, 'test1', '2022-03-21', 'This is test 1')")
    cur.execute("INSERT into transactions (item, amount, category, date, description) values "
                "(3, 3, 'test2', '2022-03-21', 'This is a test 2')")
    cur.execute("INSERT into transactions (item, amount, category, date, description) values "
                "(4, 3, 'test2', '2022-03-22', 'This is a test 3')")
    cur.execute("INSERT into transactions (item, amount, category, date, description) values "
                "(5, 4, 'test2', '2022-03-22', 'This is a test 4')")
    cur.execute("INSERT into transactions (item, amount, category, date, description) values "
                "(6, 2, 'test2', '2022-04-24', 'This is a test 5')")
    cur.execute("INSERT into transactions (item, amount, category, date, description) values "
                "(7, 1, 'test2', '2022-04-25', 'This is a test 6')")
    cur.execute("INSERT into transactions (item, amount, category, date, description) values "
                "(8, 1, 'test2', '2023-02-22', 'This is a test 7')")

    con.commit()
    con.close()
    yield
    os.remove('test.db')


@pytest.fixture
def setup_test_init():
    global db
    db = Transaction('test.db')
    yield
    os.remove('test.db')


def test_init(setup_test_init):
    assert 'test.db' in os.listdir()


def test_select_all(setup_and_teardown):
    global db
    assert db.select_all() == [
        {'rowid': 1, 'item': 1, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is a test'},
        {'rowid': 2, 'item': 2, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is test 1'},
        {'rowid': 3, 'item': 3, 'amount': 3, 'category': 'test2', 'date': '2022-03-21', 'desc': 'This is a test 2'},
        {'rowid': 4, 'item': 4, 'amount': 3, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 3'},
        {'rowid': 5, 'item': 5, 'amount': 4, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 4'},
        {'rowid': 6, 'item': 6, 'amount': 2, 'category': 'test2', 'date': '2022-04-24', 'desc': 'This is a test 5'},
        {'rowid': 7, 'item': 7, 'amount': 1, 'category': 'test2', 'date': '2022-04-25', 'desc': 'This is a test 6'},
        {'rowid': 8, 'item': 8, 'amount': 1, 'category': 'test2', 'date': '2023-02-22', 'desc': 'This is a test 7'}
    ]


def test_delete(setup_and_teardown):
    db.delete(3)
    assert db.select_all() == [
        {'rowid': 1, 'item': 1, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is a test'},
        {'rowid': 2, 'item': 2, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is test 1'},
        {'rowid': 4, 'item': 4, 'amount': 3, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 3'},
        {'rowid': 5, 'item': 5, 'amount': 4, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 4'},
        {'rowid': 6, 'item': 6, 'amount': 2, 'category': 'test2', 'date': '2022-04-24', 'desc': 'This is a test 5'},
        {'rowid': 7, 'item': 7, 'amount': 1, 'category': 'test2', 'date': '2022-04-25', 'desc': 'This is a test 6'},
        {'rowid': 8, 'item': 8, 'amount': 1, 'category': 'test2', 'date': '2023-02-22', 'desc': 'This is a test 7'},
    ]
    db.delete(1)
    db.delete(2)
    db.delete(4)
    db.delete(5)
    db.delete(6)
    db.delete(7)
    db.delete(8)
    assert db.select_all() == []


def test_add(setup_and_teardown):
    db.add({'item': 20, 'amount': 3, 'category': 'test_add', 'date': '2022-03-23', 'description': 'Testing add'})
    assert db.select_all() == [
        {'rowid': 1, 'item': 1, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is a test'},
        {'rowid': 2, 'item': 2, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is test 1'},
        {'rowid': 3, 'item': 3, 'amount': 3, 'category': 'test2', 'date': '2022-03-21', 'desc': 'This is a test 2'},
        {'rowid': 4, 'item': 4, 'amount': 3, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 3'},
        {'rowid': 5, 'item': 5, 'amount': 4, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 4'},
        {'rowid': 6, 'item': 6, 'amount': 2, 'category': 'test2', 'date': '2022-04-24', 'desc': 'This is a test 5'},
        {'rowid': 7, 'item': 7, 'amount': 1, 'category': 'test2', 'date': '2022-04-25', 'desc': 'This is a test 6'},
        {'rowid': 8, 'item': 8, 'amount': 1, 'category': 'test2', 'date': '2023-02-22', 'desc': 'This is a test 7'},
        {'rowid': 9, 'item': 20, 'amount': 3, 'category': 'test_add', 'date': '2022-03-23', 'desc': 'Testing add'}
    ]


@pytest.mark.add1
def test_add1(setup_and_teardown):
    """ add a transaction to db, then select it, then delete it"""

    tran0 = {'item': '1',
             'amount': '1',
             'category':'test',
             "date":'20220303',
             'description':'testing'
             }
    trans0 = db.select_all()
    rowid = db.add(tran0)
    trans1 = db.select_all()
    assert len(trans1) == len(trans0) + 1

  



@pytest.mark.delete1
def test_delete1(setup_and_teardown):
    """ add a transaction to db, delete it, and see that the size changes"""
    # first we get the initial table
    trans0 = db.select_all()

    # then we add this transaction to the table and get the new list of rows
    tran = {'item': '1',
             'amount': '1',
             'category':'test',
             "date":'20220303',
             'description':'testing'
             }
    rowid = db.add(tran)
    trans1 = db.select_all()

    # now we delete the transaction and again get the new list of rows
    db.delete(rowid)
    trans2 = db.select_all()

    assert len(trans0) == len(trans2)
    assert len(trans2) == len(trans1) - 1


def test_summary_by_date(setup_and_teardown):
    assert db.summary_by_date() == [(1, '2022-04-25'),
                                    (1, '2023-02-22'),
                                    (2, '2022-04-24'),
                                    (7, '2022-03-21'),
                                    (7, '2022-03-22')]


def test_summary_by_month(setup_and_teardown):
    assert db.summary_by_month() == [(1, '02'),
                                     (3, '04'),
                                     (14, '03')]

def test_summary_by_year(setup_and_teardown):
    assert db.summary_by_year() == [(1, '2023'),
                                    (17, '2022')]

def test_summary_by_category(setup_and_teardown):
    assert db.summary_by_category() == [(4, 'test1'),
                                        (14, 'test2')]
