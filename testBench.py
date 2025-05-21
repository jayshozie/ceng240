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
