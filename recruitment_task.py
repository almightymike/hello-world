import pandas as pd

"""
On every stock exhange trading is realized by making buy and sell orders with given price and quantity.
For example buying 100 Apple shares with price 55.0. Those orders can be: added and/or removed.
Having the following orders:
1) Create an object that stores them,
2) Write a piece of code that in every step displays the sum of buy/sell orders with the best price.

Id      Order       Type        Price       Quantity
001     Buy         Add         20.0        100
002     Sell        Add         25.0        200
003     Buy         Add         23.0        50
004     Buy         Add         23.0        70
003     Buy         Remove      23.0        50
005     Sell        Add         28          100

"""

data = {'Id' : [1, 2, 3, 4, 3, 5],
        'Order': ['Buy', 'Sell', 'Buy', 'Buy', 'Buy', 'Sell'],
        'Type': ['Add', 'Add', 'Add', 'Add', 'Remove', 'Add'],
        'Price': [20.0, 25.0, 23.0, 23.0, 23.0, 28],
        'Quantity': [100, 200, 50, 70, 50, 100]}

df = pd.DataFrame(data)

print(df)
price = data['Price']
print("")

def check_sum():
    print("List of the best orders:")
    for row in df.itertuples():
        if row[4] == min(price) and row[2] == 'Buy':
            print(row)
        elif row[4] == max(price) and row[2] == 'Sell':
            print(row)

check_sum()

