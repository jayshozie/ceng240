# Week 2 Sample Questions and Solutions

"""
Question 1:
In this lab, you are expected to calculate a customer's electricity bill based
on usage and the city in which the customer lives.

1. Firstly, you will read two pieces of information which are the electricity
    usage of the customer as kWh and the city name.
        * Electricity usage will be an int, which shows the total monthly usage
            of a customer.
        * City name will be a str, such as istanbul, ankara, izmir, mugla,
            corum, kirsehir (Be careful, English alphabet letters are used and
            all of the letters are lower case.

2. Secondly, you will calculate the base price of each kWh with respect to the
    total usage of the customer for the month.
        * Base Prices:
            - (0kWh <= total monthly usage <= 300 kWh) => price = 3TL/kWh
            - (300kWh <= total monthly usage <= 600 kWh) => price = 7TL/kWh
            - (600kWh <= total monthly usage) => price = 15TL/kWh

3. After finding the base price, you will show the effect of the city the
    customer lives in. If the customer lives in istanbul or ankara, the price
    per kWh will be more than the base price, otherwise, the price will be less
    than the base price:
        * If the customer lives in istanbul, then the price of each kWh will be
            3TL more than the base price.
                - For example, if the customer lives in istanbul, and the total
                    monthly usage of the customer is between 300 and 600 kWh,
                    then the price per kWh will be 10TL.
        * If the customer lives in ankara, then the price of each kWh will be
            2TL more than the base price.
                - For example, if the customer lives in ankara, and the total
                    monthly usage of the customer is between 300 and 600 kWh,
                    then the price per kWh will be 9TL.
        * If the customer lives in any other city, then the price per kWh will
            be 1TL less than the base price.

4. After finding the price per kWh for the customer, multiply it with the total
    usage of the customer to find the customer's electricity bill. Then print
    the found value on the screen.

Regulations & Hints:
--------------------
* Print the result as a float with 2 digits after the decimal ponit. You can
    use the following line to print your result in a proper format:
        print('%.2f' % your_result)

Sample I/O:
-----------

Input:
340
ankara

Output:
3060.00


Input:
299
konya

Output:
598.00


Input:
650
istanbul

Output:
11700.00


Input:
600
corum

Output:
8400.00
"""

# Sample Solution

usage = int(input())
city = input()

base_price = 0

if 0 <= usage < 300:
    base_price = 3
elif 300 <= usage < 600:
    base_price = 7
elif 600 <= usage:
    base_price = 15

if city == "istanbul":
    base_price +=3
elif city == "ankara":
    base_price += 2
else:
    base_price -= 1

total = base_price*usage
print("%.2f" % total)

"""
This solution is a wee bit better than the first week sample questions'
solutions; it still has room for improvement.
"""

# My Solution

# We need to get the usage and the city name from the user.
usage = int(input())
# I won't say something about converting the input to an integer, because
# in this case it would actually be a problem, since the user can just put
# 0.20 or something. The question explicitly tells us to use usage as integer.

city = str(input())
# I have no idea why didn't they do this, considering they did it in the
# previous line. This `str()` function will convert the input into a string.

# Sadly there is nothing we can do about these if-else statements.
if 0 <= usage < 300:
    base_price = 3
elif 300 <= usage < 600:
    base_price = 7
elif 600 <= usage:
    # Yes, technically, we could just say, `else`. Just to be on the safe side.
    # The user still can enter negative values, we didn't do anything about
    # that.
    base_price = 15
# The reason we're using elif statements instead of if statements is that,
# even though not in this case, it could be possible that the variable we're
# comparing be true for more than a single case. Using elif's instead of if's
# ensures that only one of these cases will be used. Not saying that there
# can't be two or more true comparisons, I'm just saying that we will know
# which will be the used one. The python shell, and almost every other
# programming language reads from top to bottom. If we were to change the
# second comparison to `0 <= usage < 300` the first one would be the
# base_price, since Python doesn't care about the rest of the clauses if
# any one of them is true and starts checking from the top.
# Thus, in the end, even if the first elif statement was true, the if the first
# is true, Python doesnt't care.


# Technically we could use dictionaries for this part, it would be cleaner.
# So I'll give both solutions.

# Dictionary Solution
"""
cities = {"istanbul": 3, "ankara": 2}
for c in cities:
    if c == city:
        base_price += city[c]
    else:
        base_price -= 1
"""
# This for loop will iterate through the dictionary, and if the city matches
# the input, adds its value to the base_price, if none does, then the
# base_price is decreased by 1.

# If-Else Clause Solution
if city == "istanbul":
    base_price += 3
elif city == "ankara":
    base_price += 2
else:
    base_price -= 1
# This checks one by one if the input matches a certain string. This is harder
# to manage in greater sets.

total = base_price * usage
print("%.2f" % total)


"""
Question 2:

You are working for a flower shop and your company decided to open an online
shop due to the Covid-19 pandemic. Your job is to implement a part of the
online shopping software. Specifically:

* You will read 3 numbers one by one. First one will encode the flower name,
    second one will encode the color of the flower(s), third one will encode
    the amount of flowers.

* Encoding of the flower name is as such:
    - If the most significant (leftmost) digit of the first number is 7, the
        requested flower is Rose.
    - If the most significant (leftmost) digit of the first number is 8, the
        requested flower is Tulip.
    - Otherwise the requested flower is Orchid.

* Encoding of the color is as such:
    - If the least significant (rightmost) digit of the second number is 0, 1
        2, or 3 the color is White.
    - If the least significant (rightmost) digit of the second number is 4, 5
        or 6 the color is Pink.
    - If the least significant (rightmost) digit of the second number is 7, 8
        or 9 the color is Red.

* There is no actualy encoding for the number of flowers. The third number will
    directly be the number of flowers ordered by the costumer; however, there
    are restrictions about flower amounts:
    - At most 100 Roses can be ordered at once. If more than 100 Roses are
        requested the order is Invalid.
    - At most 50 Tulips can be ordered at once. If more than 50 Tulips are
        requested the order is Invalid.
    - At most 30 Orchids can be ordered at once. If more than 30 Orchids are
        requested the order is Invalid.

* At the end, you will print the order information as such:
    - If the order is invalid, you will print "Invalid!".
    - If the order is valid, you will print the flower name, color and the
        amount without spaces. For example for 10 pink roses you will print
        "RosePink10". (Yes, flower name and the color will start with uppercase
        letters.)

Hint 1: You may need to convert the type of the input strings to integers for
    some operations, and some of them may needed to be converted back to
    string type at the end.

Hint 2: The most signnificant digit of 1234 is 1, the least significant digit
    of it is 4. Similarly, for 781, 7 is the most significant digit and 1 is
    the least significant.

Sample I/O:
-----------

Input:
7
4
90

Output:
RosePink90


Input:
85012012
23
40

Output:
TulipWhite40


Input:
13
301
40

Output:
Invalid!

Note: Last input is invalid since it requests 40 white orchids but the maximum
    permitted amount for orchids is 30.
"""

# Sample Solution

namenumber = input()
colornumber = input()
amountnumber = input()

# Determining color
if int(colornumber[-1]) in [0, 1, 2, 3]:
    color = 'White'
elif int(colornumber[-1]) in [4, 5, 6]:
    color = 'Pink'
else:
    color = 'Red'

# Order of these two blocks should be reversed lol.

# Determining name
if int(namenumber[0]) == 7:
    name = 'Rose'
elif int(namenumber[0]) == 8:
    name = 'Tulip'
else:
    name = 'Orchid'

# Printing the result
if name == 'Rose' and int(amountnumber) > 100:
    print("Invalid!")
elif name == 'Tulip' and int(amountnumber) > 50:
    print("Invalid!")
elif name == 'Orchid' and int(amountnumber) > 30:
    print("Invalid!")
else:
    print(name+color+amountnumber)


"""
That was a roller coaster. Yes, technically speaking, this is a correct
answer to the question; however, using this many if-else statements is a
nightmare incoming, but the question is weirdly specific, you don't have many
choices here. Di
"""

# I will use lists for this solution, yes you can use if statements, too.
# Just show me how you're going to manage it when there is 20 different flower
# names, 80 different colors, and 20 different maximum order amounts.

# My Solution

INVALID_ORDER_MSG = "Invalid!"
# You'll get why did I do this in a minute.

int_name = input()
int_color = input()
amount = int(input())

valid_Rose = [7]
valid_Tulip = [8]

valid_White = [0, 1, 2, 3]
valid_Pink = [4, 5, 6]

# Finding the name in their appropriate lists
if int(int_name[0]) in valid_Rose:
    name = 'Rose'
elif int(int_name[0]) in valid_Tulip:
    name = 'Tulip'
else:
    name = 'Orchid'

# Finding the color in their appropriate lists
if int(int_color[-1]) in valid_White:
    color = 'White'
elif int(int_color[-1]) in valid_Pink:
    color = 'Pink'
else:
    color = 'Red'


# Order validity check
is_valid = (name == 'Rose' and amount <= 100 or
            name == 'Tulip' and amount <= 50 or
            name == 'Orchid' and amount <= 30)
# Yes you could clean this. I think it's good enough for this case.

if not is_valid:
    print(INVALID_ORDER_MSG)
else:
    print(name + color + str(amount))


# If you have any questions please don't hesitate to reach out.
# You can open up an issue, if you didn't understand something in this file.
