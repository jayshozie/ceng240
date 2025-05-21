"""
So, here is the thing. I don't remember this question entirely.
How, you ask? Please check the ANNOUNCEMENT.md in the root of the repo.

The question was basically, here is this class, we have 2 methods in it.
When you create the object of the class, you provide it with things, then
in the second method it calculated something.
Then you were asked the code the last method called bill, which gave a list of
things.

I have no idea what the initialization arguments were, but basically it
calculated the total electricity consumption, total price before the discount,
total discount amount and the total price after the discount; and returned
these in a list.

The discount was 20% off on weekends.

If I remember correctly while initializing the object, you provided a
price/kW or something, and the discount was applied on weekends. If I remember
correctly you were allowed to assume the month started on a monday.

If you find an error in this solution, please open up and issue or send a PR.
"""

import random as rand


class MonthlyBill:
    def __init__(self, prc):
        self.consumption = [0.0] * 31
        self.price = prc

    def consume(self, day, amount):
        self.consumption[day] += amount

    def bill(self):
        total_cons = sum(self.consumption)
        weekends = [5, 6, 12, 13, 19, 20, 26, 27]
        before_disc = total_cons * self.price
        disc = 0

        for i in range(len(self.consumption)):
            if i in weekends:
                disc += self.consumption[i] * self.price * 0.2

        total = before_disc - disc

        ret_list = [total_cons, before_disc, disc, total]

        return ret_list


my_bill = MonthlyBill(10)

for v in range(0, 30):
    mnt = rand.randrange(20, 100, 1)
    my_bill.consume(v, mnt)

print(my_bill.consumption)
print(my_bill.bill())
