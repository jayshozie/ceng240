MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Examples of Conditional and Repetitive Execution

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
{number1} is not equal to {numebr2}.
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

### Coordinate Quadrant Identification

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

-------------------------------------------------------------------------------

All example questions are taken from
[W3Resource.com](https://www.w3resource.com/c-programming-exercise).
Some of them are changed a little bit, because I felt like they would be better
examples of the real world coding practices.
