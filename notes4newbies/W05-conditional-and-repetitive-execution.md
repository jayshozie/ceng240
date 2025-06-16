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

For more info visit [week 3's markdown](./W03-intro-to-python-1.md#the-for-statement).

###     TODO : DON'T FORGET NESTED STUFF

-------------------------------------------------------------------------------

# Extra - Set and List Comprehension

###     TODO : HERE
