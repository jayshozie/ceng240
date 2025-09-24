# MIT License
# Copyright (c) 2025 Emir Baha Yıldırım
# Please see the LICENSE file for more details.

"""
This is from another lab in week 6.

Basically, write a class that allows you to add items and prices, which
you don't pay the cheapest of 5. That is the only definition I got from
my friends, so I will add my own rules to this class, but it will be
harder than the official lab exam question so it's better in a way.

Easier Version
--------------

Assume the user will only add 5 items, and only 5. Your program should find the
cheapest item in it, and apply the buy 5 pay 4 discount. User will provide the
the item names and their prices in a single dictionary with the following
format:
{'coke': 2.5, 'chips': 4.25, 'wine': 89.99, 'charger': 14.90, 'butter': 15}

Harder Version
--------------
User can add more than 5 items. Your program should always find the the
cheapest items, and apply the buy 5 pay 4 discount. User will provide
the items and their prices in separate lists, so you need to keep track
which item costs how much. I'll give you an example for you to understand it
better:

Let's say a user added only 4 items, no discount applied, total calculated and
printed with the `total()` method.
Let's say a user added 5 items. Your program will find the cheapest item in it
and subtract its value from the total (you can just not add it to the total in
the first place).
Let's say a third user added 7 items. Your program will find only a single
cheapest item in it. Because they didn't buy enough items for a second
discount.
In this case if a user adds 10 items, the cheapest 2 items will be subject to
the discount.

Hints:
------


Usage:
------
>>> my_cart = Buy5Pay4()
>>> my_cart.addItems(['coke', 'chips', 'wine', 'charger', 'butter'],
[2.5, 4.25, 89.99, 14.90, 15])
>>> my_cart.total()
124.14
"""


class Buy5Pay4_Easy:
    def __init__(self):
        pass

    def addItems(self, items, prices):
        pass

    def total(self):
        pass


class Buy5Pay4_Hard:
    def __init__(self):
        pass

    def addItems(self, item_dict):
        pass

    def total(self):
        pass
