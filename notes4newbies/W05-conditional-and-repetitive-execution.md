MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Note

One of the stupid things about this course, they do explain these stuff in
week 3. I won't go into much detail, because I did in
[week 3's markdown](./W03-intro-to-python-1.md). You can find example in
[week 6's markdown](./W06-examples-of-conditional-and-repetitive-execution.md).

-------------------------------------------------------------------------------

# Conditional Executions and Expressions

The difference between conditional execution and conditional expression is that
- Conditional EXECUTION is a statement that executes a block of code if a
condition is true.
- Conditional EXPRESSION is an expression that evaluates to a value based on a
condition.

## Conditional Execution

Conditional execution is a statement that executes a block of code if a
condition is true. It is often used to control the flow of a program based on
the evaluation of a condition. The most common form of conditional execution is
the `if` statement, which allows you to execute a block of code if a specified
condition is true. If the condition is false, the block of code is skipped.
```python
if condition:
    <some_code>
elif another_condition:
    <some_other_code>
else:
    <some_another_code>
```

### Example
```python
age = 20
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

## Conditional Expression

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


###     TODO : DON'T FORGET NESTED STUFF

-------------------------------------------------------------------------------

# Repetitive Execution



###     TODO : DON'T FORGET NESTED STUFF

-------------------------------------------------------------------------------

# Extra - Set and List Comprehension

###     TODO : HERE
