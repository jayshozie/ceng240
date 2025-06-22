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
    return x % 2 == 0

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
2! = 2
3! = 6
.
.
.
N! = (N-1)! × N
```

In programming, however, recursion is a technique where a function solves a
problem by calling *itself* one or more times. This is an especially useful
technique when the argument is structured like a tree.

A very simple example 


