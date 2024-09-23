# Advent of Code 2023
# Day 13-2: Point of Incidence

ROWS = 0
COLS = 1


def find_reflection(matrix, mods_required = 0):
    for i in range(len(matrix) - 1):
        mod_count = 0

        for j in range(i + 1):
            ja = i - j
            jb = i + 1 + j

            if jb >= len(matrix):
                continue

            for k in range(len(matrix[ja])):
                if matrix[ja][k] != matrix[jb][k]:
                    mod_count +=1

        if mod_count == mods_required:
            return j + 1

    return 0


def parse_input(path):
    with open(path) as file:
        matrices = [[]]
        for line in [x.strip() for x in file.readlines()]:
            if line == "":
                matrices.append([])
            else:
                matrices[-1].append(line)

        patterns = []
        for matrix in matrices:
            rows = matrix
            cols = ["".join([row[x] for row in rows]) for x in range(len(rows[0]))]
            patterns.append({ROWS: rows, COLS: cols})

        return patterns


patterns = parse_input("input.txt")

sum = 0
for pattern in patterns:
    sum += 100 * find_reflection(pattern[ROWS], 1) + find_reflection(pattern[COLS], 1)

print(sum)