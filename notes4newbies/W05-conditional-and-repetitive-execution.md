MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Note

This is one of the stupidest things about this course, they do explain these
stuff in week 3. I won't go into much detail, because I did in
[week 3's markdown](./W03-intro-to-python-1.md). You can find example in
[week 6's markdown](./W06-examples-of-conditional-and-repetitive-execution.md).

-------------------------------------------------------------------------------

# Conditional Executions and Expressions

The difference between conditional execution and conditional expression is that
- Conditional EXECUTION is a statement that executes a block of code if a
condition is true. You can find the explanation of conditional execution in
[week 3's markdown](./W03-intro-to-python-1.md#conditional-statements)
- Conditional EXPRESSION is an expression that evaluates to a value based on a
condition.

## Conditional Expressions

Conditional expression is an expression that evaluates to a value based on a
condition. It is often used to assign a value to a variable based on the
evaluation of a condition. The most common form of conditional expression is
the ternary operator, which allows you to evaluate a condition and return one
of two values based on the evaluation of that condition.
```python
value = <true_value> if <condition> else <false_value>
```

### Example
```python
age = 20
status = "minor" if age < 18 else "adult" if age < 65 else "senior citizen"
print(status)  # Output: adult
```

### An Easier Example
```python
age = 20
status = "minor" if age < 18 else "adult"
print(status)  # Output: adult
```

## Nested Conditional Execution

Nested conditional execution is when you have a conditional statement inside
another conditional statement. This allows you to check multiple conditions
and execute different blocks of code based on the evaluation of those
conditions.
```python
if <condition1>:
    # Block of code if condition1 is true
    if <condition2>:
        # Block of code if condition1 AND condition2 is true
    else:
        # Block of code if condition1s true AND condition2 is false
else:
    # Block of code if condition1 is false
```

### Example
```python
age = 20
if age < 18:
    print("You are a minor.")
else:
    if age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
# Output: You are an adult.
```

-------------------------------------------------------------------------------

# Repetitive Execution

Repetitive execution is a programming concept that allows you to execute a
block of code multiple times based on a condition or a specific number of
iterations. There are two main types of repetitive execution in Python: loops
and comprehensions.

## Loops
Loops are used to execute a block of code repeatedly until a certain condition
is met. The most common types of loops in Python are the `for` loop and the
`while` loop.

### For Loop
The `for` loop is used to iterate over a sequence (like a list, tuple, or
string) or any iterable object. It executes a block of code for each item in
the iterable.
```python
for item in iterable:
# Block of code to execute for each item
```

#### Example
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

### While Loop

The `while` loop is used to execute a block of code as long as a specified
condition is true. It checks the condition before each iteration, and if the
condition is true, it executes the block of code. If the condition becomes
false, the loop stops executing.
```python
while <condition>:
    # Block of code to execute while the condition is true
```
```python
count = 0
while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4
```

#### Infinite Loops

Infinite loops occur when the condition of a `while` loop always evaluates to
true, causing the loop to run indefinitely. This can happen if the condition
never becomes false or if there is no mechanism to break out of the loop.
```python
# Infinite Loop
while True:
    print("This will run forever unless you stop it manually!")
    # To stop this loop, you can use Ctrl+C in the terminal or stop the execution in your IDE.
```

Infinite loops can be useful in certain scenarios, such as waiting for user
input or continuously checking for a condition. However, they should be used
with caution, as they can lead to unresponsive programs if not handled
properly.
```python
# Infinite Loop with a Break Condition
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # This will stop the loop when count reaches 5
# Output:
# 0
# 1
# 2
# 3
# 4
```

For more info visit [week 3's markdown](./W03-intro-to-python-1.md#the-for-statement).

## Nested Loops

Nested loops are loops that are placed inside another loop. This allows you to
iterate over multiple sequences or perform more complex iterations. The inner
loop will complete all its iterations for each iteration of the outer loop.
```python
for outer_item in outer_iterable:
    for inner_item in inner_iterable:
        # Block of code to execute for each combination of outer_item and inner_item
```

### Example
```python
outer_list = [1, 2]
inner_list = ['a', 'b']
for outer_item in outer_list:
    for inner_item in inner_list:
        print(f"Outer: {outer_item}, Inner: {inner_item}")
# Output:
# Outer: 1, Inner: a
# Outer: 1, Inner: b
# Outer: 2, Inner: a
# Outer: 2, Inner: b
```

Nested loops can also be used with `while` loops, but they are less common.
```python
outer_count = 0
while outer_count < 2:
    inner_count = 0
    while inner_count < 2:
        print(f"Outer: {outer_count}, Inner: {inner_count}")
        inner_count += 1
    outer_count += 1
# Output:
# Outer: 0, Inner: 0
# Outer: 0, Inner: 1
# Outer: 1, Inner: 0
# Outer: 1, Inner: 1
```

-------------------------------------------------------------------------------

# Extra - Set and List Comprehension

Set and list comprehensions are concise ways to create sets and lists in
Python. They allow you to generate a new set or list by applying an expression
to each item in an iterable, such as a list or a range. This can be useful for
creating new collections based on existing ones, filtering items, or
transforming items in a collection.

## List Comprehension
```python
new_list = [expression for item in iterable if condition]
```

## Set Comprehension
```python
new_set = {expression for item in iterable if condition}
```

## Examples of Set and List Comprehension

```python
# List comprehension example
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers if x % 2 == 0]
print(squared_numbers)  # Output: [4, 16]

# Set comprehension example
numbers_set = {1, 2, 3, 4, 5}
squared_numbers_set = {x**2 for x in numbers_set if x % 2 == 0}
print(squared_numbers_set)  # Output: {16, 4}
```
###     TODO : EXPLAIN WHY THE ORDER IS REVERSED IN THE SET EXAMPLE
###     CONTRIBUTION : I couldn't find why it is reversed, tbh. If you know
###                    why, I would love to know. Please open a PR.

-------------------------------------------------------------------------------







###     TODO : ASSIGMENT(S)









