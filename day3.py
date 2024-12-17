"""
Part 1
find all patterns of mul(int(), int())
ignore everything else
"""
import re

with open('data/3.txt') as f:
    data = f.read()

valid = re.findall(r"(mul\(\d+,\d+\))", data)

total = 0

def mul(x, y):
    return x * y

for i in valid:
    total += eval(i)

print(f"Pt 1\t{total = }")

"""
PART 2
"""

valid = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", data)

total = 0
pause = False

for i in valid:
    if i == "don't()":
        pause = True
        continue
    elif i == "do()":
        pause = False
        continue
    if not pause:
        total += eval(i)

print(f"Pt 2\t{total = }")