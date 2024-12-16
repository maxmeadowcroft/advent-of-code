
with open("data/2.txt", "r") as file:
    data = [list(map(int, line.split())) for line in file]

print(len(data))

""""
48, 45, 43, 41, 38, 37, 34

1. make sure all go up or all go down
2. make sure the interval is always at most 3

"""

valid = 0

for element in data:
    direction = element[0] < element[1]
    is_valid = True

    for i in range(0, len(element) - 1):
        if direction and element[i+1] <= element[i]:
            is_valid = False
            break
        elif not direction and element[i + 1] >= element[i]:
            is_valid = False
            break

        if abs(element[i] - element[i+1]) > 3:
            is_valid = False
            break

    if is_valid:
        valid += 1

print(valid)