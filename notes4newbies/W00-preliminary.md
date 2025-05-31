MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Preliminary Information

This markdown is basically a guide on how to read documentations. Actually,
this guide itself is enough to dive into Python.

## What is a documentation of a programming languge?

It's a reference manual of the programming language. It is a series of
definitions, explanations and examples of almost everything you need to know
about a language.

## Why do we need to read it?

For the sake of the argument, imagine you're in a country that you don't know
anything about. You don't know which city, or town you're in. Now, try not to
die. This is what happens when you don't read documentations. The documentation
is the map of that entire country. It's not just a map either, it also shows
you where everything is, how the inner dynamics of a town work. Imagine how
easy would it be to live in that city after you acquire that map. That's what
happens when you read documentations of languages. It's basically your life
saver.

## How to read documentations?

At first it won't be easy. They look very complicated with terminology that you
have no idea. First of all, it gets way easier with time. It may not be the
best way for a complete beginner to start learning a language; however, if you
have even a small amount of knowledge it is the way to go.

### Where are they?

Mostly you can just search for the documentation of a language in your
preferred search engine. For example,
[Python documentation](https://docs.python.org/3) is located at
<https://docs.python.org/3>. This is for Python 3, mind you.

### Where to start?

As I said, if you have a fundamental knowledge on programming, you can just
browse the documentation like you would on Wikipedia. If you have no prior
knowledge you can start with the
[Tutorial](https://docs.python.org/3/tutorial/index.html). You can follow that
tutorial, it's pretty well built.

### But how to read them?

If you want to learn how a specific thing works in a language, just search for
the documentation of that. For example, if you want to learn what the `print()`
function works, search it in the documentation. Read it through until the end,
if you don't understand a term in it, search that and that and that.

If you don't know what you're doing at all, then it would be best to start with
the tutorial I've told you about in the previous subsection.

## How to deal with unknown stuff?

I use this line of questioning.

Do I know what I'm doing, or what I should do?

1. Yes:

    1. Yes: Use it.
    2. No: Search for it in the documentation. Did I find what I'm looking for?

        1. Yes: Use it.
        2. No: Search for it on the Internet. Did I find what I'm looking for
            in sites like [stackoverflow](https://stackoverflow.com) or any
            issue opened on a [GitHub](https://github.com) repository?

            1. Yes: Use it.
            2. No: Ask it on stackoverflow.
                You will almost certainly get the answer you're looking for.

2. No:

    1. Search in stackoverflow directly. Did I find what I'm looking for?
        
        1. Yes: UNDERSTAND IT, then use it.
        2. No: Open up a question on stackoverflow.

As a general guide, if you have no idea what to even search for, use a large
language model (LLM) (commonly known as AI chatbots). Ask the question to that
bot, it will probably understand a general idea of what you mean. It will help
you to understand what to search for.

-------------------------------------------------------------------------------

# Introduction to Programming Concepts

After the preliminary about why and how you should use the documentation of a
programming language, let us start with the foundations of programming
languages.

## What is a programming language?

High-level programming languages, which I'll describe in just a minute, is your
intermediary language between you and your computer. It's not the native
language of either of you. The lines in your code are line-by-line instructions
that you want your computer to do.

**Technical Definition:** *A programming language is a system of notation for
    writing computer programs.*
    [Programming Language](https://en.wikipedia.org/wiki/Programming_language)


## How tf does everything work?

Up at the top, you have your central-processing unit (CPU), and your code.
Your CPU can interpret and execute that code. What happens inside the CPU which
is capable of understanding all that? No idea, too complex. Basically speaking
there are some architectures (e.g. x86 family, ARM family). These architectures
provide the developer with some very low-level, basic commands to bridge the
gap between the high-level programming language, a.k.a. Assembly language.
Assembly language differ from architecture to architecture. This guide won't
help you with that, because you don't need to know it at the moment.

-------------------------------------------------------------------------------

# Basics of Programming

I'll introduce you to some core concepts of programming, via phases. Each phase
has a way to represent, and another way to manipulate data. I will try to give
examples for Windows and Linux/macOS users for as many subjects as I can.

## Phase 1: Value & Command Line

You can interact with your computer directly from the command line. You can
do value manipulation. For example you can add/subtract values. To learn more
about command-line interfaces (CLIs) you can visit
[djangogirl](https://tutorial.djangogirls.org/en/intro_to_command_line/). This
will be of great help to learn your way through the CLI of your machine.

This is the simplest case of programming, where you do basic mathematical
operations and interact with the system directly.

For example, you can calculate the perimeter and the area of a circle:
```python
>>> import math
>>> 2 * math.pi * 10
62.83185307179586  # Perimeter of a circle with radius 10
>>> math.pi * 10**2
314.1592653589793  # Area of a circle with radius 10
```

This sure does work, but you don't want to write everything every single time.

## Phase 2: Variable & Script

Although phase 1 is basically what happens under the hood, it's pretty hard to
do every single calculation by-hand, and it overly underestimates the
capabilities of computers.

You can create variables and assign values to them. For example in the Python3
shell;
```python
>>> my_number = 30  # You just assinged your first variable!
>>> print(my_number)  # This is a print function
30
>>> my_number = "Hi"  # In Python you can change variable type without issue
>>> print(my_number)
Hi  # I did this to show you the variable name doesn't matter.
>>> y = 0.10
>>> x = 12000
>>> z = x + y  # You can assign values to variables while doing things to them
>>> print(z)
12000.1
```

Scripts are files that have executable code in them. Let's take a look at a
better version of the phase 1 example in a `circle.py` file that we've created:
```python
import math
radius = float(input("Radius of the circle: "))
print("Perimeter =", 2 * math.pi * radius)
print("Area =", math.pi * radius**2)
```
If you write these lines in a circle.py file and run it via
```bash session
$ python3 circle.py
```

Here is how it looks like:
```
Radius of the circle: 
10  # Your cursor blinks until you enter a value and press <Enter>
Perimeter = 62.83185307179586
Area = 314.1592653589793
```

There are many terminology up there that you probably don't know. Don't worry
you'll understand them in about 3 markdowns or so. Like I said, it gets easier.

Now we're getting somewhere. You can do somewhat-complex stuff with only
variables and scripts. This can be very useful for simple stuff that you need
to automate.

Now let's get to the heart of programming, functions.

## Phase 3: Argument & Function

You can make things even easier for yourself, by creating a function. A
function is a block of code which takes arguments and keyword arguments, does
stuff to them, and return something. For example here is a function that takes
the name of the user as an argument and lowers the characters in Python;
```python
def lower_my_name(name):
    name_lower = name.lower()
    return name_lower
```
Now, you know how to write functions. Just kidding. The main idea is that you
don't want to write the script everytime you want to do something, so you write
it once in a more general way so when you run it, it just works. For example;
```python
import math
def perimeter_area_circle(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * radius**2
    return perimeter, area
```

Now you can access the variables `perimeter` and `area` anywhere in your code.
For example you can do more complicated stuff like this:
```python
"""
This is a function that takes the side length of a cube calculates the area
difference between that cube and a sphere that perfectly fits inside it.
"""
import math
def volume_diff(side):
    volume_cube = side**3

    radius_sphere = side/2
    volume_sphere = (4/3)*math.pi*(radius_sphere**3)
    
    difference = volume_cube - volume_sphere
    return difference
```

Obviously this is still pretty simple compared to the stuff you will learn in
the course, but I believe it shows the general idea behind functional
programming.

Functional programming is the pinnacle of programming. From now on, we're going
into the deeply controversial territory of object oriented programming.

## Phase 4: Class

According to [Wikipedia](https://en.wikipedia.org/wiki/Object-oriented-programming);

Object-oriented programming (OOP) is a programming paradigm based on the
concept of objects. Objects can contain data (called fields, attributes or
properties) and have actions they can perform (called procedures or methods and
implemented in code). In OOP, computer programs are designed by making them out
of objects that interact with one another.

Basically, maybe you want to have multiple circles and you want to them to have
different radii and you want to keep them in memory.

Let me just show you an example of a class:
```python
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        self.perimeter = 2 * math.pi * radius
        return self.perimeter
    def area(self):
        self.area = math.pi * radius**2
        return self.area
    def properties_of_circle(self):
        print("Perimeter =", self.perimeter)
        print("Area =", self.area)

        return self.perimeter, self.area
```
To create an object of the class Circle;
```python
my_circle = Circle(4)
```
Now in the memory, you have an object called my_circle which has an attribute
called `radius` equal to 4, and nothing else. To calculate the perimeter and
the area of that circle;
```python
perimeter_of_my_circle = my_circle.perimeter()
area_of_my_circle = my_circle.area()
```
Now you have 2 different variables called which hold the perimeter and area
values.
```python
print(my_circle.properties_of_circle())
```
should print
```
Perimeter = 25.132741228718345
Area = 50.26548245743669
```

Yes, they all do the exact same thing; however, they have fundamental
differences and used in different places.

If you didn't understand anything, don't worry you will in 3 markdowns or so.
