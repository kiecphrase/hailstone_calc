'''

Concept: Hailstone series is a quick way to generate a lot of numbers that are somewhat related to eachother that can seem random. 
The thought is by picking a scale and assigning notes in the scale a value of 0 through 9, you can create somewhat random patterns
of notes to use. This is a more or less "random" version of the process in which the starting number is some integer between 1 and 10,000,000,000


things to note:

- this specific method will always end in the number 4, due to the end pattern of hailstone series and the way I made the while loop.
    - You can extend the number pattern as much as you want while staying valid by repeating 4 -> 2 -> 1 back to 4
    - the "tail" will always end in some pattern that boils down to 4. There are at least 2 unique patterns (53 or 52)
        - There's probably a larger set of patterns at the tail, but my undergrad isn't in math, so I don't know it

- there is the potential that this breaks due to the nature of hailstone series and the limit of the integer variable type
    - idk if a number in the generative range will get to it in its series though...


EXAMPLE (CMaj):

9 - D4
8 - C4
7 - B3
6 - A3
5 - G3
4 - F3
3 - E3
2 - D3
1 - C3
0 - B2


thoughts on how to use the numbers:

- I used 567 as a test, where each number of all numbers in the hailstone series corrisponded to the value of the tone of a quarter note (as shown above) to generate a melody
- could also use each entry in the series as values for a chord, measure, or some other division

'''


# import what needs to be imported
import random as r
import math as m


# generate random starting point for the hailstone
g = m.floor(10 * r.random() + 1)

y = ""
i = 0

for i in range(g):
    y += str(m.floor(10 * r.random()))

print("starting number: ", y)

x = int(y)
series = []

series.append(x)

# go through every number
while x != 1 and x != 2 and x != 4:

    # even number
    if x % 2 == 0:
        x = x // 2

    # odd number
    else:
        x = (x * 3) + 1

    series.append(x)

# display the series in the terminal
# TODO: add a file print out
print(' ')
print("numbers in hailstone series: ")
raw = ""
for s in series:
    raw += str(s)

print(raw)

print(' ')
print("hailstone series: ")
for i in series:
    print(i)