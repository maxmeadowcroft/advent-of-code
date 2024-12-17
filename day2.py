# Part 1

def is_valid_sequence(sequence: list[int]) -> int:
    is_increasing = sequence[0] < sequence[1]
    is_valid = True

    for i in range(len(sequence) - 1):
        if is_increasing and sequence[i + 1] <= sequence[i]:
            is_valid = False
            break
        elif not is_increasing and sequence[i + 1] >= sequence[i]:
            is_valid = False
            break

        if abs(sequence[i] - sequence[i + 1]) > 3:
            is_valid = False
            break

    return 1 if is_valid else 0


# Reading data from file
with open("data/2.txt", "r") as file:
    data = [list(map(int, line.split())) for line in file]

# Counting valid sequences
valid_sequence_count = sum(is_valid_sequence(seq) for seq in data)

print(valid_sequence_count)


# Part 2
def get_subsequences(sequence: list[int]) -> list[list[int]]:
    subsequences = []
    for i in range(len(sequence)):
        subsequences.append([sequence[x] for x in range(len(sequence)) if x != i])
    return subsequences


# Counting valid sequences with one element allowed to be wrong
valid_with_one_error_count = 0

for sequence in data:
    if is_valid_sequence(sequence):
        valid_with_one_error_count += 1
    else:
        subsequences = get_subsequences(sequence)
        for subsequence in subsequences:
            if is_valid_sequence(subsequence):
                valid_with_one_error_count += 1
                break

print(valid_with_one_error_count)
