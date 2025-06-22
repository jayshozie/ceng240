MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# File Handling in Python

In this markdown, we will tackle a problem most students who take this course
completely fail to understand. Why is that? Because they're NOT explaining you
how to handle files. They throw some functions and methods at you and don't
explain how they work, so you fail. Not here. Let's go.

## Introduction: Basics

Programs often need to interact with external data that persists beyond the
program's execution (e.g. saving user settings, reading data from a sensor,
logging events, etc.). Files are the primary way to store data on a computer,
and the examples I've given can't be handled in the RAM, because we don't want
to lose the settings of the user, or our logs of events. So, we save those in
files.

After understanding *why* are we handling files, let's get to how.

1. **The `open()` Function:** It's the primary way to interact with files in
Python, because before you do anything you need to open a file, right? Same
here. Here is the syntax of the function:
```python
open(<filename>, <file_mode>)
```
You provide the name of the file you want to do something as a string literal,
and the mode you want to open it with. Here are the mods you need to know:
```text
'r' (Read   Mode): Opens the file for reading, creates it if it doesn't exist.

'w' (Write  Mode): Opens the file for writing, creates it if it doesn't exist,
                   truncates (empties) the entire file it exists (very
                   important, you can lose data if you're not careful.)

'a' (Append Mode): Opens the file for writing, creates it if it doesn't exist,
                   appends data if it exists.
```
2. **The `close()` Method:** 

## Files and Sequential Access (Byte-By-Byte/Line-By-Line)

## Parsing (`split()`)

## Termination of Input

There are two ways to stop reading input from a file in a loop:
1. **Reading a Definite Number of Times:** Call `read()` or `readline()`
functions for fixed amount of times.
2. **Checking If The Cursor is at The End of The File:** Here is how you do it:
```python
with open('my_txt.txt', 'r') as text:
    nextline = text.readline()
    while nextline != '':  # checking if nextline is an empty string
        # do something here
        nextline = text.readline()  # read the next line
```

## Formatting Files

## Binary Files
