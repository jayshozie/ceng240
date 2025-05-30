MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

# Introduction

After the preliminary about why and how you should use the documentation of a
programming language, let us start with the very basics of programming.

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

# Basics

I'll introduce you to some core concepts of programming, via phases. Each phase
has a way to represent, and another way to manipulate data. I will try to give
examples for Windows and Linux/macOS users for as many subjects as I can.

## Phase 1: Value & Command Line

You can interact with your computer directly from the command line.

- For Windows 10/11:
Windows has a builtin command-line interface (CLI) called PowerShell
(PowerShell.exe), it's also a command shell. You can use it by either searching
for it in the Start menu, or running it from the Run box
(Win+R | cmd.exe <Enter>). When you enter the PowerShell you should see
something similar to this:
```bash session
PS C:\Users\foo>
```
This is your command line interface. You'll see this a lot, get used to it.
This is basically how you tell the Windows to do stuff. Yes, you can do most of
your work through Explorer or Google Chrome, but there are some things that you
need to do from here.

You can use it as a calculator;
```bash session
PS C:\Users\foo> 2+2
4
PS C:\Users\foo>
```
You can create directories (yes, they are not called folders in the universe of
shells)
```bash session
PS C:\Users\foo> mkdir testDir


    Directory: C:\Users\foo\


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        DD/MM/YYYY     HH:MM                testDir


PS C:\Users\foo>
```

You can go change your directory;
```bash session
PS C:\Users\foo> cd testDir
PS C:\Users\foo\testDir> cd ..  # You can go back with cd.. too on Windows
PS C:\Users\foo>
```

You can remove files/directories;
```bash session
PS C:\Users\foo> cd testDir
PS C:\Users\foo\testDir> cd ..  # You can go back with cd.. too on Windows
PS C:\Users\foo>
```

You can create a text-based files;
