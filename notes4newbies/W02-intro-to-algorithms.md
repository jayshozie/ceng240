MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Algorithms

## What is an algorithm?

An algorithm can mean many things, here are some definitions from the official
CENG240 slides.

An algorithm is;
- a procedure or formula for solving a problem,
- a set of instructions to be followed to solve a problem,
- an effective method expressed as a finite listt of well-defined instructions
    for calculating a function
- step-by-step procedure for calculations.

These are all pretty good explanations of what an algorithm is. I think we can
combine these into one single sentence, from Harvard's CS50 Introduction to
Computer Science course:
- An algorithm is a step-by-step set of instructions to solve a problem.

This also gives the essence of computer science, too. Whatever you're doing is
to solve a problem, that's the main idea.

<details>
    <summary>A formal definition for the curious</summary>
    Starting from an initial sate and initial input (perhaps empty), the
    instructions describe a computation that, when executed, will proceed
    through a finite number of well-defined successive states eventually
    producing output and terminating at a final ending state.
</details>

I will try to explain you what an algorithm is by giving an example, this
example is from the
[Lecture 0 of CS50 2025](https://www.youtube.com/live/2WtPyqwTLKM).

Think about a phonebook, for the younger people who are reading this it's a
thick book of alphabetically ordered phone numbers of people living at a
certain area and it may also include phone numbers of local shops and all. Now,
you want to find the phone number of John Harvard, an old friend of yours. What
are the ways you can search the book?

The first one that comes to mind is to through all pages one-by-one from start
to either finish or John Harvard, if he's in the book. This is a correct
algorithm, because if he's in the book you will definitely (if you're reading
carefully) find him; however, this is pretty inefficient isn't it? Let's sa
that there are 1000 pages in total. In every page we have very tiny lines of
phone numbers. Let's try a different algorithm, in which we go 2 pages at a
time, this should take half the time since we're going twice as fast, but is
this algorithm correct? No, right, because John Harvard could be sandwiched
between two pages when we come to 'J'. Even though this algorithm is twice as
fast as our previous algorithm, it's not completely correct. Maybe we could go
back and check again when we see that we've come to 'K'. All and all, these are
pretty bad algorithms compared to the one I'll tell you right now.

Imagine opening that book right from the middle, we're now seeing a page with
the letter 'M'. Now, effectively we've divided this phonebook into two
different parts. Which side should John Harvard be, if he's in the book? Left
side, right? Then, we can get rid of the right side completely, since we're
100% sure that he cannot be at that side. Now, we have a 500 page problem. Do
it again. Split it right in the middle, you will probably see the letter 'G'.
We've overshot, John Harvard should be at the right side, so let's get rid of
the left side of the book. Do it again and again and again, making sure which
side he should be on. At the end you should be left with a single page, in
which John Harvard is on that page (if he's in the book at all).

That's what an algorithm is, a set of very carefully put instructions that
helps us solve very real problems.

Now, let's compare those algorithms, shall we? We are going to compare their
worst-case-scenario performances, because we could be looking for someone with
a name starting with the letter 'Z'.

First algorithm is a linear one, right? If the Harvard and MIT from down the
road merged their phonebooks together, they would have a 2000-page phonebook,
and it could take us twice as fast to find that person. Let's call that graph,
n. Second algorithm is also a linear one, because even if we were going twice
as fast, every 2 pages added to the book would add one more step to our
algorithm, making its graph n/2. This way of trying to understand the average
speed of algorithms is called the Big-O Notation (e.g., O(n), O(n/2))

The third algorithm, however, is different. Its graph's shape is not linear,
it's fundamentally different. If you remember your logarithms, you should
recognize that graph as the graph of log base 2 of n. Adding 2 or 100 pages
doesn't change our runtime even a bit. Yes, it's not a constant function, but
it's significantly better than both of those algorithms. The Big-O Notation of
this algorithm would be O(log2(n)).

![1.1.1 - Three Algorithms Compared](./images/comparison-of-3-algorithms-cs50Week0Slide141.png)

If we were to compare a case where we are looking for someone with their name
starting with the letter 'Z', in a thousand-page phonebook, first algorithm
would take 1000 steps but it would find it, the second algorithm would take
~500 steps but it has a 50/50 chance of not finding it; however, the third
algorithm would only take about 10 steps.

-------------------------------------------------------------------------------

## Valid Operations in Algorithms

Let's write the third algorithm in something called 'pseudocode'.

<details>
    <summary>What is pseudocode</summary>
    A pseudocode is not a formal language or something like that. It's a way of
    creating an algorithm in understandable but precise human language without
    the burden of writing it out in syntax of programming languages.
</details>

```markdown
01. Pick up phonebook
02. Open the middle of book
03. Look at page
04. If person is on the page
05.     Call person
06. Else if person is earlier in book
07.     Open to middle of left half of book
08.     Go back to line 3
09. Else if person is later in book
10.     Open to middle of right half of book
11.     Go back to line 3
12. Else
13.     Quit
```

There are 3 types of valid operations in algorithms: sequentials, conditionals,
and iteratives. Sequentials are simple, well-defined tasks, and they're usually
declarative sentences. Conditionals are checks done by asking questions to the
code, and acting by the result of that question. Iteratives are looping
instructions that repeat a set (or subset) of instructions. Let's identify
these in my pseudocode.

From our definitions, line 1 must be a sequential operation. It's a
well-defined declarative sentence, in which the user asks the machine to pick
up the phonebook. Same thing applies to the second and third lines, they ask
the machine to do some well-defined task, open the middle of the book or look
at page. Line 4, however, is a conditional. It checks whether the person is on
the page that we've looked on line 3. The extra space on the line 5 is
intentional, they specify what the machine should do if the question asked in
the conditional is correct. In our case, if the person is on the page the
machine should call the person, if not it would continue with the next
conditional, else if person is earlier in book in our case. It checks whether
the person we're trying to call is earlier in the book and then if that's
correct it does the indented part of the code, in which it opens to middle of
the left half of the book, and goes back to line 3. Line 8 is a perfect example
of iterative operation, if the conditional is correct, it would go back to the
line 3 and iterate over the rest of the code again. Same thing applies for the
'code block' between the lines 9 and 11. If all three conditionals, the
questions we ask the computer to check, fail, we have a last case scenario, an
else case, in which we ask the computer to quit searching so it doesnt' go into
an infinite loop.

If you missed anything up there, I strongly urge you to watch the
[video](https://www.youtube.com/live/2WtPyqwTLKM) I've mentioned before. Prof.
David J. Malan is an amazing professor, he explains everything so well.

-------------------------------------------------------------------------------

## Ways of Describing Complex Algorithms

First of all, the best way of describing an algorithm is the one you understand
the best. Putting that aside there are some popular ways of doing it.

1. **Using Pseudocode**

Pseudocoding is very popular among developers, because it's very easy to
understand and make other people understand. It's really easy to write, you
just take a pen and paper and write the instructions in the order of execution,
just like what David's pseudocode of searching a name in a phonebook.

2. **Using Flow-Charts**

This is, again, very popular among developers, because it's easy to follow and
see the outcomes of every possibility. This might take a bit more time than
writing pseudocode, but you have more tools in your shed. You can use colors
for different operations, for example.

![1.3.1 - Example Algorithm Flowchart](./images/algorithm-flowchart-example.png)

In this funny example, the algorithm asks for the user's favorite subject. If
They don't say "Computer Science", the algorithm prints out "Try again.!". If
they do say "Computer Science" the algorithm prints out "Of course it is!" and
ends the program.

-------------------------------------------------------------------------------

# Programming Languages

## The World of Programming Languages

If you remember week 0, I've talked about low/high level programming languages.
I have intentionally mislead you there, sorry. Assembly is actually considered
to be a low-level programming language, it's only 'high' level compared to pure
machine code, and basically nothing else.

### Levels of Programming Languages

The levels of programming languages are not like the levels of a game. It's
actually tells you how abstracted that language is. It's not a definite thing,
mind you, it's only a way of understanding how abstract that language is
compared to pure machine code.

#### Low-Level Programming Languages

A low-level programming language, like Assembly of x86_64, is a programming
language that is very close to the machine code. It has very little abstraction
from the machine code, and it is very hard to read for humans. It is very
efficient, however, because it is very close to the machine code, thus not that
abstract compared to high-level programming languages. It is usually used in
operating systems, embedded systems, and other performance critical
applications. It is also used in reverse engineering, because it is very easy
to understand how the machine works with it.

<details>
    <summary>An Example Assembly (x86_64) Code</summary>
```assembly

section .data
    ; Define our message and its length
    msg db "Hello, World!", 0x0A ; 0x0A is the ASCII code for newline
    len equ $ - msg             ; Calculates the length of the message

section .text
    global _start               ; Entry point for the linker

_start:
    ; syscall for sys_write (write to file descriptor)
    mov rax, 1                  ; sys_write syscall number
    mov rdi, 1                  ; File descriptor 1 (stdout)
    mov rsi, msg                ; Address of the message string
    mov rdx, len                ; Length of the message
    syscall                     ; Execute syscall

    ; syscall for sys_exit (exit program)
    mov rax, 60                 ; sys_exit syscall number
    mov rdi, 0                  ; Exit code 0 (success)
    syscall                     ; Execute syscall

```
</details>

#### High-Level Programming Languages









-------------------------------------------------------------------------------

# References

1.1.1 - [CS50 - 3 Algorithms Compared](https://cs50.harvard.edu/x/notes/0/cs50Week0Slide141.png)
[WayBack Machine](https://web.archive.org/web/20250601073812/https://cs50.harvard.edu/x/notes/0/cs50Week0Slide141.png)

1.3.1 - [BBC - Example Algorithm Flowchart](https://www.bbc.co.uk/bitesize/guides/z3bq7ty/revision/3)
[WayBack Machine](https://web.archive.org/web/20250320171857/https://bam.files.bbci.co.uk/bam/live/content/zs96tfr/large)












