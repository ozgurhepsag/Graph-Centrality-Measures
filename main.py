from utility_functions import *
from centrality_functions import *
import networkx as nx
from graph import *

g = graph()

key1 = 'Louisa Clark'
key2 = 'Will Traynor'
key3 = 'Nathan'
key4 = 'Camilla Traynor'
key5 = 'Steven Traynor'
key6 = 'Josie Clark'
key7 = 'Bernard Clark'
key8 = 'Katrina Clark'
key9 = 'Patrick'
key10 = 'Georgina'


def main():

    fill_graph()

    print('Menu')
    print('1 - Degree Centrality')
    print('2 - Closeness Centrality')
    print('3 - Eccentricity Centrality')
    print('4 - Betweenness Centrality')
    print('5 - Eigen Centrality')
    print('6 - Quit')

    while True:
        input_val = input('Which centrality would you like to run? ').split()
        print("-  -  -  -  -  -  -  -  -  -  -  -  -  - ")
        print()
        operation = input_val[0]

        if operation == '1':
            print("Degree Centrality")
            degree_dict = find_degree_centrality(g)
            print_centrality_result(degree_dict)
        elif operation == '2':
            print("Closeness Centrality")
            closeness_dict = find_closeness_centrality(g)
            print_centrality_result(closeness_dict)
        elif operation == '3':
            print("Eccentricity Centrality")
            eccentricity_dict = find_eccentricity_centrality(g)
            print_centrality_result(eccentricity_dict)
        elif operation == '4':
            print("Betweenness Centrality")
            betweenness_dict = find_betweenness_centrality(g)
            print_centrality_result(betweenness_dict)
        elif operation == '5':
            print("Eigen Vector Centrality")
            find_eigenvector_centrality_numpy(g)
        elif operation == '6':
            quit()
        else:
            raise Exception("Value error")


def print_centrality_result(result_dict):
    for i in result_dict:
        print("Node : " + i.get_key() + " Values : " + str(round(result_dict[i], 2)))

    print("The node which has higher degree than other vertex is : " + str(find_vertex_has_most_degree(result_dict)))
    print()


def fill_graph():
    g.add_vertex(key1)
    g.add_vertex(key2)
    g.add_vertex(key3)
    g.add_vertex(key4)
    g.add_vertex(key5)
    g.add_vertex(key6)
    g.add_vertex(key7)
    g.add_vertex(key8)
    g.add_vertex(key9)
    g.add_vertex(key10)

    g.add_edge(key1, key2)  # A B
    g.add_edge(key1, key3)
    g.add_edge(key1, key4)
    g.add_edge(key1, key5)
    g.add_edge(key1, key6)
    g.add_edge(key1, key7)
    g.add_edge(key1, key8)
    g.add_edge(key1, key9)
    g.add_edge(key1, key10)
    g.add_edge(key2, key3)
    g.add_edge(key2, key4)
    g.add_edge(key2, key5)
    g.add_edge(key2, key6)
    g.add_edge(key2, key7)
    g.add_edge(key2, key9)
    g.add_edge(key2, key10)
    g.add_edge(key3, key4)
    g.add_edge(key3, key5)
    g.add_edge(key4, key5)
    g.add_edge(key4, key10)
    g.add_edge(key5, key10)
    g.add_edge(key6, key7)
    g.add_edge(key6, key8)
    g.add_edge(key6, key9)
    g.add_edge(key7, key8)
    g.add_edge(key7, key9)
    g.add_edge(key8, key9)


# def fill_networkx():
#     # Networkx Graph is created for calculating eigen vector centrality
#     G = nx.Graph()
#
#     G.add_edge(key1, key2)
#     G.add_edge(key1, key3)
#     G.add_edge(key1, key4)
#     G.add_edge(key1, key5)
#     G.add_edge(key1, key6)
#     G.add_edge(key1, key7)
#     G.add_edge(key1, key8)
#     G.add_edge(key1, key9)
#     G.add_edge(key1, key10)
#     G.add_edge(key2, key3)
#     G.add_edge(key2, key4)
#     G.add_edge(key2, key5)
#     G.add_edge(key2, key6)
#     G.add_edge(key2, key7)
#     G.add_edge(key2, key9)
#     G.add_edge(key2, key10)
#     G.add_edge(key3, key4)
#     G.add_edge(key3, key5)
#     G.add_edge(key4, key5)
#     G.add_edge(key4, key10)
#     G.add_edge(key5, key10)
#     G.add_edge(key6, key7)
#     G.add_edge(key6, key8)
#     G.add_edge(key6, key9)
#     G.add_edge(key7, key8)
#     G.add_edge(key7, key9)
#     G.add_edge(key8, key9)
#
#     return G

if __name__ == '__main__':
    main()
