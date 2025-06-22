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

print(squared_list)  # Output: [1, 4, 9, 16, 25]
```
In this example, the map function goes through the iterable `num_list` and use
all of its items, one-by-one, as arguments to the `square()` function. Lastly,
it takes the return value of the function and stores it in the `squared_map`
variable (object type: `map`).

2. **filter(function, iterable):**



-------------------------------------------------------------------------------

# Recurrence/Recursion

