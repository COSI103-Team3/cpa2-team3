Script started on Fri Mar 25 07:56:18 2022

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
[?1034hbash-3.2$ python3 tracker.py

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

> 4


item #     amount     category             date                 description
--------------------------------------------------------------------------------
1          50         dogs                 2000-08-25           hhhh      
> 5
amount: 700
category: rent
enter date (YYYY-MM-DD): 2022-03-01
description: paid rent 
> 4


item #     amount     category             date                 description
--------------------------------------------------------------------------------
1          50         dogs                 2000-08-25           hhhh      
2          700        rent                 2022-03-01           paid rent 
> 6
item #: 1
> 4


item #     amount     category             date                 description
--------------------------------------------------------------------------------
2          700        rent                 2022-03-01           paid rent 
> 5
amount: 20
category: food
enter date (YYYY-MM-DD): 2022-02-28
description: got chinese takeout
> 4


item #     amount     category             date                 description
--------------------------------------------------------------------------------
2          700        rent                 2022-03-01           paid rent 
3          20         food                 2022-02-28           got chinese takeout
> 7
date: 2022-02-28


item #     amount     category             date                 description
--------------------------------------------------------------------------------
3          20         food                 2022-02-28           got chinese takeout
> 8
month: 03


item #     amount     category             date                 description
--------------------------------------------------------------------------------
2          700        rent                 2022-03-01           paid rent 
> 9
year: 2021
no items to print
> 9
year: 2022


item #     amount     category             date                 description
--------------------------------------------------------------------------------
2          700        rent                 2022-03-01           paid rent 
3          20         food                 2022-02-28           got chinese takeout
> 10
category: food


item #     amount     category             date                 description
--------------------------------------------------------------------------------
3          20         food                 2022-02-28           got chinese takeout
> 11

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
bash-3.2$ 