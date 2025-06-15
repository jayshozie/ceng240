MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

<details>
    <summary>My Examples of Conditional and Repetitive Execution</summary>

## A Lot of Conditional Examples

### Equality Check of Two Numbers

This is a pretty basic and easy program. It should receive 2 numbers as input,
check whether they are equal to each other.

Regulations:
- If the result to the check is true, your program should print:
```markdown
{number1} is equal to {number2}.
```
- If the result to the check is false, your program should print:
```markdown
{number1} is not equal to {number2}.
```

Hints:
- You can use the function `eval(input())` to get input from the user.
- You can assume the user will only provide valid inputs, meaning the user will
only provide numerical values. You don't need to error handle the case where
the user provides a string, or a list, etc.

<details>
    <summary>Solution</summary>

```python
num1 = eval(input("Please enter the first number: "))
num2 = eval(input("Please enter the second number: "))

if num1 == num2:
    print(f"{num1} is equal to {num2}.")
else:
    print(f"{num1} is not equal to {num2}.")
```
</details>

### Even or Odd Check

In this program, we are expected to receive a numerical input (it can be an
int, or float number), check it's even or odd, and provide that information
with the user.

Regulations:
- If the given nummber is even, the program should print:
```markdown
{num} is even.
```
- If the given nummber is odd, the program should print:
```markdown
{num} is odd.
```
- If the given nummber is neither even nor odd, the program should print:
```markdown
{num} is neither even nor odd.
```

Hints:
- You can use the function `eval(input())` to get input from the user.
- You should NOT assume the user will provide an integer. You should check that
if the given value is a whole number.
- You can assume the user will NOT enter a complex number, so no need to error
handle that.

<details>
    <summary>Solution</summary>

```python
num = eval(input("Please enter a numerical value: "))

if num % 2 == 0:
    print(f"{num} is even.")
elif num % 2 == 1:
    print(f"{num} is odd.")
else:
    print(f"{num} is neither even nor odd.")
```
This solution assumes the user will not provide a complex number, because the
`%` operator cannot be used between a complex and an int.

- Alternative Solution (w/ Error Handling)
```python
num = eval(input("Please enter a numerical value: "))

if isinstance(num, (int, float)):
    if num % 2 == 0:
        print(f"{num} is even.")
    elif num % 2 == 1:
        print(f"{num} is odd.")
    else:
        print(f"{num} is neither even nor odd")
else:
    print(f"{num} is neither even nor odd")
```
This doesn't assume that. It explicitly checks whether the given number is an
int or float, if it isn't it automatically sends it to the else case, which
prints it's neither even nor odd; otherwise it checks whether it's divisible
by two. If it is divisible, it prints it's even, if the remainder is 1 however,
then it prints it's odd. If the provided number is a decimal number such as
`34.2`, then it prints it's neither even nor odd.
</details>

### Voting Eligibility

In this program, we are expected to receive a numerical input, which is the
age of a person, and check whether that person is eligible to vote or not.

Regulations:
- You can assume the user will provide a normal human age, meaning it won't be
less than 0.
- You can assume the user will provide an int, meaning they won't input a
decimal number like `18.5`. If the user inputs the number `18` that means they
have been on this earth longer than 18 years, meaning that they are a legal
adult.

Hints:
- You can use `eval(input())` to get input from the user.

<details>
    <summary>Solution</summary>

```python
age = eval(input("Please enter your age: "))

if age >= 18:
    print(f"You are {age} years old. You're a legal adult.")
else:
    print(f"You are {age} years old. You're not a legal adult.")
```
This is the most basic solution to the question, and it is correct according to
the regulations. It doesn't check whether the given input is a number that can
be compared with an integer, but we're not asked to do that.

- Alternative Solution (w/ Error Handling)
```python
age = eval(input("Please enter your age: "))

if isinstance(age, (int, float)):
    if age >= 18:
        print(f"You are {age} years old. You're a legal adult.")
    else:
        print(f"You are {age} years old. You're not a legal adult.")
else:
    print(f"You've entered {age} as your age. Please enter a valid number.")
```
In this solution, we check whether the given input is an int or float, if it
isn't then we automatically say that the given age is not valid. You can also
put this block of code into a while loop and let it loop until the user
provides a valid age. It would be a good exercise.
</details>

### Coordinate Quadrant Identification

In this program, the user will provide us a tuple of numbers, and we will
return in which quadrant of a Cartesian coordinate system it should be located.

Regulations:
- You should print with the following format:
```markdown
{point} is located in quadrant I.
{point} is located in quadrant II.
{point} is located in quadrant III.
{point} is located in quadrant IV.
```
- If the user provides a point which lies on one of the axes, then the program
should decide which two quadrants its in between and print with the following
format:
```markdown
{point} is located between quadrant I and IV.
{point} is located between quadrant I and II.
{point} is located between quadrant II and III.
{point} is located between quadrant III and IV.
```
- You can assume the user will provide the coordinate in the correct format
using tuples.

Hint:
- You can use `eval(input())` to get input from the user.
- You can check individual coordinates by using their index. For example,
```python
# If the tuple is given as
eg_tuple = (1, 1)
# You can access the first item with
eg_tuple[0]
```
- I highly recommend you to check the example I/O section.

<details>
    <summary>Example I/O</summary>

```markdown
Input:
(10, 24)
Output:
(10, 24) is in quadrant I.

Input:
(0, 0)
Output:
(0, 0) is the origin.

Input:
(0, 1)
Output:
(0, 1) is between quadrants I and II.
```
</details>


<details>
    <summary>Solution</summary>

```python
coordinate = eval(input("Please enter a valid coordinate: "))

if (coordinate[0] == 0 or
    coordinate[1] == 0):

    if coordinate[0] == 0 and coordinate[1] > 0:
        print(f"{coordinate} is between quadrant I and II.")
    elif coordinate[0] == 0 and coordinate[1] < 0:
        print(f"{coordinate} is between quadrant III and IV.")
    elif coordinate[0] > 0 and coordinate[1] == 0:
        print(f"{coordinate} is between quadrant I and IV.")
    elif coordinate[0] < 0 and coordinate[1] == 0:
        print(f"{coordinate} is between quadrant II and III.")
    elif coordinate[0] == 0 and coordinate[1] == 0:
        print(f"{coordinate} is the origin")

else:
    if coordinate[0] > 0 and coordinate[1] > 0:
        print(f"{coordinate} is in quadrant I.")
    elif coordinate[0] < 0 and coordinate[1] > 0:
        print(f"{coordinate} is in quadrant II.")
    elif coordinate[0] < 0 and coordinate[1] < 0:
        print(f"{coordinate} is in quadrant III.")
    elif coordinate[0] > 0 and coordinate[1] < 0:
        print(f"{coordinate} is in quadrant IV.")
```

</details>


### Character Type Classification

-------------------------------------------------------------------------------

## A Lot of For Loop Examples

### Print First 10 Natural Numbers

### Sum of First 10 Natural Numbers

### Display n Terms of Natural Numbers and Their Sum

### Sum and Average of 10 Numbers as Input

### Display Cubes of Numbers Up to an Integer

### Factorial Calculation

-------------------------------------------------------------------------------

## A Lot of While Loop Examples

### Print Numbers Using a While Loop

### Sum of Positive Integers Until 0

### Sum Until Negative Number

### Random Number Guessing Game

### Simple Password Validation


</details>


All example questions are taken from
[W3Resource.com](https://www.w3resource.com/c-programming-exercise).
Some of them are changed a little bit, because I felt like they would be better
examples of the real world coding practices.
