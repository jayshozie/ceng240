MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Object-Oriented Programming

## What is it?

To understand object oriented programming (OOP), we first need to understand
what this `object` that I've been talking about since the beginning of the
course means. An object is a self-contained unit that bundles together **data**
(what it is, what are its characteristics), and **behavior** (what it can do,
what are its actions). This is a pretty abstract definiton, so let's bring it
down to earth with an example.

Imagine an object called `My_Car`, and it's moving. Its data (attributes in
Python) may be `color`, `model`, or `current_speed`; and its behavior (methods
in Python) may be `accelerate()`, `brake()`, `turn_off()`, or `turn_on()`. When
you need to go faster, you call the `accelerate()` method; when you need to
slow down, you call the `brake()` method. This probably still feels to
abstract, but we will get there, don't worry.

## Classes

A `class` is the blueprint of objects. Let's build on what we've built already.
We can talk about a class named `Car` in our previous example. When we create
an object of this class, called `My_Car`, that object will have all the
attributes and methods the original blueprint, class `Car`, has.

<details>
    <summary>Example Car Class</summary>

```python
class Car:
    def __init__(self, model, color, current_speed, is_running):
        self.model = model
        self.color = color
        self.current_speed = current_speed
        self.is_running = is_running

    def turn_on():
        if not self.is_running:
            self.is_running = True
            self.current_speed = 0
            print("Car is turned on.")
        else:
            print("Car is already on.")

    def turn_off():
        if self.is_running:
            self.is_running = False
            self.current_speed = 0
            print("Car is turned off.")
        else:
            print("Car is already off.")

    def accelerate(speed):
        if self.is_running:
            self.current_speed += speed  # accelerate by {speed} km/h
            print(f"Accelerated by {speed} km/h.\nCurrent Speed: {current_speed} km/h.")
        else:
            print("Car is not on.")

    def brake(speed):
        if self.is_running:
            self.current_speed -= speed  # decelerate by {speed} km/h
            print(f"Decelerated by {speed} km/h.\nCurrent Speed: {current_speed} km/h.")
        else:
            print("Car is not on.")
```

I know this looks complicated, but it isn't. I need you to follow this markdown
while looking at this constatly.
</details>

In the example `Car` class case, we would do stuff like:
```python
My_Car = Car(1998, 'red', '0', False)
# This would create us an object called `My_Car` of class `Car` with the
# attributes: model=1998, color='red', current_speed=0, is_running=False
My_Car.turn_on()
# Output: Car is turned on.
My_Car.accelerate(10)
# Output: Accelerated by 10 km/h.
# Output: Current Speed: 10 km/h.
My_Car.brake(10)
# Output: Decelerated by 10 km/h.
# Output: Current Speed: 10 km/h.
My_Car.turn_off()
# Output: Car is turned off.
```
The main thing is that, I can create more cars without interfering with this
specific one. For example,
```python
My_Other_Car = Car(2025, 'jet black', '0', False)
My_Other_Car.turn_on()
# Output: Car is turned on.
My_Car.turn_on()
# Output: Car is turned on.

My_Other_Car.accelerate(50)
# Output: Accelerated by 50 km/h.
# Output: Current Speed: 50 km/h.
My_Car.accelerate(10)
# Output: Accelerated by 10 km/h.
# Output: Current Speed: 10 km/h.

My_Other_Car.brake(20)
# Output: Decelerated by 20 km/h.
# Output: Current Speed: 30 km/h.
My_Car.accelerate(10)
# Output: Accelerated by 10 km/h.
# Output: Current Speed: 20 km/h.
```
As you can see in this example, we have 2 different objects, holding two
entirely different sets of data, but having the same blueprint (same class).

## Defining Classes

To define a class, first you need to give it a name, conventionally starting
with a capital letter:
```python
class MyClass:
    # class content goes here now
    pass  # placeholder for now
```

1. **The `__init__` Method (Object Constructor):** If the class has this method
it automatically gets called when an object of that class is constructed.

2. **The `self` Parameter:** Although you can name it differently, which is
highly discouraged, the `self` parameter is a reference to the instance of the
object itself. It allows you to access variables and methods that belong to
that specific object.

3. **Constructing an Object (a.k.a. Instantiating a Class):**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

my_dog = Dog('Lucky', 'Golden Retriever')
friends_dog = Dog('Lucy', 'German Shepherd')

print(my_dog.name, my_dog.breed)  # Output: Lucky Golden Retriever
print(friends_dog.name, friends_dog.breed)  # Output: Lucy German Shepherd
```
As you can see in the example, we're calling the same variable name but we're
getting different outputs, that's because the objects are different. In the
first print function we're printing the `name` attribute of the `my_dog`
object, but in the second print function we're printing the `name` attribute of
the `friends_dog` object.

### Member Variables (Attributes) & Functions (Methods)

1. **Member Variables (Attributes):** These are the pieces of data that belong
to an object. They define its state and characteristics. Each object has its
own version of that variable. In the previous example the `my_dog` object had
`Lucky` as the `name` attribute, but the `friends_dog` object had `Lucy` as the
`name` attribute, same with their `breed` attributes. They're usually defined
in the `__init__` method, using the format in line 1 and accessed with the
format in line 2:
```python
1: self.<attribute_name> = value
2: object_name.<attribute_name>
```

2. **Member Functions (Methods):** These are functions defined inside a class
that perform actions or operations on the object's data. They're essentially
the behavior of the object. All methods always take `self` as their first
parameter, implicitly referring to the object itself, allowing the method to
access the objects own attributes. Let's work on the `Dog` class.
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog('Lucky', 'Golden Retriever')
my_dog.bark()  # method call (just like a function call)
# Output: Lucky says woof!
```

## Properties of OOP

Before we have more fun with examples, there is some terminology that we need
to know. These are the fundamental concepts that define OOP.

### Encapsulation

- **Definition:** Encapsulation means bundling the data (attributes) and the
functions (methods) that operate on that data into a single unit, an object.
In CENG240 languages, hiding implementation/representation details.

A key aspect of this encapsulation is **information hiding**. That means that
the internal working details of an object are hidden from the rest of the code.
You interact with the object only through its defined methods, rather than
directly accessing its internal components.

Imagine you're holding a TV remote. You press buttons `change_channel()`, or
`increase_volume()`. You don't need to know how the TV actually increases the
volume, or switches channels, that complexity is deliberately hidden from you.
You only interact with its public interface.
This abstraction simplifies the interaction, protects data from accidental
corruption, makes code easier to modify without breaking other parts of the
system.

### Inheritance

- **Definition:** Inheritance is a mechanism that allows a new class to inherit
properties (attributes) and behaviors (methods) from an existing class. The
class that *inherits* these is called a **child class** or **derived class**.
The class that gets *inherited* is called **parent class** or **base class**.

This creates a `is-a` relationship between classes. For example a `Car` is a
`Vehicle`, a `Dog` is a `Mammal`, etc.

Inheritance promotes code reusability. You don't have to write the same method
over and over again for closely related classes. You can just write a parent
class, and inherit those methods, which I'll show you how further down the
line.

Inheritance Example:
```python
class Vehicle:
    def __init__(self, current_speed):
        self.current_speed = current_speed

    def accelerate(self, speed):
        self.current_speed += speed
        print(self.current_speed)

class Bike(Vehicle):
    def accelerate(self, speed):
        self.current_speed += 2 * speed  # because bikes are cool
        print(self.current_speed)

class Car(Vehicle):
    def accelerate(self, speed):
        self.current_speed += 0.5 * speed  # because cars are shit
        print(self.current_speed)

class Truck(Vehicle):
    def __init__(self):
        self.current_speed = 0

my_bike = Bike(0)
my_car = Car(0)
my_truck = Truck()

my_bike.accelerate(10)  # Output: 20
my_car.accelerate(10)  # Output: 5
my_truck.accelerate(10)  # Output: 10
```
In this example, you can see that although we've not defined a method named
`__init__()` for `Bike` and `Car` child classes, we could still initiate an
object from them (which would not be the case if we didn't inherit that method
from the `Vehicle` class). Same thing applies for the `Truck` class with the
`accelerate()` method. Although we've not defined it, we were able to call it,
because it's defined in the inherited parent class. If you look closer, you can
see that the alternated version of the method is ran when called. In the `Bike`
class when you accelerate by 10 km/h your current_speed increases by 20 km/h,
in the `Car` class when you accelerate by 10 km/h your current_speed increases
by 5 km/h. This is because we've changed how these worked in the corresponding
child classes.

### Polymorphism

- **Definition:** The word polymorphism refers to the ability of OOP of
different objects to respond to the same method call in their own, appropriate
ways. In CENG240 language, the ability of a child class to behave and appear
like its parent.

You can have a general command, and different types of objects (of different
classes) will execute that specific command to their nature.

**Duck Typing:** Python's approach to polymorphism is often called *duck
typing*: "If it walks like a duck and quaks like a duck, it is a duck.". It
means if an object has the method you're trying to call, Python doesn't care
what type it explicitly is; it will just call that method. No questions asked.

Duck Typing Example from [GeeksForGeeks](https://www.geeksforgeeks.org/python/duck-typing-in-python/):
```python
class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("fish swim in sea")

# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    obj.fly()

"""
Output:
fly with wings
fly with fuel

Traceback (most recent call last):
  File "<python-input-0>", line 16, in <module>
    obj.fly()
    ^^^^^^^
AttributeError: 'Fish' object has no attribute 'fly'
"""
```
As you can see, although the name of the method is exactly the same, since the
class `Bird` and `Airplane` each has a method named `fly`, the script was able
to call for them, no questions asked; however, with the class `Fish`, since
there is no method named `fly`, Python gives an error and says that.

## Message Passing

- **Definition:** In OOP, objects communicate with each other by sending
`messages`. A message is simply a `method call`. The concept is, when an object
calls a method on another object (or even itself), it's considered to be
sending a message. The calling object doesn't explicitly know what the method
it's calling *will* happen, only it *wants* it to happen, by calling the
appropriate method. This concept reinforces encapsulation, promotes coupling,
meaning objects are less dependent on each other's internal sructuer, leading
to more modular and flexible designs.

Message Passing Example:
```python
class Printer:
    def print_document(self, document_name):
        print(f"Printing: {document_name} ...")

class User:
    def __init__(self, name):
        self.name = name

    def send_to_printer(self, printer_object, doc):
        print(f"{self.name} is printing {doc}.")
        printer_object.print_document(doc)  # Message Passing

my_printer = Printer()
me = User('jayshozie')

me.send_to_printer(my_printer, "Report.docx")
# Output:
# jayshozie is printing Report.docx.
# Printing: Report.docx ...
```

## Basics of OOP in Python









