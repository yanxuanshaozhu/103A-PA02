<h1 style="text-align:center;"> PA02</h1>

## About

---

In this team project, we make a finance tracker that allows users to keep track of their daily transactions. Users can interact with two sqlite tables that stores category information and transaction information interactively through command line prompt.



## Team Members

---

<ul>
    <li><a href="https://github.com/syoon0123">syoon0123</a></li>
    <li><a href="https://github.com/wwxiao09">wwxiao09</a></li>
    <li><a href="https://github.com/Zeng-Lecheng">Zeng-Lecheng</a></li>
    <li><a href="https://github.com/yanxuanshaozhu">yanxuanshaozhu</a></li>
</ul>


## Tools Used

---

<ul>
    <li> Visual Studio Code</li>
    <li> Python</li>
    <li> SQlite3</li>
    <li> Git</li>
    <li> GitHub</li>
</ul>


## Pylint Results

---

<ul>
    <li> category.py: 10.00/10</li>
    <li> tracker.py: 9.58/10</li>
    <li> transactions.py: 10.00/10</li>
    <li> test_category.py: 10.00/10</li>
    <li> test_transaction.py: 10.00/10</li>
</ul>

## Pytest Results

---

<ul>
    <li> test_category.py: all passed</li>
    <li> test_transaction.py: all passed</li>
</ul>

## Transcript

---

We have two versions of transcripts, readable and raw. The readable version is derived from the raw one by removing distracting control characters and mistypings.

### Readable version

```bash
Script started on 2022-03-24 21:25:19-04:00 [TERM="xterm-256color" TTY="/dev/tty1" COLUMNS="120" LINES="30"]
tiger@Tiger-T14: ~/103A-PA02/pa02$ pylint category.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

tiger@Tiger-T14: ~/103A-PA02/pa02$ pylint test_category.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

tiger@Tiger-T14: ~/103A-PA02/pa02$ pylint test_transaction.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

tiger@Tiger-T14: ~/103A-PA02/pa02$ pylint tracker.py 
************* Module tracker
tracker.py:60:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
tracker.py:58:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:58:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:58:0: R0915: Too many statements (57/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.58/10 (previous run: 9.58/10, +0.00)

tiger@Tiger-T14: ~/103A-PA02/pa02$ pylint transactions.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

tiger@Tiger-T14: ~/103A-PA02/pa02$ pytest
================================================= test session starts ==================================================
platform linux -- Python 3.8.10, pytest-7.1.1, pluggy-1.0.0
rootdir: /home/tiger/103A-PA02/pa02, configfile: pytest.ini
collecting ... 
collected 14 items                                                                                                     

test_category.py ....                                                                                            [ 28%]
test_transaction.py ..........                                                                                   [100%]

================================================== 14 passed in 0.37s ==================================================
tiger@Tiger-T14: ~/103A-PA02/pa02$ python3 tracker.py 

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

> 1
id  name       description                   
---------------------------------------------
> 2
category name: fruit  
category description: fruits are fruits
> 1
id  name       description                   
---------------------------------------------
1   fruit      fruits are fruits             
> 3
modifying category
rowid: 1
new category name: plants
new category description: plants are plants
> 1
id  name       description                   
---------------------------------------------
1   plants     plants are plants             
> 4


rowid      item       amount     category   date       description                   
--------------------------------------------------------------------
1          1          2         test1      2022-03-21 This is a test                
2          2          2         test1      2022-03-21 This is test 1                
3          3          3         test2      2022-03-21 This is a test 2              
4          4          3         test2      2022-03-22 This is a test 3              
5          5          4         test2      2022-03-22 This is a test 4              
6          6          2         test2      2022-04-24 This is a test 5              
7          7          1         test2      2022-04-25 This is a test 6              
8          8          1         test2      2023-02-22 This is a test 7              
> 5
adding transaction
item #: 20
amount: 3
category: test1
date yyyy-mm-dd:2023-02-23
description: This is test 20
> 4


rowid      item       amount     category   date       description                   
--------------------------------------------------------------------
1          1          2         test1      2022-03-21 This is a test                
2          2          2         test1      2022-03-21 This is test 1                
3          3          3         test2      2022-03-21 This is a test 2              
4          4          3         test2      2022-03-22 This is a test 3              
5          5          4         test2      2022-03-22 This is a test 4              
6          6          2         test2      2022-04-24 This is a test 5              
7          7          1         test2      2022-04-25 This is a test 6              
8          8          1         test2      2023-02-22 This is a test 7              
9          20         3         test1      2023-02-23 This is test 20               
> 6
here are the current transactions: 


rowid      item       amount     category   date       description                   
--------------------------------------------------------------------
1          1          2         test1      2022-03-21 This is a test                
2          2          2         test1      2022-03-21 This is test 1                
3          3          3         test2      2022-03-21 This is a test 2              
4          4          3         test2      2022-03-22 This is a test 3              
5          5          4         test2      2022-03-22 This is a test 4              
6          6          2         test2      2022-04-24 This is a test 5              
7          7          1         test2      2022-04-25 This is a test 6              
8          8          1         test2      2023-02-22 This is a test 7              
9          20         3         test1      2023-02-23 This is test 20               
which transaction would you like to delete? 9
> 4


rowid      item       amount     category   date       description                   
--------------------------------------------------------------------
1          1          2         test1      2022-03-21 This is a test                
2          2          2         test1      2022-03-21 This is test 1                
3          3          3         test2      2022-03-21 This is a test 2              
4          4          3         test2      2022-03-22 This is a test 3              
5          5          4         test2      2022-03-22 This is a test 4              
6          6          2         test2      2022-04-24 This is a test 5              
7          7          1         test2      2022-04-25 This is a test 6              
8          8          1         test2      2023-02-22 This is a test 7              
> 7
Summary of transactions by date:


total      date      
--------------------
1          2022-04-25
1          2023-02-22
2          2022-04-24
7          2022-03-21
7          2022-03-22
> 8
Summary of transactions by month:


total      month     
--------------------
1          02        
3          04        
14         03        
> 9
Summary of transactions by year:


total      year      
--------------------
1          2023      
17         2022      
> 10
Summary of transactions by category:


total      category  
--------------------
4          test1     
14         test2     
> 11
Here is the menu:

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

> 0
bye
tiger@Tiger-T14: ~/103A-PA02/pa02$ exit
exit

Script done on 2022-03-24 21:28:08-04:00 [COMMAND_EXIT_CODE="0"]
```

### Raw version

```bash
Script started on 2022-03-24 21:25:19-04:00 [TERM="xterm-256color" TTY="/dev/tty1" COLUMNS="120" LINES="30"]
]0;tiger@Tiger-T14: ~/103A-PA02/pa02[01;32mtiger@Tiger-T14[00m:[01;34m~/103A-PA02/pa02[00m$ pylint category.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

[0m]0;tiger@Tiger-T14: ~/103A-PA02/pa02[01;32mtiger@Tiger-T14[00m:[01;34m~/103A-PA02/pa02[00m$ pylint test_category.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

[0m]0;tiger@Tiger-T14: ~/103A-PA02/pa02[01;32mtiger@Tiger-T14[00m:[01;34m~/103A-PA02/pa02[00m$ pylint test_transaction.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

[0m]0;tiger@Tiger-T14: ~/103A-PA02/pa02[01;32mtiger@Tiger-T14[00m:[01;34m~/103A-PA02/pa02[00m$ pylint tracker.py 
************* Module tracker
tracker.py:60:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
tracker.py:58:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:58:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:58:0: R0915: Too many statements (57/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.58/10 (previous run: 9.58/10, +0.00)

[0m]0;tiger@Tiger-T14: ~/103A-PA02/pa02[01;32mtiger@Tiger-T14[00m:[01;34m~/103A-PA02/pa02[00m$ pylint transactions.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

[0m]0;tiger@Tiger-T14: ~/103A-PA02/pa02[01;32mtiger@Tiger-T14[00m:[01;34m~/103A-PA02/pa02[00m$ pytest
[1m================================================= test session starts ==================================================[0m
platform linux -- Python 3.8.10, pytest-7.1.1, pluggy-1.0.0
rootdir: /home/tiger/103A-PA02/pa02, configfile: pytest.ini
[1mcollecting ... [0m[1m
collected 14 items                                                                                                     [0m

test_category.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                                            [ 28%][0m
test_transaction.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                                   [100%][0m

[32m================================================== [32m[1m14 passed[0m[32m in 0.37s[0m[32m ==================================================[0m
]0;tiger@Tiger-T14: ~/103A-PA02/pa02[01;32mtiger@Tiger-T14[00m:[01;34m~/103A-PA02/pa02[00m$ python3 tracker.py 

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

> 1
id  name       description                   
---------------------------------------------
> 2
category name: app   fruit  
category description: fuit   ruits i are fruits
> 1
id  name       description                   
---------------------------------------------
1   fruit      fruits are fruits             
> 3
modifying category
rowid: 1
new category name: fruits      plants
new category description: plants are plants
> 1
id  name       description                   
---------------------------------------------
1   plants     plants are plants             
> 4


rowid      item       amount     category   date       description                   
--------------------------------------------------------------------
1          1          2         test1      2022-03-21 This is a test                
2          2          2         test1      2022-03-21 This is test 1                
3          3          3         test2      2022-03-21 This is a test 2              
4          4          3         test2      2022-03-22 This is a test 3              
5          5          4         test2      2022-03-22 This is a test 4              
6          6          2         test2      2022-04-24 This is a test 5              
7          7          1         test2      2022-04-25 This is a test 6              
8          8          1         test2      2023-02-22 This is a test 7              
> 5
adding transaction
item #: 20 21 test1 2023              
amount: 2 3
category: test1
date yyyy-mm-dd:2023-020 -23
description: This is test 02  20
> 4


rowid      item       amount     category   date       description                   
--------------------------------------------------------------------
1          1          2         test1      2022-03-21 This is a test                
2          2          2         test1      2022-03-21 This is test 1                
3          3          3         test2      2022-03-21 This is a test 2              
4          4          3         test2      2022-03-22 This is a test 3              
5          5          4         test2      2022-03-22 This is a test 4              
6          6          2         test2      2022-04-24 This is a test 5              
7          7          1         test2      2022-04-25 This is a test 6              
8          8          1         test2      2023-02-22 This is a test 7              
9          20         3         test1      2023-02-23 This is test 20               
> 6
here are the current transactions: 


rowid      item       amount     category   date       description                   
--------------------------------------------------------------------
1          1          2         test1      2022-03-21 This is a test                
2          2          2         test1      2022-03-21 This is test 1                
3          3          3         test2      2022-03-21 This is a test 2              
4          4          3         test2      2022-03-22 This is a test 3              
5          5          4         test2      2022-03-22 This is a test 4              
6          6          2         test2      2022-04-24 This is a test 5              
7          7          1         test2      2022-04-25 This is a test 6              
8          8          1         test2      2023-02-22 This is a test 7              
9          20         3         test1      2023-02-23 This is test 20               
which transaction would you like to delete? 9
> 4


rowid      item       amount     category   date       description                   
--------------------------------------------------------------------
1          1          2         test1      2022-03-21 This is a test                
2          2          2         test1      2022-03-21 This is test 1                
3          3          3         test2      2022-03-21 This is a test 2              
4          4          3         test2      2022-03-22 This is a test 3              
5          5          4         test2      2022-03-22 This is a test 4              
6          6          2         test2      2022-04-24 This is a test 5              
7          7          1         test2      2022-04-25 This is a test 6              
8          8          1         test2      2023-02-22 This is a test 7              
> 7
Summary of transactions by date:


total      date      
--------------------
1          2022-04-25
1          2023-02-22
2          2022-04-24
7          2022-03-21
7          2022-03-22
> 8
Summary of transactions by month:


total      month     
--------------------
1          02        
3          04        
14         03        
> 9
Summary of transactions by year:


total      year      
--------------------
1          2023      
17         2022      
> 10
Summary of transactions by category:


total      category  
--------------------
4          test1     
14         test2     
> 11
Here is the menu:

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

> 0
bye
]0;tiger@Tiger-T14: ~/103A-PA02/pa02[01;32mtiger@Tiger-T14[00m:[01;34m~/103A-PA02/pa02[00m$ exit
exit

Script done on 2022-03-24 21:28:08-04:00 [COMMAND_EXIT_CODE="0"]
```

## License

---

MIT License