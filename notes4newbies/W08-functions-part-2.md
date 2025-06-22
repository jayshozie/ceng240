MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Higher-Order Functions

Higher-order functions have two types. First type take one or morefunctions as
arguments, the second type return a function as the result. Advantages of using
higher-order functions: code reusability (e.g. mapping, filtering), abstraciton
(hiding complex stuff behind function calls), and flexibility (you can create
highly customizable and adaptable code). The official slides explicitly show
you two functions.

1. **map(function, iterable):**

The `map()` function allows you to take an iterable (e.g. list, set), and use
its items as arguments for the function that is given as argument. The returns
of the function is the output of the `map()` function.

For example, you can square a list of numbers like this:
```python
def square(x):
    return x*x

num_list = [1, 2, 3, 4, 5]

squared_map = map(square, num_list)

squared_list = list(squared_map)
# Changing the type of the object from `map` to `list`, so it's human-readable.

## You don't need to do it in separate lines and use different variables
# squared = list(map(square, num_list))
## will work without issues.

print(squared_list)  # Output: [1, 4, 9, 16, 25]
```
In this example, the map function goes through the iterable `num_list` and use
all of its items, one-by-one, as arguments to the `square()` function. Lastly,
it takes the return value of the function and stores it in the `squared_map`
variable (object type: `map`).

2. **filter(function, iterable):**

The `filter()` function allows you to filter the contents of an iterable
according to the return of the function given as argument.

For example, you can filter out even numbers in a list:
```python
def is_even(x):
    if x % 2 == 0:
        return x
    else:
        return False
# return x % 2 == 0

num_list = [n for n in range(20)]
## evaluates to:
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

evens_filter = filter(is_even, num_list)

evens = list(evens_filter)
# Same thing applies to the `filter()` function. It creates a `filter` object
# that can be converted into a list.

## Again, you con do the above two lines in a single line.
# evens = list(filter(is_even, num_list))

print(evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

<details>
    <summary>Extra Built-in Higher-Order Functions</summary>

###     TODO : ADD

</details>

-------------------------------------------------------------------------------

# Recurrence/Recursion

Recurrence is a mathematical term meaning that a function is defined by itself.
For example, the factorial of a number, except zero, is defined by the
factorial of the number before it and itself.
```text
0! = 1
1! = 1
2! = 1! × 2 = 2
3! = 2! × 3 = 6
.
.
.
N! = (N-1)! × N
```

In programming, recursion is, similarly, a technique where a function solves a
problem by calling *itself* one or more times. This is an especially useful
technique when the argument is structured like a tree.

A very simple example would be to write a function that calculates the
factorial of a given number.
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

<details>
    <summary>A Shorter Version</summary>

```python
def factorial(n): return 1 if n == 0 else n * factorial(n-1)
# Personally, I'm not a fan of single-line functions.
```
</details>
There are two parts to a recursive algorithm. First one is the **base case**,
which is the case where the function stops calling itself. You can see that in
the example's first if case. If a condition (n == 0) is true at any point in
the execution, the algorithm stops calling itself. The base case is absolutely
crucial, because otherwise the function will call itself forever. The second
one is the **recursive case**, which is the case where the function actually
calls itself. Again, you can see that in the else case of our function.
Whenever the condition is met (n != 0), the algorithm calls itself, again and
again. Until the base case is met.

Another example could be an algorithm that calculates the Fibonacci sequence.
```python
def fibonacci(n):
    if n <= 1:  # Base Case: fibonacci(0) = 0, fibonacci(1) = 1
        return n
    else:  # Recursive Case: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n-1) + fibonacci(n-2)
```
It's almost exactly the same as the previous one, so I'm going to leave
understanding this to you.

Recursive algorithms always can be written with loops and vice versa; however,
in some cases the recursive solution may look better, be understood easily, be
concise. These cases include traversing tree-like data structures, certain
mathematical algorithms, generating fractals. In these cases, it mostly mirrors
the problem's mathematical definition.

Putting the benefits aside, there are some drawbacks to using recursion. First
of all, in Python, simple problems will probably be more efficient with using
just a loop due to the overhead of function calls with recursion. Another one
happens if the developer was not very careful while writing the program. It's
called stack overflow (yes, the website's name comes from this). Without a
correctly defined base case, or for very deep recursions, you risk hitting
Python's recursion limit and raising a
[`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError).
Also, for very complex algorithms, recursion make the code seem even more
complicated then a loop.
