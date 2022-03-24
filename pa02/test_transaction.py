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
    con.commit()
    con.close()
    yield
    os.remove('test.db')


@pytest.fixture
def setup_test_init():
    db = Transaction('test.db')
    yield
    os.remove('test.db')


def test_init(setup_test_init):
    assert 'test.db' in os.listdir()


def test_select_all(setup_and_teardown):
    global db
    assert db.select_all() == [
        {'item #': 1, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is a test'},
        {'item #': 2, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is test 1'},
        {'item #': 3, 'amount': 3, 'category': 'test2', 'date': '2022-03-21', 'desc': 'This is a test 2'},
        {'item #': 4, 'amount': 3, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 3'},
        {'item #': 5, 'amount': 4, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 4'}
    ]


def test_delete(setup_and_teardown):
    db.delete(3)
    assert db.select_all() == [
        {'item #': 1, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is a test'},
        {'item #': 2, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is test 1'},
        {'item #': 4, 'amount': 3, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 3'},
        {'item #': 5, 'amount': 4, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 4'}
    ]
    db.delete(1)
    db.delete(2)
    db.delete(4)
    db.delete(5)
    assert db.select_all() == []


def test_add(setup_and_teardown):
    db.add({'item #': 6, 'amount': 3, 'category': 'test_add', 'date': '2022-03-23', 'description': 'Testing add'})
    assert db.select_all() == [
        {'item #': 1, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is a test'},
        {'item #': 2, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is test 1'},
        {'item #': 3, 'amount': 3, 'category': 'test2', 'date': '2022-03-21', 'desc': 'This is a test 2'},
        {'item #': 4, 'amount': 3, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 3'},
        {'item #': 5, 'amount': 4, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 4'},
        {'item #': 6, 'amount': 3, 'category': 'test_add', 'date': '2022-03-23', 'desc': 'Testing add'}
    ]


def test_summary_by_date(setup_and_teardown):
    assert db.summary_by_date() == [
        {'amount': 7, 'date': '2022-03-21'},
        {'amount': 7, 'date': '2022-03-22'}
    ]
