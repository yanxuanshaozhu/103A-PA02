import sqlite3

import pytest

from transactions import Transaction


@pytest.fixture
def setup_and_teardown(tmpdir):
    db = Transaction(tmpdir.join('test.db'))
    con = sqlite3.connect(tmpdir.join('test.db'))
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
    return db


@pytest.fixture
def setup_test_init(tmpdir):
    db = Transaction(tmpdir.join('test.db'))
    return db


def test_init(setup_test_init):
    path = setup_test_init.db
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute("PRAGMA table_info(transactions)")
    result = cur.fetchall()
    assert result == [(0, 'item', 'INT', 0, None, 0),
                      (1, 'amount', 'INT', 0, None, 0),
                      (2, 'category', 'TEXT', 0, None, 0),
                      (3, 'date', 'TEXT', 0, None, 0),
                      (4, 'description', 'TEXT', 0, None, 0)]


def test_select_all(setup_and_teardown):
    assert setup_and_teardown.select_all() == [
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
    setup_and_teardown.delete(3)
    assert setup_and_teardown.select_all() == [
        {'rowid': 1, 'item': 1, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is a test'},
        {'rowid': 2, 'item': 2, 'amount': 2, 'category': 'test1', 'date': '2022-03-21', 'desc': 'This is test 1'},
        {'rowid': 4, 'item': 4, 'amount': 3, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 3'},
        {'rowid': 5, 'item': 5, 'amount': 4, 'category': 'test2', 'date': '2022-03-22', 'desc': 'This is a test 4'},
        {'rowid': 6, 'item': 6, 'amount': 2, 'category': 'test2', 'date': '2022-04-24', 'desc': 'This is a test 5'},
        {'rowid': 7, 'item': 7, 'amount': 1, 'category': 'test2', 'date': '2022-04-25', 'desc': 'This is a test 6'},
        {'rowid': 8, 'item': 8, 'amount': 1, 'category': 'test2', 'date': '2023-02-22', 'desc': 'This is a test 7'},
    ]
    setup_and_teardown.delete(1)
    setup_and_teardown.delete(2)
    setup_and_teardown.delete(4)
    setup_and_teardown.delete(5)
    setup_and_teardown.delete(6)
    setup_and_teardown.delete(7)
    setup_and_teardown.delete(8)
    assert setup_and_teardown.select_all() == []


def test_add(setup_and_teardown):
    setup_and_teardown.add(
        {'item': 20, 'amount': 3, 'category': 'test_add', 'date': '2022-03-23', 'description': 'Testing add'})
    assert setup_and_teardown.select_all() == [
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
             'category': 'test',
             "date": '20220303',
             'description': 'testing'
             }
    trans0 = setup_and_teardown.select_all()
    rowid = setup_and_teardown.add(tran0)
    trans1 = setup_and_teardown.select_all()
    assert len(trans1) == len(trans0) + 1


@pytest.mark.delete1
def test_delete1(setup_and_teardown):
    """ add a transaction to db, delete it, and see that the size changes"""
    # first we get the initial table
    trans0 = setup_and_teardown.select_all()

    # then we add this transaction to the table and get the new list of rows
    tran = {'item': '1',
            'amount': '1',
            'category': 'test',
            "date": '20220303',
            'description': 'testing'
            }
    rowid = setup_and_teardown.add(tran)
    trans1 = setup_and_teardown.select_all()

    # now we delete the transaction and again get the new list of rows
    setup_and_teardown.delete(rowid)
    trans2 = setup_and_teardown.select_all()

    assert len(trans0) == len(trans2)
    assert len(trans2) == len(trans1) - 1


def test_summary_by_date(setup_and_teardown):
    assert setup_and_teardown.summary_by_date() == [(1, '2022-04-25'),
                                                    (1, '2023-02-22'),
                                                    (2, '2022-04-24'),
                                                    (7, '2022-03-21'),
                                                    (7, '2022-03-22')]


def test_summary_by_month(setup_and_teardown):
    assert setup_and_teardown.summary_by_month() == [(1, '02'),
                                                     (3, '04'),
                                                     (14, '03')]


def test_summary_by_year(setup_and_teardown):
    assert setup_and_teardown.summary_by_year() == [(1, '2023'),
                                                    (17, '2022')]


def test_summary_by_category(setup_and_teardown):
    assert setup_and_teardown.summary_by_category() == [(4, 'test1'),
                                                        (14, 'test2')]
