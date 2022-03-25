#! /opt/miniconda3/bin/python3
"""
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

"""

from category import Category
from transactions import Transaction

transactions = Transaction('tracker.db')
category = Category('tracker.db')

# here is the menu for the tracker app

MENU = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''


def process_choice(choice):
    """ process the user's choice"""
    if choice == '0':
        return
    elif choice == '1':
        cats = category.select_all()
        print_categories(cats)
    elif choice == '2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name': name, 'desc': desc}
        category.add(cat)
    elif choice == '3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name': name, 'desc': desc}
        category.update(rowid, cat)
    elif choice == '4':
        res = transactions.select_all()
        print_transactions(res)
    elif choice == '5':
        print('adding transaction')
        item = int(input('item #: '))
        amount = int(input('amount: '))
        cat = input('category: ')
        date = input("date yyyy-mm-dd:")
        desc = input('description: ')
        trans = {'item': item, 'amount': amount, 'category': cat, 'date': date, 'description': desc}
        transactions.add(trans)
    elif choice == '6':
        print('here are the current transactions: ')
        res = transactions.select_all()
        print_transactions(res)
        row = int(input('which transaction would you like to delete? '))
        transactions.delete(row)
    elif choice == '7':
        print("Summary of transactions by date:")
        res = transactions.summary_by_date()
        print_transaction_summary(res, 'date')
    elif choice == '8':
        print("Summary of transactions by month:")
        res = transactions.summary_by_month()
        print_transaction_summary(res, 'month')
    elif choice == '9':
        print("Summary of transactions by year:")
        res = transactions.summary_by_year()
        print_transaction_summary(res, 'year')
    elif choice == '10':
        print("Summary of transactions by category:")
        res = transactions.summary_by_category()
        print_transaction_summary(res, 'category')
    elif choice == '11':
        print("Here is the menu:")
        print(MENU)
    else:
        print("choice", choice, "not yet implemented")

    choice = input("> ")
    return choice


def toplevel():
    """ handle the user's choice """
    print(MENU)
    choice = input("> ")
    while choice != '0':
        choice = process_choice(choice)
    print('bye')


#
# here are some helper functions
#

def print_transactions(items):
    """ print the transactions """
    if len(items) == 0:
        print('no items to print')
        return
    print('\n')
    print(f"{'rowid':<10} {'item':<10} {'amount':<10} {'category':<10} {'date':<10} {'description':<30}")
    print('-' * 68)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10d %-10d %-10s %-10s %-30s"
              % (item['rowid'], item['item'], item['amount'], item['category'], item['date'], item['desc']))


def print_transaction_summary(items, criteria):
    """ print the transaction summarized by criteria """
    if len(items) == 0:
        print('no items to print')
        return
    print('\n')
    print(f"{'total':<10} {criteria:<10}")
    print('-' * 20)
    for item in items:
        print(f"{item['total']:<10} {item[criteria]:<10}")


def print_category(cat):
    """ print one category """
    print(f"{cat['rowid']:<3d} {cat['name']:<10} {cat['desc']:<30}")


def print_categories(cats):
    """ print the categories"""
    print(f"{'id':<3} {'name':<10} {'description':<30}")
    print('-' * 45)
    for cat in cats:
        print_category(cat)


# here is the main call!

toplevel()
