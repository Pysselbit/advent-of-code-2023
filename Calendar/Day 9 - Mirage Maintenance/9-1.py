# Advent of Code 2023
# Day 9-1: Haunted Wasteland

import numpy as np

with open("input.txt") as file:
    history = []

    for line in file.readlines():
        history.append([np.fromstring(line.strip(), dtype=int, sep=" ").tolist()])

    for data_set in history:
        while not all(item == 0 for item in data_set[-1]):
            data_set.append([])

            source = data_set[-2]
            target = data_set[-1]

            for i in range(1, len(source)):
                target.append(source[i] - source[i - 1])

        data_set[-1].append(0)
        for i in range(-1, -len(data_set), -1):
            data_set[i - 1].append(data_set[i - 1][-1] + data_set[i][-1])

    print(sum(data_set[0][-1] for data_set in history))