MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

In this markdown, we will start working on Python 3. If you didn't read 
[Week 0 - Preliminary](./W00-preliminary.md), you really should. I've explained
how/where/when to read documentations of programming languages in that. You
will really need it from now on.

-------------------------------------------------------------------------------

# Data Types in Python

As we've seen, a CPU cannot understand anything other than `integers` and
`floating-point numbers`, also we've seen ways to make a CPU 'understand
strings'. There are 2 main types of data you need to know about: Basic and
Container.

I will give you small assignments at the end of every markdown from now on. You
can find the answers to them in the [solutions](./solutions) directory. I
recommend you to work on them yourself until you are absolutely sure that you
cannot do them, and then looking at the answers. This way you will actually try
to learn how things work.

P.S: In Python, to assign a value (it can be anything) to a variable, you don't
need to specify which type it should be. Python does its best to understand
what you mean, and stores it itself.

## Basic Data Types

Basic data types store actual values. There are some quirks in Python that you
should know, but I will talk about those when it's time.

<details>
    <summary>Integers (int)</summary>

Integers are whole numbers (e.g., 2, 18, 31, 5258489). It can be positive or
negative. In Python, you can change the value of an integer directly by
re-declaring it. Integers in Python, can be of any size. It is not limited by
bit size or anything like that.
```python
x = 3           # The value of 'x' in memory is 3.
print(x)        # Output: 3
print(type(x))  # Output: <class 'int'>
x = 7575        # The value of 'x' in memory went from 3 to 7575.
print(x)        # Output: 7575
print(type(x))  # Output: <class 'int'>
x = -128        # The value of 'x' in memory went from 7575 to -128.
print(x)        # Output: -128
print(type(x))  # Output: <class 'int'>
x = 0           # The value of 'x' in memory went from -128 to 0.
print(x)        # Output: 0
print(type(x))  # Output: <class 'int'>
```
</details>

<details>
    <summary>Floating-Point Numbers (float)</summary>

A float can be any real number, except irrationals we can't completely
represent them, obivously. Floats are in IEEE-754 standard. If the float is
bigger than 32-bits, than it changes it to double (64-bit) float as it is in
IEEE-754 standard.
```python
my_float = 3.14          # The value of 'my_float' in memory is 3.14
print(my_float)          # Output: 3.14
other_float = -1839.421  # The value of 'other_float' in memory is -1839.421
print(other_float)       # Output: -1839.41
```
</details>

<details>
    <summary>Complex Numbers (complex)</summary>

Complex numbers are exactly what they are called. They are complex numbers
directly from mathematics. If you want to store the imaginary part of a complex
number, you must specify it with the character `j`.
```python
my_complex_num = 3+4j         # 'my_complex_num' is 3+4j
print(my_complex_num)         # Output: 3+4j
my_other_complex = -345.324j  # 'my_other_complex' is (-345.324j)
print(my_other_complex)       # Output: (-0-345.324j)
my_other_other_complex = my_complex_num + my_other_complex
print(my_other_other_complex) # Output: (3-341.324j)
print(type(my_complex_num))   # Output: <class 'complex'>
```
</details>

<details>
    <summary>Strings (str)</summary>

These are the strings that we've talked about. A string can be of any value
that can be represented by characters. Python uses UTF-8 by default, but it can
be changed. 
```python
my_name = "Jayshozie"  # Value of 'my_name' is "Jayshozie"
print(my_name)         # Output: Jayshozie
print(type(my_name))   # Output: <class 'str'>
```
</details>

<details>
    <summary>Booleans (bool)</summary>

A bool is a truth value. In every programming language different values have
different 'truthy' values. You only need to know what Python's are, so that's
what I'll give you.
```python
my_bool = True
my_other_bool = False
print(my_bool)         # Output: True
```
These are your default booleans, it can be 'True' or 'False'; however, other
numbers and strings have different truthiness, so to say. Values that evaluate
to 'True' are considered 'Truthy', and values that evaluate to 'False' are
considered 'Falsy'. Here are some examples:
```python
# Falsy Values along with 'False' itself:
x = []        # Empty Lists (we'll get to lists in a minute)
y = ()        # Empty Tuples (we'll get to tuples in a minute)
z = {}        # Empty Dictionaries (we'll get to dictionaries in a minute)
k = set()     # Empty Sets (we'll get to sets in a minute)
l = ""        # Empty Strings
r = range(0)  # Empty Ranges (we'll get to ranges in a different markdown)
# Zero of any numeric type is considered Falsy
x = 0    # Integers
y = 0.0  # Floats
z = 0j   # Complex numbers
# Constants that are considered Falsy
b = None  # None constant is falsy
m = False # False constant is considered Falsy, obviously
```
What we mean by false or true will be way more clear in the conditionals
section. Anything other than these are considered 'Truthy' and would evaluate
to 'True'.

<details>
    <summary>Weird Thing as Extra Information</summary>

```python
x = "False"  # Evaluates to 'True' because it's a non-empty string. What it
             # holds doesn't matter.
```
</details>
</details>

## Container Data Types

These are containers, as in they contain other values. It will be more clear
after learning about them, but before we learn about them we need to learn a
concept in programming called 'mutability'. It's basically whether the value of
a variable (it can be a container or a basic data type) can be changed or not.
We'll see examples of it in a minute. There are some 'methods' you need to
learn with containers, I will give them when you need them.

<details>
    <summary>Lists (list)</summary>

A list is a mutable 'list' of values, also called a sequence. It is ordered,
meaning that the order of the elements matter. A list can hold any value you
want to store, such as integers, floats, strings, and even other lists, tuples,
or dictionaries.
```python
# Let's create a list object.
my_list = []  # This creates an empty list with no values in it.
my_list.append(13)
# This will 'append' (add as the last element) 13 to the list
print(my_list)  # Output: [13]
# Let's append another value.
my_list.append("hi")
# This will append the string "hi" to the list as a separate element.
print(my_list)  # Output: [13, "hi"]
```
###     TODO : ADD .pop AND OTHER METHODS OF LISTS
</details>

<details>
    <summary>Tuples (tuple)</summary>

A tuple is an immutable, ordered sequence. Immutable, as in you cannot change
anything in it after you construct it. That means you also cannot use the
method `append()`, because it doesn't exist.
```python
my_tuple = ()  # This creates an empty tuple with no values in it.
my_tuple.append(34)
```
This line should give an error that says something like;
```python
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    my_tuple.append(34)
    ^^^^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append'
```
Don't be scared, it just says that it doesn't understand what `append` means in
this context. This happens because you can't `append` something to a tuple, it
just simply doesn't exist. You should add the values you want to store in a
tuple at the initiation.
```python
my_other_tuple = (2, 3, 5, 7, 11)
print(my_other_tuple)  # Output: (2, 3, 5, 7, 11)
```
After you create that tuple, you can't change anything in it, that's why it's
called immutable.
</details>

<details>
    <summary>Dictionaries (dict)</summary>

A dictionary (dict) is a mutable, unordered, mapping type. In a dictionary, you
store `values` associated with a `key`.
```python
my_dict = {'name': 'Ayse', 'age': 34, 'education': 4}
print(my_dict)  # Output: {'name': 'Ayse', 'age': 34, 'education': 4}
print(type(my_dict))  # Output: <class 'dict'>
```
</details>

-------------------------------------------------------------------------------

# Useful Operations with Numerical Types

## [`type(<data)`](https://docs.python.org/3/library/functions.html#type)


Example Use:
```python

```


## `abs(<number>)`
Example Use:
```python

```

## `pow(<number1>, <number2>`
Example Use:
```python

```

## `round(<float>)`
Example Use:
```python

```

## `sin()`, `cos()`, `log()` from the `math` Library
Example Use:
```python

```

-------------------------------------------------------------------------------

# Useful Operations with Strings

## `str()`
Example Use:
```python

```

## `len()`
Example Use:
```python

```

## `eval()`
Example Use:
```python

```

-------------------------------------------------------------------------------

# Useful Operations with Dictionaries

## `len()`
Example Use:
```python

```

## `values()`
Example Use:
```python

```

## `keys()`
Example Use:
```python

```

-------------------------------------------------------------------------------

# Expressions in Python

## Presedence and Associativity

## Logic in Python

## Type Conversion

-------------------------------------------------------------------------------

# Statements

## Basic Statements

### Assignments

## Compond Statements

### Conditional Statements

### Repetition Statements

-------------------------------------------------------------------------------

# Assignment of W03

Write a Python program that takes 2 values as input, adds them, and prints the
result. Create a Python file, naming doesn't matter but for convention you can
use `W03-assignment.py`. Write your code in it, and run it with Python. If you
don't have Python installed on your computer you can use
[CS50's](https://cs50.dev) online coding environment built on top of Visual
Studio Code. I recommend for you to install
[Python](https://www.python.org/downloads/) and
[Visual Studio Code](https://code.visualstudio.com/) to your PC. This will help
you a lot, since you will be able to reuse a lot of stuff. Check the markdown
named
[W03 How to Install Python and VSCode](./W03--how-to-install-python-and-vscode.md)
for more info.
If you like to have even more pain than CS50's online IDE, you can use
[Google Colab](https://colab.research.google.com/). It's incredibly cramped,
but if you don't want to install anything and just want to pass the course it
should be enough.

Hints:
1. You can use the function `eval(input())` to get input from the user.
2. You should use two different variables for the values the user will give.
3. You can use a third variable to store their product, but it's not necessary.
4. You can print your result with `print()` function, in which you should
specify what you're printing.

```markdown
Example Input/Output (I/O):

Input:
13
12
Output:
25

Input:
10
10
Output:
20
```

-------------------------------------------------------------------------------

# Glossary

1. `print()` : Generic print function. Prints the value given in the argument.

2. `type()` : returns the type of the given argument
    1. Used in 'integers' subsection, it returns 'class <int>', since all
    numbers in that section are integers.
    2. Used in 'floats' subsection, it returns 'class <float>', since all
    numbers in that section are floating-point numbers.
