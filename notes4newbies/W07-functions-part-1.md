MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Note

This markdown is incredibly important for everyone. Even if you're not going to
pursue a career in computer science, you still need to completely understand
this week's subject, functions, to pass this course. Otherwise, you'll have a
really bad time.

-------------------------------------------------------------------------------

# About Functions

## Why Functions?

As you might've realized, the way we've written scripts so far is a bit weird.
For example, in the
[previous example](./W06-examples-of-conditional-and-repetitive-execution.md#bubble-sort-algorithm),
if we wanted to sort a different list, we need to re-run the script entirely.
If we defined the bubble sort algorithm as a function, however, we would be
able to use it again and again in our code.

> [!NOTE]
> Functions are `reusable`.

You probably heard that functions are also "easier to maintain", but what does
that mean? To understand that, first we need to look at a really unmaintainable
code. The code block you see beneath does a pretty straightforward job. It has
some numerical values, calculates stuff with those.
```python
# Calculate for Bar 1
area_bar1 = 3.14159 * (0.02 / 2)**2
stress_bar1 = 10000 / area_bar1
strain_bar1 = stress_bar1 / 200e9
print(f"Bar 1 - Stress: {stress_bar1:.2f} Pa")

# Calculate for Bar 2 (repeated code!)
area_bar2 = 3.14159 * (0.025 / 2)**2
stress_bar2 = 12000 / area_bar2
strain_bar2 = stress_bar2 / 200e9
print(f"Bar 2 - Stress: {stress_bar2:.2f} Pa")
```
But, here is the thing. What if you need to change the value of the pi from
`3.14159` to `3.141519265`, or what if you need to change any other `repeated`
value in the code. It may look, or actually be, easy for 10 lines of code, but
what if you had hundreds, maybe thousands of lines of code? Then, you will
definitely screw up something, and it will be incredibly harder to trace.

> [!NOTE]
> Functions are easier to `maintain`.

Finally, consider large programs. Without functions, your entire script would
be one long, continuous block of code. This makes it incredibly difficult to
navigate, understand the flow, or even locate specific parts of the program.
Functions allow you to break down complex problems into smaller, manageable
chunks, each responsible for a specific task. This modularity makes your code
much more organized and easier to comprehend, both for yourself and for anyone
else reading your code.
```python
def calculate_bar_properties(diameter, force):
    area = 3.14159 * (diameter / 2)**2
    stress = force / area
    strain = stress / 200e9
    return stress, strain

# Calculate for Bar 1
stress1, strain1 = calculate_bar_properties(0.02, 10000)
print(f"Bar 1 - Stress: {stress1:.2f} Pa")
# Calculate for Bar 2
stress2, strain2 = calculate_bar_properties(0.025, 12000)
print(f"Bar 2 - Stress: {stress2:.2f} Pa")
```

> [!NOTE]
> Functions are `structured`.

-------------------------------------------------------------------------------

## Functions in Programming vs Mathematics

> In math, remember a function is basically a rule or a process that takes an
> input and gives you back a single, predictable output.
[^KhanAcademy]

The type of functions we'll see are similar to the ones in mathematics, but
there are some core differences. First of all, a function doesn't have to
return something in programming. Basically, it probably does something in the
background, but it doesn't have to show something. Think of functions this way,
they are structured abstract algorithms that you write ahead of time to do the
stuff you don't want to do multiple times. Secondly, a function in mathematics
only depends on its arguments. That's not the way things work around here. The
function you've written may not even need arguments. I'll give examples of all
of these different cases. Last thing about functions is that, functions in
maths don't have side effects. Ours do.

Also, this is a good time to talk about abstraction.

-------------------------------------------------------------------------------

## Functions in Python

Don't forget that syntax always matters, and it's really important. Python
interpreter won't understand what you mean if you don't follow the language's
rules. In Python, more than other languages anyway, indentation is extremely
important. You probably realized that when we were studying conditionals. You
need to be extremely careful with your indentations, because Python's
interpreter trusts you completely with them.

> [!IMPORTANT]
> ### Syntax of Functions in Python
> ```python
> def <name_of_your_function>(*arguments, **keyword_arguments):
>     # your code
> ```

### Nested Functions

I hate to talk about these, because they mostly use these to confuse you in
exams, and they're not even used that often, because they, most of the time,
only confuse people.

Nested functions are functions defined inside other functions. They can be
useful for encapsulating functionality that is only relevant within the context
of the outer function. However, they can also make code harder to read and
maintain, so use them judiciously. (Thanks, Copilot. For explaining this
without making me mad.)
```python
def f(N):
    Number = N
    def g():
        C = 20
        return N*Number
    print(f"Number {N}, and its square: {g()}")
```

In this example, function `g()` can access all the local variables as well as
the parameters of the function `f()`. Function `f()`, however, cannot access
the local variables of `g()`. This is due to the something called `scope`,
which we'll get to in a minute. No function can be used before it's been
defined, this includes `g()`. For example, line 2 couldn't be the line below.
```python
Number = 10 * g(10)
```
Remember when I said indentation is incredibly important? Yeah, that's why the
`print()` function at the end belongs to `f()` and not `g()`.
<details>
    <summary>Vent</summary>

I know this example is only here as a "bad" example, but this is so bad it
confuses first-timers. Also, nested functions are not even needed that much.
They only use these in the midterm and finals, just to confuse you and force
you to make a mistake. This mentality is the reason why someone with grade 70
can get a AA from this course. I hate them so fucking much.
</details>

### Scope in Python

To understand global variables and nested functions better, we need to
understand what is scope. Scope refers to the visibility and lifetime of a
variable within a program. In Python, there are two main types of scope: local
and global.

As I always do, I'm going to recommend you to read the documentation, rather
than trying to understand whatever they mean in the slides.

> [!IMPORTANT]
> What is a scope? (direct quote from the documentation[^Scope])
>
> A scope defines the visibility of a name within a block. If a local variable
> is defined in a block, its scope includes that block. If the definition
> occurs in a function block, the scope extends to any blocks contained within
> the defining one, unless a contained block introduces a different binding for
> the name. When a name is used in a code block, it is resolved using the
> nearest enclosing scope. The set of all such scopes visible to a code block
> is called the block’s environment.

#### Local Scope
Local scope refers to variables defined within a function. These variables are
only accessible within that function and are destroyed once the function
execution is complete. For example:
```python
def my_function():
    local_variable = 10  # This variable is local to my_function
    print(local_variable)

my_function()  # Output: 10
# print(local_variable)
# This would raise an error because local_variable is not defined outside
# my_function, thus not accessible here.
```

#### Global Scope
Global scope refers to variables defined outside of any function. These
variables are accessible from anywhere in the program, including inside
functions.
```python
global_variable = 20  # This variable is global
def another_function():
    print(global_variable)  # This can access the global variable

another_function()  # Output: 20
print(global_variable)
# This wouldn't raise an error since it's a global variable
```

#### LEGB Rule in Python (included)

The LEGB rule is a way Python resolves names. It stands for:
- **L**ocal: Names defined within the current function.
- **E**nclosing: Names in the local scope of enclosing functions.
- **G**lobal: Names defined at the top level of the module or declared global.
- **B**uilt-in: Names pre-defined in Python (like `print()`, `len()`, etc.).

When you reference a name, Python searches for it in the order of LEGB. If it
finds the name in the local scope, it uses that. If not, it checks the
enclosing scope, then the global scope, and finally the built-in scope. If it
doesn't find the name in any of these scopes, it raises a `NameError`.
```python
def outer_function():
    x = 10  # Local variable in outer_function
    def inner_function():
        x = 20  # Local variable in inner_function
        print(f"Inner function: {x}")  # This will print 20
    inner_function()
    print(f"Outer function: {x}")  # This will print 10

outer_function()
# Output:
# Inner function: 20
# Outer function: 10
```

### Global Variables in Python

Global variables are variables defined globally. I don't even know why is this
in a separate slide.

Global variables are variables that are defined in the `global scope`.
```python
event_count = 0  # global variable

def outer_function():
    # global event_count
    # this wouldn't make it accessible in inner_function()
    def inner_function():
        global event_count
        # That's why you need to use the global keyword to call it and not
        # redefine it.
        event_count += 1
        # Since we've called the variable into this scope we can use and
        # manipulate it.
        print(f"  Inner function increments. Count: {event_count}")
```

> [!WARNING]
> Global variables are not recommended to use. Here is three reasons why:
> 1. **Hidden Side Effects:** Makes it unclear what a function modifies outside
> of its direct inputs.
> 2. **Hard to Debug:** Changes to global variables can cause unexpected behavior
> elsewhere, making bugs difficult to trace back.
> 3. **Poor Reusability:** Functions become tied to specific global states,
> making them less modular and harder to use.

### Updating Nonlocal Variables

There are three main methods of doing this.

1. **Using the Function Like an Object**
```python
def f():
    f.a = 10

    def m():
        f.a = 20

    m()
    print(f"a (method 1): {f.a}")

f()  # Output: a (method 1): 20
```

2. **Using the `nonlocal` Keyword**
```python
def g():
    a = 10

    def m():
        nonlocal a
        a = 20

    m()
    print(f"a (method 2): {a}")

g()  # Output: a (method 2): 20
```

3. **Using a Mutable Datatype**
```python
def h():
    a = [1]

    def m():
        a[0] = 20

    m()
    print(f"a (method 3): {a}")

h()  # Output: a (method 3): 20
```

### Parameter Passing in Functions

<details>
    <summary>Explanation of Below</summary>

In the function `g`, the variable `a` is defined with a value of 20. When
`f(a)` is called, it passes the value of `a` (which is 20) to the function `f`.
Inside `f`, the parameter `n` receives this value, and then `n` is modified by
adding 20 to it. However, this modification does not affect the variable `a` in
the function `g`, because integers are immutable in Python.
</details>

```python
def f(n):
    n = n + 20

def g():
    a = 10
    print(a)
    f(a)
    print(a)

g()
# Output: 
# 10
# 10
```

<details>
    <summary>Explanation of Below</summary>

In this example, the function `f` takes a list as an argument and modifies its
first element to 'A'. When `g` is called, it creates a list `L` with three
elements. When `f(L)` is called, it modifies the first element of the list `L`
to 'A'. Since lists are mutable in Python, the change is reflected in the
list `L` defined in `g`. Therefore, the output shows the modified list after
the function call.
</details>

```python
def f(List):
    List[0] = 'A'

def g():
    L = [1, 2, 3]
    print(L)

    f(L)
    print(L)

g()
# Output:
# [1, 2, 3]
# ['A', 2, 3]
```

<details>
    <summary>Explanation of Below</summary>

In this example, the function `f` attempts to reverse the list passed to it
using slicing (`List[::-1]`). However, this operation creates a new list
instead of modifying the original list in place. When `g` is called, it creates
a list `L` with three elements. When `f(L)` is called, it reverses the list but
does not modify the original list `L` in `g`. Therefore, the output shows that
the original list `L` remains unchanged after the function call.
</details>

```python
def f(List):
    List = List[::-1]

def g():
    L = [1, 2, 3]
    print(L)

    f(L)
    print(L)

g()
# Output:
# [1, 2, 3]
# [1, 2, 3]
```

-------------------------------------------------------------------------------

## Further Dissecting Functions

### Arguments (\*Args) and Keyword Arguments (\*\*Kwargs)

OK, we've seen how arguments (args) work. Now, we need to talk about keyword
arguments, a.k.a. kwargs. It's pretty straightforward so I'll just show an
example to you.
```python
def f(a=10, b=20):
    print(f"a: {a}, b: {b}")

f()  # Output: a: 10, b: 20
```
When you call a function with keyword arguments, you can specify the arguments
by name, allowing you to skip some arguments or change their order.
```python
# Omitting
f(b=30)  # Output: a: 10, b: 30
# Changing order
f(b=30, a=40)  # Output: a: 40, b: 30
```
Keyword arguments are sometimes called `defaults`, because they allow you to
set default values for parameters. If you don't provide a value for a keyword
argument, the function will use the default value specified in the function
definition. This is useful for creating functions that can be called with
fewer arguments than defined, while still providing sensible defaults.

You can also mix positional and keyword arguments in a function call. Positional
arguments must come before keyword arguments, and you can skip some positional
arguments as long as you provide values for the keyword arguments that follow.
```python
def f(a, b=20, c=30):
    print(f"a: {a}, b: {b}, c: {c}")

f(10)  # Output: a: 10, b: 20, c: 30
f(10, c=40)  # Output: a: 10, b: 20, c: 40
f(10, 50, c=60)  # Output: a: 10, b: 50, c: 60
```

<!-- Below part is not in italics, it only looks like it is. -->
You can also use `*args` and `**kwargs` to accept a variable number of
positional and keyword arguments, respectively. This allows you to create
functions that can handle a flexible number of arguments.
```python
def f(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

f(1, 2, 3, a=10, b=20)

# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'a': 10, 'b': 20}
```

-------------------------------------------------------------------------------

## A Short Summary of [W07.5](./W07.5-extra-dissecting-python.md)

Note: The [next chapter](./W07.5-extra-dissecting-python.md) is not included in
the course, I've written it only for the curious. This means that this summary
also is not included.

###     TODO : ADD A SHORT SUMMARY OF W07.5

-------------------------------------------------------------------------------

# References

[^KhanAcademy]: [Khan Academy : What is a function?](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:evaluating-functions/v/what-is-a-function#:~:text=and%20from,and%20only%20ONE%20given%20output.) | 
[^Scope]: [Documentation : What is scope?](https://docs.python.org/3/reference/executionmodel.html#resolution-of-names) | 
