MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Variables (cont.)

## Aliasing Issue in Python

Every data, constant or not, has an identifier, stored as an integer in Python.
```python
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
```python
>>> a = ['a', 'b']
>>> b = a
>>> b[0] = 0
>>> a
[0, 'b']
```
<details>
    <summary>More Examples</summary>

```python
>>> a = 4
>>> b = [1, 2, 3, a]
>>> a = 8
>>> print(b)
[1, 2, 3, 4]  # This is even worse than the previous example
```
```python
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
```python
>>> print("Hi.\nMy name is Jay.\nI'm gonna fail all my courses this semester.")
"Hi."
"My name is Jay."
"I'm gonna fail all my courses this semester."
# There won't be `"` characters normally, I've added them for correct coloring
# on GitHub
```
But sometimes you do want to use the backslash character, then you should use
raw strings.
```python
>>> print(r"C:\Users\foo\bar")
"C:\Users\foo\bar"
# There won't be `"` characters normally, I've added them for correct coloring
# on GitHub
```
If you were to use a normal string literal with that, you would probably get
some kind of an error:
```python
>>> print("C:\Users\foo\bar")
"""
  File "<python-input-8>", line 1
    print("C:\Users\foo\bar")
          ^^^^^^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
"""
# There won't be `"""` characters normally, I've added them for correct
# coloring on GitHub
```

## Byte Strings (`b`, `B` prefix)

The prefixes `b` and `B` indicatees a **byte string literal**.

## Unicode Strings (`u`, `U` prefix)

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
</details>


Latest Version: [Documentation](https://docs.python.org/3.13/reference/lexical_analysis.html#string-and-bytes-literals)

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












