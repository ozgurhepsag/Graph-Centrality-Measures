from utility_functions import *
import networkx as nx
import numpy as np
from scipy import linalg


def find_degree_centrality(graph):
    degree_dict = {}
    degree_sum = 0

    # Calculate the sum of degrees
    for node in graph:
        degree = node.get_neighbours_counts()
        degree_dict[node] = degree
        degree_sum += degree

    # Normalization
    for i in degree_dict:
        degree_dict[i] = degree_dict[i] / degree_sum
    return degree_dict


def find_closeness_centrality(graph):
    node_measure_results = {}
    normalization_value = graph.get_vertex_number() - 1
    distances_sum = 0

    # Calculate the sum of degrees
    for node in graph:
        vertices, distances = find_shortest_path(node)
        for i in distances:
            distances_sum += distances[i]

        node_measure_results[node] = distances_sum
        distances_sum = 0

    # Normalization
    for i in node_measure_results:
        node_measure_results[i] = node_measure_results[i] / normalization_value
        node_measure_results[i] = 1 / node_measure_results[i]
    return node_measure_results


def find_eccentricity_centrality(graph):
    node_measure_results = {}
    distances_max = 0

    # Calculate the sum of degrees
    for node in graph:
        vertices, distances = find_shortest_path(node)
        for i in distances:
            value = distances[i]
            if value > distances_max:
                distances_max = value
        node_measure_results[node] = distances_max
        distances_max = 0

    # Normalization
    for i in node_measure_results:
        if not node_measure_results[i] is 0:
            node_measure_results[i] = 1 / node_measure_results[i]
    return node_measure_results


# Main eigen centrality function
def find_eigenvector_centrality_numpy(graph):
    index = 0
    indices_of_max_node = 0
    new_graph_list = list(graph.vertices)

    np_array = find_adjacency_matrix(graph)

    eigen_values, eigen_vector = linalg.eig(np_array)

    # Round float values
    eigen_vector = np.round(eigen_vector[:, 0], 2)
    node_degree_with_max = eigen_vector.max()

    for i in eigen_vector:
        print("Node : " + str(new_graph_list[index]) + " " + str(i))
        index = index + 1

    for i in eigen_vector:
        if i == node_degree_with_max:
            break
        else:
            indices_of_max_node += indices_of_max_node

    print("Eigen Vector with most central node is : " + str(new_graph_list[indices_of_max_node]) + " with eig value :"+str(node_degree_with_max))


def find_betweenness_centrality(graph):
    node_measure_results = dict()
    adjacency_list = {}
    count = 0
    neighbors_list = []

    # Converts graph structure to adjacency list
    for node_temp in graph:
        temp = node_temp.get_neighbours()
        for node_neighbour in temp:
            neighbors_list.append(node_neighbour.get_key())
        adjacency_list[node_temp.get_key()] = neighbors_list.copy()
        neighbors_list.clear()

    # Calculate the sum of degrees
    for node_selected in graph:
        node_measure_results[node_selected] = 0
        for node_src in graph:
            for node_dest in graph:

                if node_src is node_dest:   # A == A
                    continue
                elif node_dest.get_key() is node_selected.get_key() or node_src.get_key() is node_selected.get_key():
                    continue

                all_paths = find_paths(adjacency_list, node_src.get_key(), node_dest.get_key(), path=[])  # Utility
                all_shortest = find_shortest_paths(all_paths)   # Utility function

                for path in all_shortest:   # find paths that passing through our selected node
                    if node_selected.get_key() in path:
                        count += 1

                node_measure_results[node_selected] = node_measure_results[node_selected] + (count / len(all_shortest))

                all_shortest.clear()
                count = 0

        node_measure_results[node_selected] = node_measure_results[node_selected] / 2

    return node_measure_results


# Written for testing numpy eigen function results
# def find_eigenvector_centrality_networkx(graph):
#     centrality = nx.eigenvector_centrality(graph)
#     for i in centrality:
#         print("Vertex : "+ str(i) + " "+ str(round(centrality[i], 2)))
#
#     #print("Eigen Vector results :  " + str(graph.degree))
#     max_degree = 0
#     node_degree_with_max = ''
#     for i in centrality:
#         current_degree = centrality[i]
#         if current_degree > max_degree:
#             max_degree = current_degree
#             node_degree_with_max = i
#     print("Eigen Vector with most central node is : " + str(node_degree_with_max))

