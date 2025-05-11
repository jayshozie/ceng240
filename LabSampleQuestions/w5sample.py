"""
Week 5 Sample Question and Solution

You are going to implement a function that processes a list of transactions.
The function definition and its parameters are as follows:

process_transactions(transactions, lower_bound, upper_bound)
    - transactions: A list of floats.
    - lower_bound: A float.
    - upper_bound: A float.

The function should return a list of three items:
    - The first item is a list containing the transactions that are less than
        or equal to the lower bound.
    - The second item is a list containing the transactions that are between
        the lower and upper bounds.
    - The third item is a list containing the transactions greater than or
        equal to the upper bound.

Hints & Regulations:
- Create separate empty lists for the three items and fill them up accordingly.


Example I/O:

>>> process_transactions([27.5, 34.0, 73.3, 31.0, 66.0], 30.0, 40.0)
([27.5], [34.0, 31.0], [73.3, 66.0])

>>> process_transactions([27.89, 34.44, 32.21, 31.26, 66.71], 20.0, 34.44)
[[], [27.89, 32.21, 31.26], [34.44, 66.71]]
"""


# Solution


def process_transactions(transactions, lower_bound, upper_bound):
    low = []
    mid = []
    high = []

    for transaction in transactions:
        if transaction <= lower_bound:
            low.append(transaction)
        elif transaction >= upper_bound:
            high.append(transaction)
        else:
            mid.append(transaction)

    return [low, mid, high]
