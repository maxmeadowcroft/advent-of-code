"""
PART 1
"""

with open("data/1.txt", "r") as file:
    lines = file.readlines()

data_left: list[int] = [int(line.split()[0]) for line in lines]
data_right: list[int] = [int(line.split()[1]) for line in lines]

data_left.sort()
data_right.sort()

total_distance: int = 0

for i in range(len(data_left)):
    total_distance += abs(data_left[i] - data_right[i])

print(total_distance)

"""
Part 2
"""

similarity = 0

for i in range(len(data_left)):
    similarity += data_left[i] * data_right.count(data_left[i])

print(similarity)

