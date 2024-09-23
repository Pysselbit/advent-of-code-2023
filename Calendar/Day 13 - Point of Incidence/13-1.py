# Advent of Code 2023
# Day 13-1: Point of Incidence

def find_reflection(matrix):
    for i in range(len(matrix) - 1):
        is_reflection = True

        for j in range(min(i + 1, len(matrix) - i - 1)):
            if matrix[i - j] != matrix[i + 1 + j]:
                is_reflection = False

        if is_reflection:
            return i + 1

    return 0


def parse_input(path):
    with open(path) as file:
        matrices = [[]]
        for line in [x.strip() for x in file.readlines()]:
            if line == "":
                matrices.append([])
            else:
                matrices[-1].append(line.replace(".", "0").replace("#", "1"))

        patterns = []
        for matrix in matrices:
            rows = [int("0b" + y, 2) for y in matrix]
            cols = [int("0b" + "".join(str(row[x]) for row in matrix), 2) for x in range(len(matrix[0]))]
            patterns.append([rows, cols])

        return patterns


patterns = parse_input("input.txt")

print(sum(find_reflection(pattern[1]) + 100 * find_reflection(pattern[0]) for pattern in patterns))