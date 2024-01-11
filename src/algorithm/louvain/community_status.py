# coding=utf-8


class Status(object):
    """
    To handle several data in one struct.

    Could be replaced by named tuple, but don't want to depend on python 2.6
    """
    node2com = {}
    total_weight = 0 # actually weight equals number of links
    internals = {}
    degrees = {}
    in_degrees = {}
    out_degrees = {}
    gdegrees = {}
    in_gdegrees = {}
    out_gdegrees = {}

    def __init__(self):
        self.node2com = dict([])
        self.total_weight = 0
        self.degrees = dict([])
        self.in_degrees = dict([])
        self.out_degrees = dict([]) # for community


        self.gdegrees = dict([]) # for node
        self.in_gdegrees = dict([])
        self.out_gdegrees = dict([])

        self.internals = dict([])
        self.loops = dict([])

    def __str__(self):
        return ("node2com : " + str(self.node2com) + " degrees : "
                + str(self.degrees) + " internals : " + str(self.internals)
                + " total_weight : " + str(self.total_weight))

    def copy(self):
        """Perform a deep copy of status"""
        new_status = Status()
        new_status.node2com = self.node2com.copy()
        new_status.internals = self.internals.copy()
        new_status.degrees = self.degrees.copy()
        new_status.in_degrees = self.in_degrees.copy()
        new_status.out_degrees = self.out_degrees.copy()
        new_status.gdegrees = self.gdegrees.copy()
        new_status.in_gdegrees = self.in_gdegrees.copy()
        new_status.out_gdegrees = self.out_gdegrees.copy()
        new_status.total_weight = self.total_weight

    def init(self, graph, weight, part=None):
        """Initialize the status of a graph with every node in one community"""
        count = 0
        self.node2com = dict([])
        self.total_weight = 0
        self.degrees = dict([])
        self.gdegrees = dict([])

        self.in_degrees = dict([])
        self.out_degrees = dict([])
        self.in_gdegrees = dict([])
        self.out_gdegrees = dict([])

        self.internals = dict([])
        self.total_weight = graph.size(weight=weight)
        if part is None:
            for node in graph.nodes():
                self.node2com[node] = count
                deg = float(graph.degree(node, weight=weight))
                if deg < 0:
                    error = "Bad node degree ({})".format(deg)
                    raise ValueError(error)
                self.degrees[count] = deg

                self.gdegrees[node] = deg
                in_deg = float(graph.in_degree(node, weight=weight))
                self.in_degrees[count] = in_deg
                self.in_gdegrees[node] = in_deg

                out_deg = float(graph.out_degree(node, weight=weight))
                self.out_degrees[count] = out_deg
                self.out_gdegrees[node] = out_deg

                edge_data = graph.get_edge_data(node, node, default={weight: 0})
                self.loops[node] = float(edge_data.get(weight, 1))
                self.internals[count] = self.loops[node]
                count += 1
        else:
            for node in graph.nodes():
                com = part[node]
                self.node2com[node] = com
                deg = float(graph.degree(node, weight=weight))
                self.degrees[com] = self.degrees.get(com, 0) + deg
                self.gdegrees[node] = deg

                in_deg = float(graph.in_degree(node, weight=weight))
                self.in_degrees[com] = self.in_degrees.get(com, 0) +in_deg
                self.in_gdegrees[node] = in_deg

                out_deg = float(graph.out_degree(node, weight=weight))
                self.out_degrees[com] = self.out_degrees.get(com, 0) + out_deg
                self.in_gdegrees[node] = out_deg

                inc = 0.
                for neighbor, datas in graph[node].items():
                    edge_weight = datas.get(weight, 1)
                    if edge_weight <= 0:
                        error = "Bad graph type ({})".format(type(graph))
                        raise ValueError(error)
                    if part[neighbor] == com:
                        if neighbor == node:
                            inc += float(edge_weight)
                        else:
                            inc += float(edge_weight) / 2.
                self.internals[com] = self.internals.get(com, 0) + inc