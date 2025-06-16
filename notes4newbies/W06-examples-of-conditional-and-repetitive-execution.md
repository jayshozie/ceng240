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

That's a lot of if statements. It looks messy and hard to maintain, I wonder if
we can make it better? :)
</details>

### Character Type Classification

In this program, we will receive a single character as input, and we will
determine whether it's a `digit`, `alphabet`, or a `special character`. The
checklist should be from the original ASCII printable characters, which you can
find it in the dropdown below.

<details>
    <summary>ASCII Printable Special Characters</summary>

|ASCII Number|Character|ASCII Number|Character|ASCII Number|Character|
|:----------:|:-------:|:----------:|:-------:|:----------:|:-------:|
|32|space|64|@ |96 |\`|
|33|  !  |65|A |97 | a|
|34|  "  |66|B |98 | b|
|35|  #  |67|C |99 | c|
|36|  $  |68|D |100| d|
|37|  %  |69|E |101| e|
|38|  &  |70|F |102| f|
|39|  '  |71|G |103| g|
|40|  (  |72|H |104| h|
|41|  )  |73|I |105| i|
|42|  \* |74|J |106| j|
|43|  +  |75|K |107| k|
|44|  ,  |76|L |108| l|
|45|  -  |77|M |109| m|
|46|  .  |78|N |110| n|
|47|  /  |79|O |111| o|
|48|  0  |80|P |112| p|
|49|  1  |81|Q |113| q|
|50|  2  |82|R |114| r|
|51|  3  |83|S |115| s|
|52|  4  |84|T |116| t|
|53|  5  |85|U |117| u|
|54|  6  |86|V |118| v|
|55|  7  |87|W |119| w|
|56|  8  |88|X |120| x|
|57|  9  |89|Y |121| y|
|58|  :  |90|Z |122| z|
|59|  ;  |91|[ |123| {|
|60|  <  |92|\ |124|\||
|61|  =  |93|] |125| }|
|62|  >  |94|^ |126| ~|
|63|  ?  |95|_ |   |  |

<details>
    <summary>Alphabeticals</summary>

```markdown
a b c d e f g h i j k l m n o p q r s t u v w x y z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```
</details>

<details>
    <summary>Digits</summary>

```markdown
0 1 2 3 4 5 6 7 8 9
```
</details>

The rest are considered special characters.
</details>

Regulations:
- Every character that is not in the above list should be treated as a
`special` character.
- You don't need to add a check for every single character, that's the point of
this exercise. Try to find a way that let's you check these characters without
adding a separate if-else check for every single one of them.
- If the input is longer than a single character, your program should let the
user know. (P.S.: You can check all characters if you want, but that's not
necessary.)
- The `space` (` `) character is also a special character.
- Please don't forget to check the example I/O section.

Hints:
- You can use `eval(input())` to get input from the user.

<details>
    <summary>Expected I/O</summary>

```markdown
Input:
@
Output:
'@' is a special character.

Input:
k
Output:
'k' is an alphabetical character.
```
</details>

<details>
    <summary>Solution</summary>

```python
alphabeticals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                 'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

input_char = str(input("Please enter a character: "))

if input_char in alphabeticals:
    print(f"{input_char} is an alphabetical character.")
elif input_char in digits:
    print(f"{input_char} is a digit character.")
else:
    print(f"{input_char} is a special character.")
```

First of all, this is NOT a good way of doing this. There are functions in
Python that allows you to check if a character is alphabetical, digit, or
special, but since you don't need to know them this would be their expected
code.

Alternative Solution (w/ Error Handling):
```python
lowercase_alphabeticals = [chr(i) for i in range(ord('a'), ord('z') + 1)]
uppercase_alphabeticals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
lowercase_alphabeticals.extend(uppercase_alphabeticals)

alphabeticals = lowercase_alphabeticals.copy()

digits = [chr(i) for i in range(ord('0'), ord('9') + 1)]

input_char = str(input("Please enter a character: "))

if input_char in alphabeticals:
    print(f"{input_char} is an alphabetical character.")
elif input_char in digits:
    print(f"{input_char} is a digit character.")
else:
    print(f"{input_char} is a special character.")
```
This is a way cleaner solution, but it requires a lot the `ord()` function and
list comprehension is a bit complex relative to just writing out all the
characters we need.
</details>

-------------------------------------------------------------------------------

## A Lot of For Loop Examples

### Print First 10 Positive Natural Numbers

In this program, we're expected to print out the first 10 natural numbers
without writing them explicitly. Since we're learning about for loops and not
while loops we're expected to use for loops.

Regulations:
- Your program should only print the natural numbers without explicitly
declaring what numbers you're printing in anywhere in your program.

Hints:
- `range(10)` gives you a range from `0` to `9`.
- You can use `print()` function to print out the numbers.

<details>
    <summary>Solution</summary>

```python
for i in range(10):
    print(i+1)
```
</details>

### Sum of First 10 Positive Natural Numbers

In this program, we're expected to print the sum of first 10 natural numbers
without calculating it ourself. Again, since we're learning about for loops,
don't calculate it and just print, use a for loop instead.

Regulations;
- Your program should only print the total, and nothing else.

Hints:
- `range(10)` gives you a range from `0` to `9`.
- You ccan use `print()` function to print your result.

<details>
    <summary>Solution</summary>

```python
total = 0
for i in range(10):
    print(f"DEBUG: i = {i} | total = {total}")
    total += i+1
```

</details>

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
