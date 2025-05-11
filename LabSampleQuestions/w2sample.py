"""
Week 2 Sample Questions and Solutions

Question 1:
In this lab, you are expected to calculate a customer's electricity bill based
on usage and the city where the customer lives.

1. Firstly, you will read two pieces of information which are the electricity
    usage of the customer as kWh and the city name.
        - Electricity usage will be an int, which shows the total monthly usage
            of a customer.
        - City name will be a string, such as "istanbul", "ankara", "izmir",
            "mugla", "corum", "kirsehir" (Be careful, English alphabet letters
            are used and all of the letters are lowercase.).
    2. Secondly, calculate the base price of each kWh with respect to the total
        usage of the customer for the month.
            - 0 kWh <= total monthly usage < 300 kWh, then the price of each
                kWh is 3 TL.
            - 300 kWh <= total monthly usage < 600 kWh, then the price of each
                kWh is 7 TL.
            - 600 kWh <= total monthly usage, then the price of each kWh is
                15 TL.
    3. After finding the base price, you should show the effect of the city the
        customer lives in. If the customer lives in Istanbul or Ankara, the
        price of each kWh will be more than the base price, otherwise, the
        price will be less than the base price.
            - If the customer lives in Istanbul, the price of each kWh will
                be 3 TL more than the base price.
                - For example, if the customer lives in Istanbul and the total
                    monthly usage is between 300 kWh and 600 kWh, the price of
                    each kWh is 10 TL.
            - If the customer lives in Ankara, the price of each kWh will be
                2 TL more than the base price.
                - For example, if the customer lives in Ankara and the total
                    monthly usage is between 300 kWh and 600 kWh, the price of
                    each kWh is 9 TL.
            - For the other cities, the nthe price of each kWh will be 1 TL
                less than the base price.
                - For example, if the customer lives in Antalya and the total
                    monthly usage is between 300 kWh and 600 kWh, the price of
                    each kWh is 6 TL.
    4. After finding the price of each kWh for the customer, multiply it with
        the total usage of the customer to find the customer's electricity
        bill. Then print the found value on the screen.

Regulations & Hints:
- Print the result as a float with 2 digits after the decimal point. You can
    use the following line to print your result in proper format.
        print('%.2f' % your_result)


Sample I/O:

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

# Solution

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
    base_price += 3
elif city == "ankara":
    base_price += 2
else:
    base_price -= 1

total_price = base_price * usage
print('%.2f' % total_price)


"""
Question 2:

You are working for a flower shop and your company decided to open an online
shop due to the Covid-19 pandemic. Your job is to implement a part of the
online shopping software. Specifically;

- You will read 3 numbers one by one. First one will encode the flower name,
    second one will encode the color of the flower(s), third one will encode
    the amount of flowers.
- Encoding for the flower name is as such:
    - if the most significant digit (the leftmost digit) of the number is 7,
        the requested flower is a Rose.
    - if the most significant digit (the leftmost digit) of the number is 8,
        the requested flower is a Tulip.
    - otherwise the requested flower is Orchid.

- Encoding for the color of the flower is as such:
    - If the least significant digit (the rightmost digit) of the second number
        is 0, 1, 2, or 3, the color is White.
    - If the least significant digit (the rightmost digit) of the second number
        is 4, 5, or 6, the color is Pink.
    - If the least significant digit (the rightmost digit) of the second number
        is 7, 8, or 9, the color is Red.
- There is no actual encoding forr the number of flowers. The third number will
    directly be the number of flowers ordered by the customer. However, there
    are such restrictions about the flower amounts:
        - At most 100 Roses ccan be ordered at noce. if more than 100 Roses are
            requested, the order is Invalid.
        - At most 50 Tulips can be ordered at once. if more than 50 Tulips are
            requested, the order is Invalid.
        - At most 30 Orchids can be ordered at once. if more than 30 Orchids
            are requested, the order is Invalid.
- At the end, you will print the order information as such:
    - If the order is invalid, you will print "Invalid!"
    - If the order is valid, you will print flower name, flower color, and the
        amount without spaces.

For example, for 10 pink roses you will print: "RosePink10". (Yes, flower name
    and color will start with uppercase letters.)

Regulations & Hints:
1. You may need to convert the type of the input strings to integers for some
    operations. (And some of them may needde to be converted back to string
    type at the end.)
2. The most significant digit of 1234 is 1, the least significant digit of 1234
    is 4. Similarly, for 781, 7 is the most significant digit and 1 is the
    least significant digit.


Example I/O:

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
"""

# Solution

namenumber = int(input())
colornumber = int(input())
amountnumber = int(input())

# Determining color

if colornumber[-1] in [0, 1, 2, 3]:
    color = "White"
elif colornumber[-1] in [4, 5, 6]:
    color = "Pink"
else:
    color = "Red"

# Determining name

if namenumber[0] == 7:
    name = "Rose"
elif namenumber[0] == 8:
    name = "Tulip"
else:
    name = "Orchid"

# Now it's time to print things:

if name == "Rose" and amountnumber > 100:
    print("Invalid!")
elif name == "Tulip" and amountnumber > 50:
    print("Invalid!")
elif name == "Orchid" and amountnumber > 30:
    print("Invalid!")
else:
    print(name + color + str(amountnumber))
