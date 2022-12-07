from collections import deque

class Graph:

    def __init__(self, node_list):
        self.node_list = node_list

    def get_neighbors(self, v):
        return self.node_list[v]
    def h(self, n):
        H = {
            'A': 10,
            'B': 8,
            'C': 5,
            'D': 7,
            'E': 3,
            'F':6,
            'G':5,
            'H':3,
            'I':1,
            'J':0
        }

        return H[n]


    def a_star_algorithm(self, start_node, stop_node):

        open_list = set([start_node])
        closed_list = set([])


        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None


            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight


                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

node_list = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3),('D', 2)],
    'C': [('E', 5),('D',1)],
    'D': [('C',1),('E',8)],
    'E':[('J',5),('I',5)],
    'F' :[('G',1),('H',7)],
    'G' :[('I',3)],
    'H':[('I',2)],
    'I':[('E',5),('J',3)]

}
graph1 = Graph(node_list)
graph1.a_star_algorithm('A', 'J')