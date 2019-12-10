from queue import *


# Find all paths between start and end node
def find_paths(adjacency, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for child in adjacency[start]:
        if child not in path:
            child_paths = find_paths(adjacency, child, end, path)
            for child_path in child_paths:
                paths.append(child_path)
    return paths


# Extracts shortest path according to source node
def find_shortest_path(src):
    parent = {src: None}
    distance = {src: 0}

    visited = set()
    q = queue()
    q.enqueue(src)
    visited.add(src)

    while not q.is_empty():
        current = q.dequeue()
        for destination in current.get_neighbours():
            if destination not in visited:
                visited.add(destination)
                parent[destination] = current
                distance[destination] = distance[current] + 1
                q.enqueue(destination)

    return parent, distance


# Find all of the shortest path from path array
def find_shortest_paths(all_paths):
    all_shortest = []
    min = 0

    if len(all_paths) > 0:
        min = len(all_paths[0])

        for path in all_paths:
            if len(path) < min:
                min = len(path)

        for path in all_paths:
            if len(path) is min:
                all_shortest.append(path)

    return all_shortest


# Find the node with the most neighbor
def find_vertex_has_most_degree(dictionary):
    max_degree = 0
    node_with_max_degree = ''
    for vertex in dictionary:
        current_degree = dictionary[vertex]
        if current_degree > max_degree:
            max_degree = current_degree
            node_with_max_degree = vertex.get_key()
    return node_with_max_degree


# Converts linked list graph to adjacency matrix
def find_adjacency_matrix(graph):
    adjancency_list = []
    for node_i in graph:
        adjancency_row = []
        for node_j in graph:
            if node_i.get_key() is node_j.get_key():
                adjancency_row.append(0)
            elif node_j in node_i.get_neighbours():
                adjancency_row.append(1)
            else:
                adjancency_row.append(0)
        adjancency_list.append(adjancency_row.copy())

    return adjancency_list
