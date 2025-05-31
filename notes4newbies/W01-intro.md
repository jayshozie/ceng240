MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

Since they do ask these things as questions in the midterm and final exams, I
also will explain you what they mean. Sorry in advance.

# Computers

-------------------------------------------------------------------------------

## What is a computer?

A computer is an electronic object that can do some sort of calculation. This
may sound like a calculator, but guess what? The very thing you're reading this
on is an extremely over-powered calculator, and it can only do addition. If you
would like to learn even more deeper stuff like how does a computer do
subtraction with addition, visit my
[cs-studies](https://github.com/jayshozie/cs-studies) repository. Generally,
Alan Turing is the accepted father of the computer. He's the inventor of the
Turing machine, which is a theoretical machine that manipulates a tape with
infinite 0s and 1s on it. This machine is a complete equivalent of the machine
you're reading this right now. It can do whatever a modern computer can,
because that is exactly what your machine is doing right now. Even though more
complicated, every modern computer is a Turing machine on steroids.

-------------------------------------------------------------------------------

## Components of a Computer

There are multiple cruical components of a computer, namely the CPU, RAM, and
storage.

### The von Neumann (Princeton) Architecture

This is the blueprint of the great-great grandpa of your computer. It has 2
parts: the CPU and the memory. The main difference between the Princeton
architecture and the Harvard architecture is that in the Princeton architecture
both the instructions and the value are stored in the same memory. In Harvard
architecture, however, there are 2 separate memories, where one holds the
instructions and the other holds the values that are needed on runtime.

#### Central-Processing Unit (CPU)

The central-processing unit, or abbreviated as CPU, is the brain of the
computer. It's the component that handles all of the computation. It starts as
soon as you start your computer and it executes instruction after instruction.
Modern computers are way more complex than what von Neumann designed, but the
idea stays the same. It itself has multiple parts.

##### Registers

These are spots on a CPU that holds some values. The reason why these exist
and why the CPU doesn't just store them in the memory is the speed difference.
In modern computers there are 4 ways we can store data (from fastest to
slowest): registers, cache, RAMs, SSDs, HDDs. If you read this from last to
first now you have the list from highest storage to lowest. Actually, assigning
speed to registers is a bit of misleading, because since that's where the CPU
is doing its calculations its speed is the speed of the CPU itself.

Cache is the fastest way a CPU can access to data. They are placed right at the
die itself, where die is the silicon die of the CPU (for further reading:
[Die (integrated circuit)](https://en.wikipedia.org/wiki/Die_(integrated_circuit))

##### Arithmetic-Logic Unit (ALU)

This is the part of the CPU that handles all of arithmetic and logical
calculations. This is the place where 1+1 equals 10. A weird world, surely.
ALU has a lot of electrical logic gates (e.g.: AND, OR), which is connected so
that it can do computations and process instructions.

P.S.: 10 is the binary representation of the decimal number 2.

##### Control Unit

This is the part of the CPU that handles the
reading-and-writing-values-to-the-memory-part. 

#### Random Access Memory (RAM)

Memory (or its more modern name, RAM) is a long list of values and instructions
stored in addresses. Addresses may look a bit scary (e.g.: 11000011 (binary),
0xC3 (hexadecimal), ebx (Assembly)), but you don't need to worry about them too
much, Python handles all of that.

#### Instructions

Instructions are how the user interacts with the CPU. Here is an example:
(This is not how we actually, well, there are some people who has to code like
this, but that's not what we're going to do.)

##### Machine Code (Binary)
100000111100001100001010
(10000011 11000011 00001010 for easier reading)
##### Machine Code (Hexadecimal)
0x83 0xC3 0x0A
##### Assembly (x86_64)
add ebx, 10

All of these mean exactly the same thing, add the value 10 to the ebx memory
location.

#### Fetch-Decode-Execute (Fetch-Execute) Cycle

OK, now we have a way to tell the CPU to do stuff, but how does it understand
us?

Control Unit fetches an instruction from the memory, stores it in the registers
of the CPU. ALU, decodes that instruction, executes it, stores the answer
of that computation in another register. Control Unit takes that stored data
and writes it into memory, if needed. This is called the "Fetch-Execute" cycle.

#### CPU Architectures

First of all, yes, it's called architecture.

A CPU architecture is a way of so-to-say constructing the CPU chips, but the
part that concerns us is that they are sets of instructions that are almost
exactly the same in every CPU with that architecture.



There are 2 main architectures you need to know: x86 family and ARM. 

