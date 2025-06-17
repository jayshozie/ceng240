MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Note



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

[^Khan Academy]
> In math, remember a function is basically a rule or a process that takes an
> input and gives you back a single, predictable output.

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

# References

[^Khan Academy]: [What is a function?](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:evaluating-functions/v/what-is-a-function#:~:text=and%20from,and%20only%20ONE%20given%20output.)

