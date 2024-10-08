# Advent of Code 2023
# Day 23-2: A Long Walk

class Node:
    def __init__(self):
        self.edges = []

    def add_edge(self, node, cost):
        self.edges.append(Edge(node, cost))

    def replace_edge(self, old_node, new_node, new_cost):
        for edge in self.edges:
            if edge.node is old_node:
                edge.node = new_node
                edge.cost = new_cost


class Edge:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost


def find_longest_path(path, goal, distance=0):
    node = path[-1]

    if node is goal:
        return distance

    max_distance = 0
    for edge in node.edges:
        if edge.node not in path:
            max_distance = max(find_longest_path(path + (edge.node,), goal, distance + edge.cost), max_distance)

    return max_distance  # Dead ends will return 0.


def parse_input(path):
    with open(path) as file:
        input_grid = [row.strip() for row in file.readlines()]
        node_grid = [[None for _ in range(len(input_grid[y]))] for y in range(len(input_grid))]

        # Create nodes:
        for y in range(len(input_grid)):
            for x in range(len(input_grid[y])):
                if input_grid[y][x] == "#":
                    continue

                node = Node()

                # Connect to node at x - 1:
                if x > 0 and node_grid[y][x - 1]:
                    node.add_edge(node_grid[y][x - 1], 1)
                    node_grid[y][x - 1].add_edge(node, 1)

                # Connect to node at y - 1:
                if y > 0 and node_grid[y - 1][x]:
                    node.add_edge(node_grid[y - 1][x], 1)
                    node_grid[y - 1][x].add_edge(node, 1)

                node_grid[y][x] = node

        # Remove all nodes with two edges, connecting their connected nodes:
        for y in range(len(node_grid)):
            for x in range(len(node_grid[y])):
                node = node_grid[y][x]

                if node and len(node.edges) == 2:
                    edge_a, edge_b = node.edges[0], node.edges[1]
                    node_a, node_b = edge_a.node, edge_b.node
                    new_cost = edge_a.cost + edge_b.cost

                    node_a.replace_edge(node, node_b, new_cost)
                    node_b.replace_edge(node, node_a, new_cost)

                    node_grid[y][x] = None

        return [node for row in node_grid for node in row if node is not None]


nodes = parse_input("input.txt")
start_node, end_node = nodes[0], nodes[-1]

print(find_longest_path((start_node,), end_node))