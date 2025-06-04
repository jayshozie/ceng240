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
'strings'. There are 2 main types of data you need to know about: Basic and
Container.

P.S: In Python, to assign a value (it can be anything) to a variable, you don't
need to specify which type it should be. Python does its best to understand
what you mean, and stores it itself.

## Basic Data Types

Basic data types store actual values. There are some quirks in Python that you
should know, but I will talk about those when it's time.

<details>
    <summary>Integers (int)</summary>

Integers are whole numbers (e.g., 2, 18, 31, 5258489). In Python, you can
change the value of an integer directly by re-declaring it.
```python
x = 3     # The value of 'x' in memory is 3.
print(x)  # Output: 3
x = 7575  # The value of 'x' in memory went from 3 to 7575.
print(x)  # Output: 7575
```

