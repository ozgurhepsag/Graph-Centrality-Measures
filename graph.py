import vertex as Vertex


class graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        if key not in self.vertices:
            vertex = Vertex.vertex(key)
            self.vertices[key] = vertex

    def remove_vertex(self, key):
        self.vertices.pop(key)

    def get_vertex(self, key):
        return self.vertices[key]

    def get_vertex_number(self):
        return self.vertices.__len__()

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, src_key, dest_key, weight=1):
        if src_key not in self.vertices:
            print('Vertex {} does not exist.'.format(src_key))
        elif dest_key not in self.vertices:
            print('Vertex {} does not exist.'.format(dest_key))
        else:
            if (not self.does_edge_exist(src_key, dest_key)) and \
                    (not self.does_edge_exist(dest_key, src_key)):
                self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
                self.vertices[dest_key].add_neighbour(self.vertices[src_key], weight)
            else:
                print('Edge already exist.')

    def does_edge_exist(self, src_key, dest_key):
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def __iter__(self):
        return iter(self.vertices.values())
