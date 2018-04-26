# /usr/bin/python
# coding: utf-8


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.visited_label = {}

    # DFS recursively
    def cloneGraph(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])

    # def cloneGraph(self, node):
    #     if not node:
    #         return
    #     clone_node = UndirectedGraphNode(node.label)
    #     self.clone_graph(node, clone_node)
    #     return clone_node
    #
    # def clone_graph(self, node, clone_node):
    #     if node.label not in self.visited_label:
    #         self.visited_label[node.label] = clone_node
    #         for neighbor in node.neighbors:
    #             if neighbor.label in self.visited_label:
    #                 clone_node.neighbors.append(self.visited_label[neighbor.label])
    #             else:
    #                 clone_node.neighbors.append(UndirectedGraphNode(neighbor.label))
    #         for neighbor, clone_neighbor in zip(node.neighbors, clone_node.neighbors):
    #             self.clone_graph(neighbor, clone_neighbor)
