# MIT License
# Copyright (c) 2025 Emir Baha Yıldırım
# Please see the LICENSE file for more details.

"""
This is from another lab in week 6.

Basically, write a class that allows you to add items and prices, which
you don't pay the cheapest of 5. That is the only definition I got from
my friends, so I will add my own rules to this class, but it will be
harder than the official lab exam question so it's better in a way.

User can add more than 5 items. Your program should always find the the
cheapest items, and apply the buy 5 pay 4 discount. User will provide
the items and their prices in separate lists, so you need to keep track
which item costs how much.

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


class Buy5Pay4:
    def __init__(self):
        pass

    def addItems(self, items, prices):
        pass

    def total(self):
        pass
