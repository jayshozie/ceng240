MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Variables (cont.)

## Aliasing Issue in Python

Every data, constant or not, has an identifier, stored as an integer in Python.
```pycon
>>> a = 1
>>> b = 1
>>> id(1)
140165965326288
>>> id(a)
140165965326288
>>> id(b)
140165965326288
```
If the data is mutable, then we have a problem:
```pycon
>>> a = ['a', 'b']
>>> b = a
>>> b[0] = 0
>>> a
[0, 'b']
```
<details>
    <summary>More Examples</summary>

```pycon
>>> a = 4
>>> b = [1, 2, 3, a]
>>> a = 8
>>> print(b)
[1, 2, 3, 4]  # This is even worse than the previous example
```
```pycon
>>> a = [1,2]
>>> b = [1,2,a]
>>> a
[1, 2]
>>> b
[1, 2, [1, 2]]
>>> a.append(3)
>>> b
[1, 2, [1, 2, 3]]
>>> a
[1, 2, 3]
```
</details>

This is called aliasing, and even though it can be useful, it most likely will
fuck up your code. Don't do it, be careful not to do it accidentally.

## Variable Names

- Variable names are case-sensitive in Python, so `a` and `A` are two different
variables.
- Variable names can contain English letters a-z, A-Z, numbers 0-9, the
underscore `_` character, and nothing else.
- Variable names can only start with a letter or the underscore `_` character,
meaning the variable names `10a`, `$a`, and `var$` are invalid.
- Variable names cannot be one of the keywords in Python:
<details>
    <summary>List of Reserved Names in Python</summary>

```markdown
False   await     else     import    pass
None    break     except   in        raise
True    class     finally  is        return
and     continue  for      lambda    true
as      def       from     nonlocal  while
assert  del       global   not       with
async   elif      if       or        yield
```
Latest Version: [Documentation](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
</details>

-------------------------------------------------------------------------------

# More Info About the `print()` and `input()` Functions

As you might've seen in the previous examples, the `print()` and the `input()`
functions have a lot of functionality and 'settings'. Let's dive in.

First, we need to talk about different kinds of strings. We've seen the generic
string type, but there are more. If you remember, the full name of the string
type is `string literal`, we will work with that.

## Raw Strings (`r`, `R` prefix)

The prefixes `r` and `R` indicates a **raw string literal**. If you've messed
around with the interpreter up until now, you may have noticed that the `\`
(backslash) character cannot be used in string literals, because it's reserved
as the escape character. You can do stuff like this:
```pycon
>>> print("Hi.\nMy name is Jay.\nI'm gonna fail all my courses this semester.")
Hi.
My name is Jay.
I'm gonna fail all my courses this semester.
```
But sometimes you do want to use the backslash character, then you should use
raw strings.
```pycon
>>> print(r"C:\Users\foo\bar")
C:\Users\foo\bar
```
If you were to use a normal string literal with that, you would probably get
some kind of an error:
```pycon
>>> print("C:\Users\foo\bar")
  File "<python-input-8>", line 1
    print("C:\Users\foo\bar")
          ^^^^^^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
```

## Byte Strings (`b`, `B` prefix)

The prefixes `b` and `B` indicates a **byte string literal**. Characters in
byte strings are not stored as Unicode characters, but bytes.
```python
byte_data = b"Hello, World!"
print(byte_data)  # Output: b'Hello, World!'
print(type(byte_data))  # Output: <class 'bytes'>
```
You can't mix normal strings with byte strings, Python will raise a TypeError.
```pycon
>>> new_str = byte_data + "will give error"
```
```Python traceback
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    new_str = byte_data + "will give error"
              ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
TypeError: can't concat str to bytes
```

## Unicode Strings (`u`, `U` prefix)

The prefixes `u` and `U` indicates a **Unicode string literal**. This is the
same type of strings that I've been talking about as `normal` strings. This
prefix still exists only for backwards compatibility with Python 2, you don't
need to use it.
```python
print(u"Same string, same encoding, same storing type.")
# Output: Same string, same encoding, same storing type.
print("Same string, same encoding, same storing type.")
# Output: Same string, same encoding, same storing type.
```
The `u` prefix is not necessary in Python 3, as all strings are Unicode by
default. However, you can still use it if you want to make it explicit.

## Formatted Strings (f-Strings)

Formatted strings (a.k.a. f-strings) are a way of 

It's achieved by either using the `f` prefix before the string, or using the
`format()` method for strings.
```python
my_str = "This is a {0} string literal."
my_fstr = f"This is a formatted string."
my_other_fstr = my_str.format('formatted')

print(my_str)  # Output: This is a {0} string literal.
print(my_fstr)  # Output: This is a formatted string.
print(my_other_fstr)  # Output: This is a formatted string literal.
```
Not exactly the best examples, but we will see better ones in a minute.

<details>
    <summary>Better Examples</summary>

```python
age = input("Please enter your age:")
# This line print the string literal "Please enter your age:" & waits for input

print(f"Your age is {age}. Stored.")  # User entered 18 as input
# Output: Your age is 18. Stored.
```

###     TODO : ADD MORE EXAMPLES

</details>

There are some little quirks with formatting numerical values in f-strings. For
example, let's say that you want to show only the first two decimal places in
a float you calculated, here's two ways how you can achieve that.
```python
pi_approx = 22/7

print(f"{pi_approx:.2f}")
# Output: 3.14

print("{:.2f}".format(pi_approx))
# Output: 3.14
```
In the first example, you use the variable just like you would without changing
the value, but then use a `:` colon character and then the formatting
specification, which is `.2f` in this case, meaning that you want to show the
value as a float with two decimal places. In the second example, you use the
`format()` method of the string, and pass the formatting specification as an
argument to the method. This is called the
[format specification mini-language](https://docs.python.org/3.13/library/string.html#format-specification-mini-language).

Latest Documentation of String and Bytes Literals:
[Documentation](https://docs.python.org/3.13/reference/lexical_analysis.html#string-and-bytes-literals)

-------------------------------------------------------------------------------

# Ignored Syntax in Python

There are some intentional syntax in Python, actually in all programming
languages, that the interpreter (or compiler) automatically ignores.

In-Line Comments
```python
x = 5  # Python interpreter will ignore everything after the '#' character
```

Multi-line Comments (used for docstrings)
```python
"""
Everything in 3 `"` character combos are ignored
    by the Python interpreter.
        You can do whatever you want in these
                and

    the Python

                interpreter


will ignore these lines.
"""
```

`pass` Keyword
```python
if <a_condition>:
    pass  # @TODO Add this later
else:
    statement-1
    statement-2
```
With the `pass` keyword you can skip that block without errors, because if you
don't put anything indented after `if`, `elif`, `else`, `for`, `while` blocks
Python will give out an error. You can get rid of the error by using the `pass`
keyword.

-------------------------------------------------------------------------------












