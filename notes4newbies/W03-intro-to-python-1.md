MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

In this markdown, we will start working on Python 3. If you didn't read 
[Week 0 - Preliminary](./W00-preliminary.md), you really should. I've explained
how/where/when to read documentations of programming languages in that. You
will really need it from now on.

-------------------------------------------------------------------------------

# IMPORTANT NOTE 1

This markdown is very long, and it contains way more information than you can
learn in one sitting. I recommend you to read it slowly, understand as much as
you can, and leave the rest of the stuff for now. You can use this markdown as
a reference or a cheat sheet if you will. I will try to make it as up-to-date
as I can, but don't trust it completely. For the most recent information,
always consult to the [documentation](https://docs.python.org/3/) of Python 3,
and try to understand it. It is very well written, and it has a lot of
information that I won't and can't possibly cover in this markdown.

-------------------------------------------------------------------------------

# IMPORTANT NOTE 2

Another thing is that, since these are incredibly foundational in programming,
there is no actual order that they should be studied. These topics are
incredibly intertwined, and should be studied as a whole. Please, if you don't
understand something, continue. Don't stop just because you didn't understand
something, because there is a possibility that it's been explained in a further
section, or you will understand it down the road.

-------------------------------------------------------------------------------

# Data Types in Python

As we've seen, a CPU cannot understand anything other than `integers` and
`floating-point numbers`, also we've seen ways to make a CPU 'understand
strings'. There are 2 main types of data you need to know about: Basic and
Container.

I will give you small assignments at the end of every markdown from now on. You
can find the answers to them in the [solutions](./solutions) directory. I
recommend you to work on them yourself until you are absolutely sure that you
cannot do them, and then looking at the answers. This way you will actually try
to learn how things work.

P.S: In Python, to assign a value (it can be anything) to a variable, you don't
need to specify which type it should be. Python does its best to understand
what you mean, and stores it itself.

## Basic Data Types

Basic data types store actual values. There are some quirks in Python that you
should know, but I will talk about those when it's time.

<details>
    <summary>Integers (int)</summary>

Integers are whole numbers (e.g., 2, 18, 31, 5258489). It can be positive or
negative. In Python, you can change the value of an integer directly by
re-declaring it. Integers in Python, can be of any size. It is not limited by
bit size or anything like that.
```python
x = 3           # The value of 'x' in memory is 3.
print(x)        # Output: 3
print(type(x))  # Output: <class 'int'>
x = 7575        # The value of 'x' in memory went from 3 to 7575.
print(x)        # Output: 7575
print(type(x))  # Output: <class 'int'>
x = -128        # The value of 'x' in memory went from 7575 to -128.
print(x)        # Output: -128
print(type(x))  # Output: <class 'int'>
x = 0           # The value of 'x' in memory went from -128 to 0.
print(x)        # Output: 0
print(type(x))  # Output: <class 'int'>
```
</details>

<details>
    <summary>Floating-Point Numbers (float)</summary>

A float can be any real number, except irrationals we can't completely
represent them, obivously. Floats are in IEEE-754 standard. If the float is
bigger than 32-bits, than it changes it to double (64-bit) float as it is in
IEEE-754 standard.
```python
my_float = 3.14          # The value of 'my_float' in memory is 3.14
print(my_float)          # Output: 3.14
other_float = -1839.421  # The value of 'other_float' in memory is -1839.421
print(other_float)       # Output: -1839.41
```
</details>

<details>
    <summary>Complex Numbers (complex)</summary>

Complex numbers are exactly what they are called. They are complex numbers
directly from mathematics. If you want to store the imaginary part of a complex
number, you must specify it with the character `j`.
```python
my_complex_num = 3+4j         # 'my_complex_num' is 3+4j
print(my_complex_num)         # Output: 3+4j
my_other_complex = -345.324j  # 'my_other_complex' is (-345.324j)
print(my_other_complex)       # Output: (-0-345.324j)
my_other_other_complex = my_complex_num + my_other_complex
print(my_other_other_complex) # Output: (3-341.324j)
print(type(my_complex_num))   # Output: <class 'complex'>
```
</details>

<details>
    <summary>Strings (str)</summary>

These are the strings that we've talked about. A string can be of any value
that can be represented by characters. Python uses UTF-8 by default, but it can
be changed. 
```python
my_name = "Jayshozie"  # Value of 'my_name' is "Jayshozie"
print(my_name)         # Output: Jayshozie
print(type(my_name))   # Output: <class 'str'>
```
</details>

<details>
    <summary>Booleans (bool)</summary>

A bool is a truth value. In every programming language different values have
different 'truthy' values. You only need to know what Python's are, so that's
what I'll give you.
```python
my_bool = True
my_other_bool = False
print(my_bool)         # Output: True
```
These are your default booleans, it can be 'True' or 'False'; however, other
numbers and strings have different truthiness, so to say. Values that evaluate
to 'True' are considered 'Truthy', and values that evaluate to 'False' are
considered 'Falsy'. Here are some examples:
```python
# Falsy Values along with 'False' itself:
x = []        # Empty Lists (we'll get to lists in a minute)
y = ()        # Empty Tuples (we'll get to tuples in a minute)
z = {}        # Empty Dictionaries (we'll get to dictionaries in a minute)
k = set()     # Empty Sets (we'll get to sets in a minute)
l = ""        # Empty Strings
r = range(0)  # Empty Ranges (we'll get to ranges in a different markdown)
# Zero of any numeric type is considered Falsy
x = 0    # Integers
y = 0.0  # Floats
z = 0j   # Complex numbers
# Constants that are considered Falsy
b = None  # None constant is falsy
m = False # False constant is considered Falsy, obviously
```
What we mean by false or true will be way more clear in the conditionals
section. Anything other than these are considered 'Truthy' and would evaluate
to 'True'.

<details>
    <summary>Weird Thing as Extra Information</summary>

```python
x = "False"  # Evaluates to 'True' because it's a non-empty string. What it
             # holds doesn't matter.
```
</details>
</details>

## Container Data Types

These are containers, as in they contain other values. It will be more clear
after learning about them, but before we learn about them we need to learn a
concept in programming called 'mutability'. It's basically whether the value of
a variable (it can be a container or a basic data type) can be changed or not.
We'll see examples of it in a minute. There are some 'methods' you need to
learn with containers, I will give them when you need them.

<details>
    <summary>Lists (list)</summary>

A list is a mutable 'list' of values, also called a sequence. It is ordered,
meaning that the order of the elements matter. A list can hold any value you
want to store, such as integers, floats, strings, and even other lists, tuples,
or dictionaries.
```python
# Let's create a list object.
my_list = []  # This creates an empty list with no values in it.
my_list.append(13)
# This will 'append' (add as the last element) 13 to the list
print(my_list)  # Output: [13]
# Let's append another value.
my_list.append("hi")
# This will append the string "hi" to the list as a separate element.
print(my_list)  # Output: [13, "hi"]
```

You can access items in a list with it's index number. In most programming
languages, including Python, we start counting from 0. We've talked about why
in the previous markdown.
```python
print(my_list[0])  # Output: 13
print(my_list[1])  # Output: "hi"
```

Lists are very useful, since Python doesn't have a way of storing arrays. You
can nest lists, meaning you can store lists inside of lists, so on and so on.
```python
# Since Python doesn't have arrays, we can store a 2x2 matrix like this
my_array = [[1,2],[3,4]]

# That `array` is still a list. It's first element, a.k.a. index 0, is the list
# [1, 2].
print(my_array[0])  # Output: [1, 2]

# If you want to access an item in that list you can do;
print(my_array[0][1])  # Output: 2
```

There are some very important methods that you need to know with lists.

### [Important Operations with Lists](https://docs.python.org/3/tutorial/datastructures.html)

1. `append()`

We've seen this method. It takes an argument, and adds that element to the
list. It always adds the item to the end of that list.
```python
my_list = ["This string was in my list."]
print(my_list)  # Output: ["This string was in my list."]

my_list.append("I've just appended this string to my list!")
print(my_list)  # Output: ["This string was in my list.", "I've just append this string to my list!"]
```

2. `pop()`

The `pop()` method takes an optional argument, which should be an index. You
don't have to provide it. If you don't the method will remove the last item
from the list.
```python
my_list = [0, 1, 2, 3, 4]
my_list.pop()
print(my_list)  # Output: [0, 1, 2, 3]

# You can also store that value if you want.
number_three = my_list.pop(-1)
# You can also negatively index lists, meaning index -1 is the last item in a
# list. It's 3 in our case.

print(number_three, my_list)  # 3 [0, 1, 2]
```

3. `clear()`

I believe it's pretty clear what this method does. Pun intended. It clears out
the list, meaning it deletes all values stored in. Resulting list is an empty
list.
```python
lemme_clear_this = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lemme_clear_this.clear()
print(lemme_clear_this)  # Output: []
```

4. `extend()`

The `extend()` method takes a list or tuple as argument, and adds the items in
that list/tuple to the given list.
```python
lemme_extend_this = [0, 1, ["random", "values"], 2]
to_this = [4, 5, "even", ["more", "random values"]]

lemme_extend_this.extend(to_this)

print(lemme_extend_this)  # Output: [0, 1, ['random', 'values'], 2, 4, 5, 'even', ['more', 'random values']]
```

5. `insert()`

The `insert(index, item)` method takes an index and an item (can be anything
that can be stored in a list) and adds that item to the desired index.
```python
gonna_insert_2_this = [0, 1, 3, 4]
gonna_insert_2_this.insert(2, "2")

print(gonna_insert_2_this)  # Output: [0, 1, '2', 3, 4]
# If you look carefully, in the index 2, we don't have the number 2 stored,
# what we stored is a string that has the character 2 in it.
```

6. `remove()`

The `remove()` method takes an argument, looks for that value in the list and
removes it if it finds it. It only removes the first item it finds.
```python
random_bs_go = [0, 1, 0, 3, 4, 5]

random_bs_go.remove(0)

print(random_bs_go)  # Output: [1, 0, 3, 4, 5]
# See? It didn't remove the second 0.
```

7. `index()`

The `index()` method takes an argument, looks for it in the list, returns the
first match's index.
```python
this_is_getting_weird = [0, 0, 1, "really"]

index_of_really = this_is_getting_weird.index("really")

print(index_of_really)  # Output: 3
```

8. `count()`

The `count()` method takes an argument, looks at the list, returns how many
copies of that values are there.
```python
very_much = [0, 0, 1, 2, 3, 4]

how_much_zeroes = very_much.count(0)

print(how_much_zeroes)  # Output: 2
```

9. `sort()`

It's pretty basic. It sorts the list. If you don't provide it with a way of
sorting it's going to assume for the best, and sort it according to the values.
```python
unsorted_list = [7, 93, 24, 1, 0, 73722]

unsorted_list.sort()

print(unsorted_list)  # Output: [0, 1, 7, 24, 93, 73722]
```
Here is what else you can do with the `sort()` method. Formal definition of the
method is;
`sort(*, key=None, reverse=False)`
Don't worry, it's not that complicated. The asterisk (\*) means it doesn't
accept any argument other than keyword arguments, meaning you can't give it any
arguments other than `key` or `reverse`. The `sort()` function only uses `<`
comparisons in between items, meaning that if the sort fails at any point, then
your list may be jumbled up.

Let's see what those keyword arguments do.

```python
# Maybe you want to reverse the order of the list
my_reverse_ordered_list = [0, 7, 5, 9, 5, 7, 9]
my_reverse_ordered_list.sort(reverse=True)
print(my_reverse_ordered_list)  # Output: [9, 9, 7, 7, 5, 5, 0]

# Or you want to specify a key, meaning that you want to sort the list in a
# different way. Let's say you have a nested list, and you want to sort it with
# respect to it's items in index[1]
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# Since we haven't talked about lambda functions yet, I'm gonna do it with a
# normal function

def return_grade(student):
    return student[2]
# This function takes an argument, and returns the 2nd (starting from 0) item

student_tuples.sort(key=return_grade, reverse=True)
# Let's also reverse it so that we have the highest grading student first.
print(student_tuples)  # Output: [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```
The `key` keyword argument takes basically a function that takes in a single
argument and returns a key to use for sorting purposes.

<details>
    <summary>Formal Definition of the key Keyword Argument for Nerds</summary>

The value of the key parameter should be a function (or other callable) that
takes a single argument and returns a key to use for sorting purposes. This
technique is fast because the key function is called exactly once for each input
record.
</details>

<details>
    <summary>A Better Version of the Previous Example for Nerds</summary>

```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

student_tuples.sort(key=lambda student: student[2], reverse=True)

print(student_tuples)
```
This is the recommended, and more Python-y way of sorting that list. We will
visit the lambda functions topic after we talk about functions.
</details>

And that concludes our important methods of lists.
</details>

<details>
    <summary>Tuples (tuple)</summary>

A tuple is an immutable, ordered sequence. Immutable, as in you cannot change
anything in it after you construct it. That means you also cannot use the
method `append()`, because it doesn't exist.
```python
my_tuple = ()  # This creates an empty tuple with no values in it.
my_tuple.append(34)
```
This line should give an error that says something like;
```python
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    my_tuple.append(34)
    ^^^^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append'
```
Don't be scared, it just says that it doesn't understand what `append` means in
this context. This happens because you can't `append` something to a tuple, it
just simply doesn't exist. You should add the values you want to store in a
tuple at the initiation.
```python
my_other_tuple = (2, 3, 5, 7, 11)
print(my_other_tuple)  # Output: (2, 3, 5, 7, 11)
```
After you create that tuple, you can't change anything in it, that's why it's
called immutable.

There are some important methods with tuples, too.

### [Important Operations with Tuples](https://docs.python.org/3/tutorial/datastructures.html)

1. `count()`

This is the same method with the `count()` method in lists.
```python
how_many_yes = ("yes", 10, 20, "yes", "yes")

how_many_tho = how_many_yes.count("yes")

print(how_many_tho)  # Output: 3
```

2. `index()`

This is the same method with the `index()` method in lists.
```python
my_tuple = ["my name", "is not", 30]
index_of_30 = my_tuple.index(30)

print(index_of_30)  # Output: 2
```

And this concludes our important methods with tuples.

</details>

<details>
    <summary>Dictionaries (dict)</summary>

A dictionary (dict) is a mutable and unordered mapping type. In a dictionary,
you store `values` associated with a `key`.
```python
my_dict = {'name': 'Ayse', 'age': 34, 'education': 4}
print(my_dict)  # Output: {'name': 'Ayse', 'age': 34, 'education': 4}
print(type(my_dict))  # Output: <class 'dict'>
```

<details>
    <summary>Important Operations with Dictionaries</summary>

There are a lot of stuff associated with dictionaries, so I've felt the need to
make this section a drop-down. You don't need to know every single one of these
with immense detail, but it would make your life real easier. For more info,
please check the [documentation](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict).

1. `list(d)`

This function takes a dictionary 'd' as argument, and returns a list of its
keys.
```python
my_dict = {"name": "jay", "age": 20, "cgpa": 4.00}
# that cgpa is a lie lol

print(list(my_dict))  # Output: ['name', 'age', 'cgpa']
```

2. `len(d)`

This function takes a dictionary 'd' as argument, and returns the number of
items in 'd'.
```python
random_bs_go = {'one': 42, 'three': 3, 'four': 4, 'two': None}

print(len(random_bs_go))  # Output: 4
```

3. `d[k]`

Returns the item of 'd' with key 'k'. If the key 'k' is missing, then it raises
"KeyError" error.
```python
random_bs_go = {'one': 42, 'three': 3, 'four': 4, 'two': None}

print(random_bs_go['one'])  # Output: 42

print(random_bs_go['name'])
# Output:
# Traceback (most recent call last):
#   File "<python-input-3>", line 1, in <module>
#     print(random_bs_go['name'])
#           ~~~~~~~~~~~~^^^^^^^^
# KeyError: 'name'
```

4. `d[k] = value`

Sets `d[k]` to `value`.
```python
random_bs_go = {'one': 42, 'three': 3, 'four': 4, 'two': None}

random_bs_go['one'] = 100

print(random_bs_go['one'])  # Output: 100
```

5. `k in d`

This is more of a logic thing and not exclusive to dictionaries, but basically
returns `True` if the dictionary 'd' has a key 'k'.
```python
random_bs_go = {'one': 42, 'three': 3, 'four': 4, 'two': None}

print('one' in random_bs_go)  # Output: True

# You can combine it with 'not'.
print('five' not in random_bs_go)  # Output: True

print('one' not in random_bs_go)  # Output: False
```

<details>
    <summary>A Different Example</summary>

```python
student = {'name': 'ahmet yilmaz', 'age': 20, 'cgpa': 2.98}

if 'age' in student:
    print(student['age'])
```
</details>

6. `clear()`

This is a method that clears all items in a dictionary, works almost exactly
the same as the list method.
```python
my_dict = {'name': 'Ayse', 'age': 34, 'education': 4}
my_dict.clear()
print(my_dict)  # Output: {}
```

7. `get(key, default=None)`

Returns the value for 'key' if the 'key' is in the dictionary, returns None as
default if not. Default can be changed by the argument `default`.
```python
my_dict = {'name': 'Ayse', 'age': 34, 'education': 4}
print(my_dict.get('name'))  # Output: Ayse
print(my_dict.get('surname'))  # Output: None

print(my_dict.get('surname', 'No such key!'))  # Output: No such key!
```

8. `items()`

Returns a view object that displays a list of a dictionary's key-value tuple
pairs.
```python
my_dict = {'name': 'Ayse', 'age': 34, 'education': 4}
print(my_dict.items())  # Output: dict_items([('name', 'Ayse'), ('age', 34), ('education', 4)])
```

9. `keys(key, [, default])`
Returns a view object that displays a list of all the keys in the dictionary.
```python
my_dict = {'name': 'Ayse', 'age': 34, 'education': 4}
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'education'])
```

10. `popitem()`
This method removes the last inserted key-value pair from the dictionary and
returns it as a tuple. If the dictionary is empty, it raises a KeyError. It
works almost exactly the same as the `pop()` method in lists, except that, you
can specify which item to pop from a list. You can't do it here. It always
works as LIFO (last-in first-out).
```python
my_dict = {'name': 'Ayse', 'age': 34, 'education': 4}
print(my_dict.popitem())  # Output: ('education', 4)
print(my_dict)  # Output: {'name': 'Ayse', 'age': 34}
```
</details>
</details>

<details>
    <summary>Sets (set, frozenset)</summary>

There are two types of sets, one type is mutable and other type is immutable.
The mutable set type is just called a `set`, the immutable type is called
`frozenset`. Sets are unordered, and they do not record element position or
order of insertion. Accordingly, sets do not support indexing, slicing, or
other sequence-like behavior. Sets are mostly used for membership testing,
removing duplicates from a sequence, and computing mathematical operations such
as intersection, union, difference, and symmetric difference.

Example:
```python
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4, 5})
```

### [Important Operations with Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

I will tell you which method can be use with which type of set.

1. `add()`

This method adds an element to the set. It only works with mutable sets, not
with frozensets.
```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

2. `clear()`

This method removes all elements from the set. It only works with mutable sets,
not with frozensets.
```python
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)  # Output: set()
```

3. `difference()`

This method returns a new set with elements in the first set that are not in
the second set. It works with both mutable and immutable sets.
```python
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}
my_difference = my_set1.difference(my_set2)
print(my_difference)  # Output: {1, 2}
# Note: This method only returns the items that are in the first set that are
# not in the second set. It does not return items that are in the second set
# that are not in the first set.

# You can also use the `-` operator to achieve the same result.
same_difference_diff_variable = my_set1 - my_set2
print(same_difference_diff_variable)  # Output: {1, 2}
```

4. `intersection()`

This method returns a new set with elements that are common to both sets. It
works with both mutable and immutable sets.
```python
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}
my_intersection = my_set1.intersection(my_set2)
print(my_intersection)  # Output: {3, 4, 5}

# You can also use the `&` operator to achieve the same result.
same_intersection_diff_variable = my_set1 & my_set2
print(my_intersection)  # Output: {3, 4, 5}
```

5. `isdisjoint()`

This method returns `True` if two sets have no elements in common, otherwise
it returns `False`. It works with both mutable and immutable sets.
```python
my_set1 = {1, 2, 3}
my_set2 = {4, 5, 6}
print(my_set1.isdisjoint(my_set2))  # Output: True
my_set3 = {2, 3, 4}
print(my_set1.isdisjoint(my_set3))  # Output: False
```

6. `issubset()`

This method returns `True` if all elements of the first set are in the second
set, otherwise it returns `False`. It works with both mutable and immutable
sets.
```python
my_set1 = {1, 2, 3}
my_set2 = {1, 2, 3, 4, 5}
print(my_set1.issubset(my_set2))  # Output: True
my_set3 = {1, 2, 6}
print(my_set1.issubset(my_set3))  # Output: False

# You can also use the `<=` operator to achieve the same result.
same_issubset_diff_variable = my_set1 <= my_set2
print(same_issubset_diff_variable)  # Output: True
```

7. `issuperset()`

This method returns `True` if all elements of the second set are in the first
set, otherwise it returns `False`. It works with both mutable and immutable
sets.
```python
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {1, 2, 3}
print(my_set1.issuperset(my_set2))  # Output: True
my_set3 = {1, 2, 6}
print(my_set1.issuperset(my_set3))  # Output: False

# You can also use the `>=` operator to achieve the same result.
same_issuperset_diff_variable = my_set1 >= my_set2
print(same_issuperset_diff_variable)  # Output: True
```

8. `symmetric_difference()`

This method returns a new set with elements in either the first or second set,
but not both. It works with both mutable and immutable sets.
```python
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}
my_symmetric_difference = my_set1.symmetric_difference(my_set2)
print(my_symmetric_difference)  # Output: {1, 2, 6, 7}

# You can also use the `^` operator to achieve the same result.
same_symmetric_difference_diff_variable = my_set1 ^ my_set2
print(same_symmetric_difference_diff_variable)  # Output: {1, 2, 6, 7}
```

9. `union()`

This method returns a new set with all elements from both sets. It works with
both mutable and immutable sets.
```python
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}
my_union = my_set1.union(my_set2)
print(my_union)  # Output: {1, 2, 3, 4, 5, 6, 7}

# You can also use the `|` operator to achieve the same result.
same_union_diff_variable = my_set1 | my_set2
print(same_union_diff_variable)  # Output: {1, 2, 3, 4, 5, 6, 7}
```

10. `update()`

This method updates the first set with elements from the second set. It only
works with mutable sets, not with frozensets.
```python
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5, 6, 7}
my_set1.update(my_set2)
print(my_set1)  # Output: {1, 2, 3, 4, 5, 6, 7}

# You can also use the `|=` operator to achieve the same result.
my_set1 |= my_set2
print(my_set1)  # Output: {1, 2, 3, 4, 5, 6, 7}
```

You can check the rest of the methods in the
[documentation](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).

</details>

-------------------------------------------------------------------------------

# Useful Operations

<details>
    <summary>w/ Numerical Types</summary>

## [`type(<data>)`](https://docs.python.org/3/library/functions.html#type)

I've used this function when I was talking about types. What the function does
is basically return the type of a variable.

```python
x = 1.345
print(type(x))  # Output: <class 'float'>

a = "Hello, World!"
print(type(a))  # Output: <class 'str'>
```

## [`abs(<number>)`](https://docs.python.org/3/library/functions.html#abs)

This function takes in a numerical value, complex numbers too, and return its
absolute value.

In the case of complex numbers, its magnitude is returned.

Example Use:
```python
x = abs(-1243.424)
print(x)  # Output: 1243.424

comp_num = -3-4j
print(abs(comp_num))  # Output: 5
```

## [`pow(<base>, <exponent>)`](https://docs.python.org/3/library/functions.html#pow)

This function takes 2 numerical arguments. First one is the base, and second
one is the exponent. It does the calculation, `x^y`. Same can be accomplished
with `x**y`. Arguments must be numerical values.

Weird Quirk: pow(0,0) = 1

Example Use:
```python
x = 2
y = 4
print(pow(x,y))  # Output: 16
```

## [`round(<float>)`](https://docs.python.org/3/library/functions.html#round)

The argument value is rounded to the closest multiple of 10 to the power minus
ndigits; if two multiples are equally close, rounding is done toward the even
choice (banker's rounding).

Example Use:
```python
x = 2.5
y = 1.5
z = 0.5

round_x = round(x)
round_y = round(y)
round_z = round(z)

print(round_x, round_y, round_z)
# Output: 2 2 0
```

## `sin()`, `cos()`, `log()` from the [`math`](https://docs.python.org/3/library/math.html) Library

These three functions are from the `math` library, thus the library must be
included before their use. They are the sine, cosine, and logarithm functions
in maths. They take their arguments in radians (rad).

The base of the logarithm function is `e` as default, but it can be changed by
providing as a separate argument separated by a comma ','.

Example Use:
```python
from math import sin, cos, log
# You can use `import math` but it has a lot of functions, it's bad practice to
# load an entire library if you're going to use just a couple of things.

sin_of_pi = sin(pi)
cos_of_pi = sin(pi)
log10_of_10 = log(10, 10)

print(sin_of_pi, cos_of_pi, log10_of_10)
# Output:
# 1.2246467991473532e-16 -1 1
```
</details>


<details>
    <summary>w/ Strings</summary>

## `str()`

`str()` function takes a single argument, returns the string version of the
value given as argument.

Example Use:
```python
x = 13
y = "My number: "

# If you try to 'add' these two values, Python will scream at you, since they
# are not of the same type, they can't be added.

print(y + str(x))  # This won't scream at you.
# Output: My number: 13
```

## `len()`
Example Use:
```python

```

## `eval()`
Example Use:
```python

```
</details>


<details>
    <summary>w/ Dictionaries</summary>

## `len()`
Example Use:
```python

```

## `values()`
Example Use:
```python

```

## `keys()`
Example Use:
```python

```
</details>

-------------------------------------------------------------------------------

# Expressions in Python

## Presedence and Associativity

> The combination of values, variables, operators, and function calls is termed
as an expression. The Python interpreter can evaluate a valid expression.

Direct Quote from:
[Programiz](https://www.programiz.com/python-programming/precedence-associativity)[^1]

<details>
    <summary>Precedence and Associativity Table (basic)</summary>

| Precedence |                   Operators                  |                     Description                     | Associativity |
|:----------:|:--------------------------------------------:|:---------------------------------------------------:|:-------------:|
|      1     |                      ()                      |                     Parantheses                     | Left to right |
|      2     |                      \**                     |                    Exponentiation                   | Right to left |
|      3     |                  +x, -x, ~x                  |           Positive, negative, bitwise NOT           | Left to right |
|      4     |                  \*, /, //, %                | Multiplication, division, floor division, remainder | Left to right |
|      5     |                     +, -                     |               Addition and subtraction              | Left to right |
|      6     |                    <<, >>                    |                        Shifts                       | Left to right |
|      7     |                       &                      |                     Bitwise AND                     | Left to right |
|      8     |                       ^                      |                     Bitwise XOR                     | Left to right |
|      9     |                      \|                      |                      Bitwise OR                     | Left to right |
|     10     | in, not in, is, is not, <, <=, >, >=, !=, == |    Comparisons, Membership Tests, Identity tests    | Left to right |
|     11     |                     not x                    |                     Boolean NOT                     | Right to left |
|     12     |                      and                     |                     Boolean AND                     | Left to right |
|     13     |                      or                      |                      Boolean OR                     | Left to right |
|     14     |                      and                     |                     Boolean AND                     | Left to right |

</details>

For example:
```python
>>> 5 - 7
-2
```
There is no ambiguity there; however, if we were to do this:
```python
>>> 10 - 7 * 3
```
Without precedence, Python wouldn't be able to understand which operator should
be done first. We're lucky that we do have it.
```python
>>> 10 - 7 * 3
-11
```

What if there are two operators that have the same precedence? That's where
associativity comes in. If there are two or more operators with the same
precedence, then Python checks the associativity of those operators.
```python
>>> 3 * 4 / 4
3
```
Python interpreter reads the operators from left to right in this case. There
may be some operators that you don't know in there, don't worry you'll
understand them in about 3-4 markdowns.

<details>
    <summary>Precedence and Associativity Table (detailed)</summary>

| Precedence |                   Operators                  |                         Description                         | Associativity |
|:----------:|:--------------------------------------------:|:-----------------------------------------------------------:|:-------------:|
|      1     |                      ()                      |                         Parantheses                         | Left to right |
|      2     |            x[index] x[index:index]           |                     Subscription Slicing                    | Left to right |
|      3     |                    await x                   |                       Await expression                      |      N/A      |
|      4     |                      \**                     |                        Exponentiation                       | Right to left |
|      5     |                  +x, -x, ~x                  |               Positive, negative, bitwise NOT               | Left to right |
|      6     |                \*, @, /, //, %               | Multiplication, matrix, division, floor division, remainder | Left to right |
|      7     |                     +, -                     |                   Addition and subtraction                  | Left to right |
|      8     |                    <<, >>                    |                            Shifts                           | Left to right |
|      9     |                       &                      |                         Bitwise AND                         | Left to right |
|     10     |                       ^                      |                         Bitwise XOR                         | Left to right |
|     11     |                      \|                      |                          Bitwise OR                         | Left to right |
|     12     | in, not in, is, is not, <, <=, >, >=, !=, == |        Comparisons, Membership Tests, Identity tests        | Left to right |
|     13     |                     not x                    |                         Boolean NOT                         | Right to left |
|     14     |                      and                     |                         Boolean AND                         | Left to right |
|     15     |                      or                      |                          Boolean OR                         | Left to right |
|     16     |                    if-else                   |                    Conditional expression                   | Right to left |
|     17     |                    lambda                    |                      Lambda expression                      |      N/A      |
|     18     |                      :=                      |           Assignment expression (walrus operator)           | Right to left |
</details>

## Logic in Python

If you took a logic course at any point in your education this should be really
easy for you, because it's basically the same thing. For example, let's say
that you have a program that serves as a calculator. It's just in its first
version so you didn't implement any functionality other than addition, but you
did implement a way for the user to specify which action they want to take. You
can check whether they are trying to add numbers by logic.
```python
num1 = eval(input("Please enter the first number: "))
num2 = eval(input("Please enter the second number: "))
operator = eval(input("Please enter an operator (+,-,*,/): "))

if operator == '+':
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

else:
    print(f"An unexpected error, ocurred.")
```
In this example, Python checks whether the user provided the string "+" as
input for the operator variable.

There are more logic checks that can be used in Python, let me go over some of
them.
```python
# You could check for multiple things in a single logic check.

num1 = eval(input())
num2 = eval(input())
operator = eval(input())

if (operator == '+' and
    isinstance(num1, (int,float)) and
    isinstance(num2, (int,float))):
    """
    Let's talk about this entire check. We know what the first one does, it
    checks whether the variable operator is some string, but what about others?
    There is an `and` operator in between all of them. Which means, for this
    entire statement to be `True`, all of them must be `True`. The second check
    is a function called `isinstance()` from the standard library of Python. It
    returns `True` if the provided object's (num1 in our case) type is one of
    the given. Usually it's used with a single type, but in this case, we can
    use two. In that case those must be provided in a `tuple`, we learned what
    that is. That means, if num1 or num2 is not either an integer or a float,
    the program will skip that if block, and continue with the else block. The
    else block can't check for anything, that's by design. If you want to check
    for other stuff in the same conditional block, you should use `elif`
    keyword. So, second and third checks are checking whether the user provided
    numerical values for both of the variables. If they didn't then the script
    will print "An unexpected error ocurred.".

    Then, in the best case scenario, that check sums up to `True and True and
    True`, meaning it is `True`.
    """

    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

else:
    print("An unexpected error ocurred.")
```

<details>
    <summary>Why check that extensively?</summary>

Programming 101: Always expect the worst case scenario. The user may provide a
string for the numerical values, or can leave it empty instead of numericals.
If we don't check for that, and the user gives a string for the first numerical
value and a numerical value for the second one, then when we try to add them
together the Python interpreter will give an error. We do not want that. Even
if there is an error, we want to be the ones that give the error, not the
interpreter. So, we check if both numerical inputs are actually numerical
values, then we check whether the operator is the one we want. After being sure
that all those are true, then we do our calculation and provide the user with
the result.
</details>

## Type Conversion

### Implicit Type Conversion

In certain situations, Python automatically converts the type of your
variables;
```python
my_int = 134
print(my_int, type(my_int))  # Output: 134 <class 'int'>

my_int = 13.4
print(my_int, type(my_int))  # Output: 13.4 <class 'float'>

# 'my_int' is still the same variable, but its type and value has changed,
# because we reassigned it.
```
This type of type conversion is called implicit, because you don't actually
specify which type you're converting to, and leave that decision to the Python
interpreter. Python interpreter avoids data loss in implicit type conversion.

### Explicit Type Conversion (a.k.a. Type Casting)

You can also explicitly change the type of a variable with some functions. In
this case, data loss can occur, since we're forcing it to another type.
```python
my_num = 13
my_num = str(my_num)  # You can re-assign variables.

print(my_num, type(my_num))  # Output: 13 <class 'str'>

my_float = 13.7
my_float = int(my_float)

print(my_float, type(my_float))  # Output: 13 <class 'int'>
# As you can see we've lost the precision of a float since we forced it into
# becoming an integer.
```

-------------------------------------------------------------------------------

# Statements

## Basic Statements

### Assignment Statements

Assignment statements (assignments) are used to give a name (a variable) to a
value or a result. They "bind" a name to an object in memory. They always
involve the `=` operator (a.k.a. the assignment operator). They perform an
action of storing a value, and do not produce a result that can immediately be
used by another part of the code, meaning you can't assign and use an object in
the same line of code. We've used these a lot up until this point, but it's a
good time to give it a name.
```python
x = 20
name = "jay"
y = 243424.4324324
my_dict = {"random": "bs", "go": True}

my_tuple = ("maybe", "randomness", "was")
my_list = ["the friends", "we", "made along", "the way"]
```
Above examples are all assignments. The so-to-say name before the assignment
operator `=` is the name of the variable, the rest in what you assigned to that
variable.

### Expression Statements

Expression statements (expressions) differ from assignment a lot, even though
they look awfully similar. Expressions are used to evaluate something. They
represent a piece of data that can be "resolved" into something. They consist
of expressions, and produce a value. Unlike assignments, this value can be used
immediately, even in the same line. We've also seen a lot of these. Expressions
don't make sense on their own, they need to be paired up with other things.
```python
10
"Hello, world!"
5 + 3
x * 2
len("Python")
```
If you write these to the Python interpreter one by one, it should either
return the value back, or give an error in the 4th line (x * 2) since we
haven't actually 'assigned' a value to a variable called 'x', so Python doesn't
know what we're talking about.

### Clearing Confusions

```python
x = 5 * 3
```
The `5 * 3` part is an expression, and the entire line is an assignment. You
want Python to resolve that 'expression' `5 * 3` and 'assign' it to a variable
named `x`.

```python
if x > 5:
    print(x)
```
The `x > 5` part is an expression, and the entire line is a conditional
expression. In that line, we want Python to resole tha expression `x > 5`, and
if the answer to that expression (check) is `True`, than we want it to do
whatever is after that check (indented code block).

## Compond Statements

> Compound statements contain (groups of) other statements; they affect or
control the execution of those other statements in some way. In general,
compound statements span multiple lines, although in simple incarnations a
whole compound statement may be contained in one line.

Direct Quote from:
[Python Documentation](https://docs.python.org/3/reference/compound_stmts.html)

To simplify things, they are basically a compilation of the basic statements we
have just seen, with a bit of extra stuff.

### Conditional Statements

If you remember the [W02](./W01-intro.md) markdown, we've talked about an
operation type called conditionals. Now we're going to learn what do they
actually mean and how are they constructed.

Conditionals are, basically, conditions that we need the computer to check and
act accordingly. They are one of the foundations of programming, and without
conditionals it would be incredibly hard to code, because you would need to
exactly know what will happen, and sometimes it's not even possible.

Let's see a very basic example of a conditional.
```python
val = eval(input())  # We are asking the input of the user.

if val == "Hi":  # We're checking whether the user said "Hi". If yes,
    print("Hi")  # we do this.
elif val == "Hello": # If the user did not say "Hi", but said "Hello", then
    print("Hello")  # we say "Hello".
else:  # If the user did not say "Hi" or "Hello", we say
    print("Ready")  # "Ready"
```
In Python, you have 3 different check tools, so-to-say. You always start with
an 'if' case, because that's the syntax (how the code should be written,
otherwise the Python interpreter won't understand what is happening and scream
at you). Then, if you need to check for another case, you should use 'elif',
standing for 'else if', and another condition. If you don't provide another
condition with the 'elif' case Python interpreter will, again, scream at you,
because it doesn't know what to check for. After every check you want is done,
we have the 'else' case. It's basically the last resort, if every other check
has failed, then the Python interpreter will run the code you have written in
that block. A side note, you don't need to provide an 'elif' or 'else' case,
they're not forced, but optional.
```python
usr_age = int(input())  # We take an input from the user and store it as int

if usr_age >= 18:  # Check whether the usr_age is greater than or equal to 18
    print("User is an adult, they can enter.")  # if yes, do this
else:  # If not (all other checks failed)
    print("User is not an adult, they cannot enter.")  # do this
```

<details>
    <summary>An Example with Only an if Case</summary>

```python
val = int(input())

if val >= 0:
    print("Positive number.")
```

I know it doesn't make much sense, but I couldn't think of another example.
</details>


<details>
    <summary>Some Formatting of Python in Conditional Statements</summary>

If you wish to continue with your Python journey outside of this course, I
highly recommend you to check out [PEP8](https://peps.python.org/pep-0008/).
PEPs are basically guidelines to how to write Python styled code. There are
some standards that you should follow while writing Python code. PEPs give you
those standards. [PEP8](https://peps.python.org/pep-0008/) is a good starting
point, in my opinion.

Even if you won't please read the rest of this dropdown.

If we go back to our main subject, there are some stuff that you should know
about how to construct conditionals.

### `if a_true_condition == True:`

If you are checking for the truthines of something, do not say check with True
instead just leave it as is.

Do:
```python
if some_bool: ...
```
Don't:
```python
if some_bool == True: ...
```

### `if some_really_long_condition and some_other_really_long_condition and some_other_other_really_long_condition:`

If the stuff you're checking in the if statement is too long (80 characters to
be precise), you should put the checks in parantheses and go into a new line:

Do:
```python
if (some_really_long_condition and
    some_other_really_long_condition and
    some_other_other_really_long_condition):
    ...
```
Don't:
```python
if some_really_long_condition and some_other_really_long_condition and some_other_other_really_long_condition: ...
```

### `if not foo is None:`

If you're checking for something is not None type, use `is not` operator.

Do:
```python
if foo is not None: ...
```
Don't:
```python
if not foo is None: ...
```

### `if foo[:3] == "bar":`

Use `''.startswith()` and `''.endswith()` functions instead of slicing to
check for prefixes or suffixes.

Do:
```python
if foo.startswith('bar'): ...
```
Don't:
```python
if foo[:3] == 'bar': ...
```

### `if type(foo) is type(bar):`

If you're checking for the type of an object, use `isinstance()` instead of
comparing types directly.

Do:
```python
if isinstance(foo, bar): ...
```
Don't:
```python
if type(foo) == type(bar): ...
```
Worse:
```python
if type(foo) is type(bar): ...
```

### `if len(seq):`

For sequences, (strings, lists, tuples), use the fact that empty sequences are
false.

Do:
```python
if seq: ...
if not seq: ...
```
Don't
```python
if len(seq): ...
if not len(seq): ...
```
</details>

-------------------------------------------------------------------------------

### Repetition Statements

Sometimes, you want to repeat a block of code multiple times. For example, you
want to print a statement 5 times, you can do;
```python
print("some statement that i want the user to see")
print("some statement that i want the user to see")
print("some statement that i want the user to see")
print("some statement that i want the user to see")
print("some statement that i want the user to see")
```
This sure will work. It will print that exact statement 5 times, but what if
you want to change what you want to say, or maybe you want them to differ from
one another? What can you do? That's when repetition statements come in.
```python
for i in range(5):
    print("some statement that i want the user to see")
```
This will do the exact same thing, it will print that line 5 times, and if you
want to change the thing you want to print, you can just do it once and it will
just work. Also in the first example, there is a problem. OK, it is easy to
check whether you did everything right with 5 lines of code, but what if it was
50, or 500, or maybe even 5000 lines of code. Then we'll run into a problem.
You will definitely miss something, and it'll become incredibly hard to debug.

#### The `for` Statement

`for` loops are mostly used in iterations where you know how long the entire
iteration will take. For example, in our first example, we know that it should
happen 5 times. It's better to use a `for` loop in that case, since we know it
ahead of time. Here is the official syntax of `for` loop:
```markdown
for_stmt ::= "for" target_list "in" starred_list ":" suite
             ["else" ":" suite]
```
[The for Statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)

I know it looks complicated, but it actually isn't. What it says is, you put
the keyword `for` first, then a `target_list`, and a `starred_list`. A
`target_list` list is any iterable variable, mostly integers, it's `i` in our
example. Then you need to provide a `starred_list`, it should be an iterable
object, such as ranges, lists, etc. An iterable object is any Python object
capable of returning its members one at a time, permitting it to be iterated
over a loop. Lists are a perfect candidate for this type of operation.

#### The `while` Statement

`while` loops are used when you don't know how many iterations it'll take, but
they can be used interchangeably. For example, if you want to check if the user
provided the correct password, you don't know how many times they will enter
the wrong password, so it's best to use a `while` loop in that case. Here is
the offical syntax of `while` loop:
```markdown
while_stmt ::= "while" assignment_expression ":" suite
               ["else" ":" suite]
```
[The while Statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

Again, I know it looks complicated, but it really isn't. It just says that, you
need to put the keyword `while`, then you put an `assignment_expression`,
meaning that you state something, such as `i < 6`, and want that block of code
to be executed until that statement is `False`. Get it? You check for
something, and it happens `while` it's True. We can write the exact same
program as a while loop.
```python
i = 0
while i < 6:
    print("some statement that i want the user to see")
    i += 1
    # This is just a shorthand for `i = i + 1`.
    # There are other example like `i -= 1` or `i *= 2`, they're pretty
    # intuitive, but we will get to them later anyway.
```

-------------------------------------------------------------------------------

# Assignment 1 of W03

Write a Python program that takes 2 values as input, adds them, and prints the
result. Create a Python file, naming doesn't matter but for convention you can
use `W03-assignment.py`. Write your code in it, and run it with Python. If you
don't have Python installed on your computer you can use
[CS50's](https://cs50.dev) online coding environment built on top of Visual
Studio Code. I recommend for you to install
[Python](https://www.python.org/downloads/) and
[Visual Studio Code](https://code.visualstudio.com/) to your PC. This will help
you a lot, since you will be able to reuse a lot of stuff. Check the markdown
named
[W03 How to Install Python and VSCode](./W03--how-to-install-python-and-vscode.md)
for more info.
If you like to have even more pain than CS50's online IDE, you can use
[Google Colab](https://colab.research.google.com/). It's incredibly cramped,
but if you don't want to install anything and just want to pass the course it
should be enough.

Hints:
1. You can use the function `eval(input())` to get input from the user.
2. You should use two different variables for the values the user will give.
3. You can use a third variable to store their product, but it's not necessary.
4. You can print your result with `print()` function, in which you should
specify what you're printing.

```markdown
Example Input/Output (I/O):

Input:
13
12
Output:
25

Input:
10
10
Output:
20
```

# Assignment 2 of W03

Write a Python script that takes 2 the radii of 2 circles, calculates the area
of both, and calculates the area difference of them. If one of them are bigger
than the other, then the script should print;
```markdown
{circle1} > {circle2}
Area Difference : {area_difference}
```
If both are of same size, then it should print;
```markdown
{circle1} = {circle2}
Area Difference : 0
```

Hints:
1. You can use the function `eval(input())` to get input from the user.
2. You should use two differente variables for the radii, and calculate the
areas of each circle and store them in differente variables.
3. You can assign a fifth variable to the area difference, but it's not
necessary.
4. You can use this to print out your calculations, but don't forget to change
the `radius_1`, `radius_2`, and `area_diff` variables to your own variables.
```python
print(f"{radius_1} > {radius_2}")  # If radius 1 is larger than radius 2
print(f"{radius_1} = {radius_2}")  # If radii are equal
print(f"Area Difference : {area_diff}")  # The area difference
```

-------------------------------------------------------------------------------

# Glossary

1. `print()` : Generic print function. Prints the value given in the argument.

2. `type()` : Returns the type of the value given as argument.

-------------------------------------------------------------------------------

# References

[^1]: [Precedence and Associativity of Operators in Python](https://www.programiz.com/python-programming/precedence-associativity) | 
[WayBack Machine](https://web.archive.org/web/20250605144400/https://www.programiz.com/python-programming/precedence-associativity)
