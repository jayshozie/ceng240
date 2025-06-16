from getpass import getpass

password = None
mode = None

print(
"|-------------------------------------------|\n",
"|       Completely-Secure-Interface         |\n",
"|-------------------------------------------|\n",
"| Enter Mode : 1                            |\n",
"| Set Mode   : 0                            |\n",
"|-------------------------------------------|\n",
sep='')

while True:
    if password is None:
        print(
            "|-------------------------------------------|\n",
            "| Set a password to use this interface.     |\n",
            "|-------------------------------------------|",
        sep='')
        mode = 0
    else:
        print(
            "|-------------------------------------------|\n",
            "| Enter/Set :                               |\n",
            "|-------------------------------------------|",
        sep='')
        mode = input()

    try:
        mode = int(mode)
    except ValueError:
        print(
            f"|-------------------------------------------|\n",
            f"| You've entered an invalid input           |\n",
            f"| ('{mode}'), please try again.             |\n",
            f"|-------------------------------------------|",
        sep='')
        continue

    if mode == 1 and password is not None:
        print(
            "|-------------------------------------------|\n",
            "| Please enter your password:               |\n",
            "|-------------------------------------------|",
        sep='')
        pwd_try = getpass(" ")
        if pwd_try == password:
            print(
                "|-------------------------------------------|\n",
                "| Password is correct.                      |\n",
                "|-------------------------------------------|",
            sep='')
            break
        else:
            print(
                "|-------------------------------------------|\n",
                "| Incorrect password, please try again.     |\n",
                "|-------------------------------------------|",
            sep='')
            continue
    elif mode == 0:
        print(
            "|-------------------------------------------|\n",
            "| Please enter your new password:           |\n",
            "|-------------------------------------------|",
        sep='')
        password = getpass(" ")
        continue
