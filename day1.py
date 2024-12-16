
with open("data/1.txt", "r") as file:
    lines = file.readlines()

data_left = [int(line.split()[0]) for line in lines]
data_right = [int(line.split()[1]) for line in lines]

data_left.sort()
data_right.sort()

total_distance = 0

for i in range(len(data_left)):
    total_distance += abs(data_left[i] - data_right[i])

print(total_distance)