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
After you're done with a file, you should always close it to free up system
resources. You can do this by calling the `close()` method on the file object.
```python
file = open('myfile.txt', 'r')
# do something with the file
file.close()  # Always close the file when done
# always do close the file when done, but we'll see that explicitly calling
# that method becomes unnecessary with a 'with' call.
```
There's nothing else with the `close()` method that you need to know other than
if you don't close the file you may actually lose the data.

## Files and Sequential Access (Byte-By-Byte/Line-By-Line)

When you open a file, a cursor is placed at the beginning of the file. You can
think of this as a blinking line in your favorite text editor. When you read or
write data, the cursor moves forward by the number of bytes read or written.
There is 2 main ways to access data in a file:

1. **Byte-By-Byte Access:** You can read or write data one byte at a time using
the `read(size)` and `write(data)` methods. The `size` parameter specifies the
number of bytes to read or write. If you don't provide a size, it defaults to
one (1) byte.
2. **Line-By-Line Access:** You can read or write data one line at a time using
the `readline()` and `writeline(data)` methods. These methods read or write
data until a newline character (`\n`) is encountered. Don't forget that this
reading process itself will include the newline character in the string it
returns.

You probably won't use byte-by-byte access unless it's absolutely necessary,
since usually it's more efficient to read/write larger chunks of data at once.

## The Much Needed Example

Now that we know how to open a file and write to it, let's do it.
```python
# let's create a sample file with the open method in write mode
temporary_file_pointer = open('firstexample.txt', 'w')
temporary_file_pointer.write('hello\n')
temporary_file_pointer.write('how are you?\n')
temporary_file_pointer.close()
```
Now, if you go and open that file with a text editor (firstexample.txt), you
should see this:
```text
hello
how are you?
```
Let's try that again with a different set of commands.
```python
other_temporary_fp = open('firstexample.txt', 'w')
other_temporary_fp.write('what\n')
other_temporary_fp.write('happened\n')
other_temporary_fp.write('here?\n')
other_temporary_fp.close()
```
Now, if you open the file you should see this:
```text
what
happened
here?
```
Like I said, if you open a file in write mode and it already exists it
overwrites the file. Let's do something else in append mode.
```python
fp = open('firstexample.txt', 'a')
fp.write('ohh, i used write mode,\n')
fp.write('and not append mode.\n')
fp.close()
```
You should see this:
```text
what
happened
here?
ohh, i used write mode,
and not append mode.
```
I hope this example makes it clear.

Now we can have an example that explains the difference between `read()` and
`readline()`.


## Parsing (`split()`)

When you read data from a file, it often comes in a single string. To make it
more manageable, you can split the string into smaller parts using the 
`split()` method. This method splits a string into a list of substrings based
on a specified delimiter (by default, whitespace). Here is an example:
```python
data = "Hello, world! This is a test."
words = data.split()  # splits by whitespace by default
print(words)  # Output: ['Hello,', 'world!', 'This', 'is', 'a', 'test.']
```
You can also specify a different delimiter:
```python
data = "apple,banana,cherry"
fruits = data.split(',')  # splits by comma
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

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

-------------------------------------------------------------------------------

###     TODO : ASSIGNMENT(S)
