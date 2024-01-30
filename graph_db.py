import json
from uuid import uuid4
import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass


class Node:
    """
    This is a node class that represents a node/entity in a graph.
    """
    def __init__(self, name):
        self.id = str(uuid4().hex[:6])
        self.name = name
        

class Edge:
    """
    This is an edge class that represents the relationship between two nodes.
    """
    def __init__(self, source: Node, target: Node, data):
        self.id = str(uuid4().hex[:6])
        self.source = source
        self.target = target
        self.data = data


class Graph:
    """
    This is a graph class that represents a graph database.
    """
    def __init__(self, description: str):
        self.description = description
        self.nodes = {}
        self.edges = []
    
    def add_node(self, node: Node):
        self.nodes[node.id] = node
    
    def add_edge(self, edge: Edge):
        self.edges.append(edge)


def visualize_graph(graph: Graph):
    """
    Visualize the graph using networkx and matplotlib
    
    Args: graph (Graph): The graph to be visualized
    """
    G = nx.Graph()
    for node in graph.nodes.values():
        G.add_node(node.id, name=node.name)
    for edge in graph.edges:
        G.add_edge(edge.source.id, edge.target.id, relation=edge.data['relation'])
    nx.draw(G, font_weight='bold', labels=nx.get_node_attributes(G, 'name'))
    plt.show()


def main():
    """Graph testing --main function"""
    graph = Graph("Test1")
    node1 = Node("Node1")
    node2 = Node("Node2")
    node3 = Node("Node3")
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    edge1 = Edge(node1, node2, {"relation": "edge1"})
    edge2 = Edge(node2, node3, {"relation": "edge2"})
    graph.add_edge(edge1)
    graph.add_edge(edge2)
    visualize_graph(graph)


if __name__ == '__main__':
    main()