import random

num = random.randint(1, 10)

print(
"|--------------------------------------|\n",
"|------------Guess My Number-----------|\n",
"|--------------------------------------|\n",
"| I have picked a number between 0 and |\n",
"| 10. Take a guess.                    |\n",
"|--------------------------------------|\n",
sep='')

print(f"DEBUG : num = {num}")

while True:
    guess = input("My Guess: ")
    try:
        guess = int(guess)
    except ValueError:
        print(f"You've entered a non-int value ({guess}). Please try again.")
        continue

    if guess == num:
        print("Correct!")
        break
    else:
        print("Wrong guess! Try again.")
        continue
