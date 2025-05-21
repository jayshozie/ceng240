# Week 5 Sample Question and Solution

"""
Question:

You are going to implement a function that processes a list of transactions.
The function definition and its parameters are as follows:

process_transactions(transactions, lower_bound, upper_bound)
* transactions : A list of floats
* lower_bound : A float
* upper_bound : A float

The function should return a list of three items:

1. The first item is a list containing the transactions lower than or equal to
    the lower_bound.

2. The second item is a list containing the transactions between the
    lower_bound and the upper_bound.

3. The third item is a list containing the transactions greater than or equal
    to the upper_bound.

Hint: Create separate empty lists for the three items and fill them up
    accordingly.

Sample I/O:
-----------

>>> process_transactions([27.5, 34.0, 73.3, 31.0, 66.0], 30.0, 40.0)
[[27.5], [34.0, 31.0], [73.3, 66.0]]

>> process_transactions([27.89, 34.44, 32.21, 31.26, 66.71] 20.0, 34.44)
[[], [27.89, 32.21, 31.26], [34.44. 66.71]]
"""

# Sample Solution


def process_transacions(transactions, lower_bound, upper_bound):
    low = []
    mid = []
    high = []

    for t in transactions:
        if t <= lower_bound:
            low.append(t)
        elif t >= upper_bound:
            high.append(t)
        else:
            mid.append(t)

    return [low, mid, high]


"""
I don't have much to say about this problem, since it's so easy, the answer
is pretty straightforward.
"""

# My Solution


def my_process_transactions(transactions, lower, upper):
    low, mid, hgh = [], [], []

    for transaction in transactions:
        if transaction <= lower:
            low.append(transaction)
        elif transaction >= upper:
            hgh.append(transaction)
        else:
            mid.append(transaction)

    return [low, mid, hgh]


# If you have any questions please don't hesitate to reach out.
# You can open up an issue, if you didn't understand something in this file.
