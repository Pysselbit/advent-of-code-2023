# Advent of Code 2023
# Day 8-2: Haunted Wasteland

import re
import math

START = "A"
FINISH = "Z"

with open("input.txt") as file:
    lines = file.readlines()

    moves = lines[0].strip()
    graph = {}
    nodes = []

    for i in range(2, len(lines)):
        matches = re.findall(r"[A-Z][A-Z][A-Z]", lines[i])

        node = matches[0]
        nodeL = matches[1]
        nodeR = matches[2]

        graph[matches[0]] = [matches[1], matches[2]]
        if node[2] == START:
            nodes.append(node)

    move_index = 0
    move_count = 0

    # Find periods:
    periods = [-1] * len(nodes)
    while min(periods) < 0:
        move = moves[move_index % len(moves)]
        move_index += 1

        for i in range(len(nodes)):
            nodes[i] = graph[nodes[i]][0] if move == "L" else graph[nodes[i]][1]
            if nodes[i][2] == FINISH:
                if periods[i] < 0:
                    periods[i] = move_index

    # Find LCM of periods:
    move_count = 1
    for period in periods:
        move_count = math.lcm(period, move_count)

    print(move_count)