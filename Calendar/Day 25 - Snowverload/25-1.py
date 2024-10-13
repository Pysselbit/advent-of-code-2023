# Advent of Code 2023
# Day 25-1: Snowverload

import random


def get_shortest_path(graph, start, goal):
    paths = {}
    queue = [(start, ())]

    while len(queue) > 0:
        node, path = queue.pop(0)
        path += (node,)

        if node in paths and len(path) > len(paths[node]):
            continue

        paths[node] = path

        for neighbor in graph[node]:
            queue.append((neighbor, path))

    return paths[goal]


def get_most_frequent_edges(graph, nodes, edges, runs):
    edge_frequencies = {edge: 0 for edge in edges}

    for _ in range(runs):
        node_a = random.choice(nodes)
        node_b = random.choice(nodes)

        path = get_shortest_path(graph, node_a, node_b)

        for i in range(1, len(path)):
            edge_frequencies[frozenset({path[i - 1], path[i]})] += 1

    return sorted(edge_frequencies, key=edge_frequencies.get, reverse=True)[:3]


def get_component_size(graph, node):
    visited = {}
    queue = [node]

    while len(queue) > 0:
        node = queue.pop(0)

        if node in visited:
            continue

        visited[node] = True

        for neighbor in graph[node]:
            queue.append(neighbor)

    return len(visited)


def parse_input(path):
    graph = {}
    nodes = []
    edges = []

    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]

        for line in lines:
            component, connections = line.split(":")
            connections = connections.strip().split(" ")

            if component not in graph:
                graph[component] = []
                nodes.append(component)

            for connection in connections:
                if connection not in graph:
                    graph[connection] = []
                    nodes.append(connection)

                graph[component].append(connection)
                graph[connection].append(component)
                edges.append(frozenset({component, connection}))

    return graph, nodes, edges


def try_get_disconnected_component_sizes(input_path, runs):
    graph, nodes, edges = parse_input(input_path)
    most_frequent_edges = get_most_frequent_edges(graph, nodes, edges, runs)

    for edge in most_frequent_edges:
        node_a, node_b = edge
        graph[node_a].remove(node_b)
        graph[node_b].remove(node_a)

    node_a, node_b = most_frequent_edges[0]
    size_a = get_component_size(graph, node_a)
    size_b = get_component_size(graph, node_b)

    return size_a != len(nodes), size_a, size_b


success = False
size_a = size_b = 0

while not success:
    success, size_a, size_b = try_get_disconnected_component_sizes("input.txt", 100)

print(size_a * size_b)