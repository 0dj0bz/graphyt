#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: robabbott

Graphyt

A somewhat elegant and efficient Graph class

Copyright 2016-2019, Robert L. Abbott

"""

import uuid

class Node():
    """
    Class - Node
    
    This is the Node class that supports the Graph class.
            
    The '_' dict enables user-defined name-value pairs to be stored at the
        Node level.
    """
    
    def __init__(self, label=None, metric=1.0):
        self._id = str(uuid.uuid4())
        if label is None:
            self.label = str(self._id)
        else:
            self.label = label
            
        self.edges = {}
        self.metric = metric
        self._ = {}
        
    def add_membership(self, edge):
        self.edges[edge._id] = edge
        
    def delete_membership(self, edge):
        print('Node: in delete_membership')
        try:
            del self.edges[edge._id]
        except KeyError:
            pass        
        
# End nested class Node        
       
class Edge():
    """
    Class - Edge
    
    This is the Edge class that supports the Graph class.
    
    This class depends upon the Node class.
    The src and dst attributes are instances of the Node class
    An Edge MUST have both a src and a dst Node
    
    The '_' dict enables user-defined name-value pairs to be stored at the
        Edge level. 
                
    """
    
    def __init__(self, src=None, dst=None, label=None, metric=None):
        self._id = str(uuid.uuid4())
        self.src = src
        src.add_membership(self)
        self.dst = dst
        dst.add_membership(self)
        
        if label is None:
            self.label = str(self._id)        
        else:
            self.label = label
            
        self.metric = metric 
        self._ = {}
        
    def __del__(self):
        print('Edge: in __del__')
        self.src.delete_membership(self)
        self.dst.delete_membership(self)

        

# End nested class Edge

    
class Graph():
    """
    Class - Graph
    
    This is the Graph class.
    
    A Graph object is a collection of Node objects that may be joined by 
        Edge objects
        
    The nodes dict has the following structure:
        
        { node1._id:{node:node1, edges:[edge1, edge2, ...]}, ...}
        
    The purpose of this layout is to enable quickly finding the Edge
        objects that a Node participates in.
        
    The edges dict has the following structure:
        
        { edge._id:{src:node1, dst:node2, edge:edge}, ... }
        
    This enables efficient search and retrieval of an Edge and its
        corresponding Node objects.
        
    The '_' dict enables user-defined name-value pairs to be stored at the
        Graph level.
        
    """
    
    
    # Begin Graph class function definitions
    
    def __init__(self, nodes={}, edges={}, label=None):
        self._id = str(uuid.uuid4())
        
        if label is None:
            self.label = str(self._id)        
        else:
            self.label = label
            
        self.nodes = {}
        self.edges = {}
        self._ = {}
        
    def add_node(self, node=None):
        """
        add_node    - adds a new Node object to a Graph
                    - takes a dict parameter with the attributes of the 
                        Node to be added:
                            {'label':<str>, 'metric':<float>}
                        
        """
        
        if node is None:
            return None
        
        # option 1 - node is a single Node object to add to Graph             
        if type(node) == Node:
            self.nodes[node._id] = node
            return node._id
            
        # option 2 - node is a dict that contains the proprties to create
        #               a new node
        if type(node) == dict:
            n = Node()
            self.nodes[n._id] = n
            n_id = n._id
            return n_id
            
    def delete_node(self, node=None):
        # TODO: make sure that the Node isn't part of an existing Edge
        if node is not None:
            try:
                del self.nodes[node._id]
            except KeyError:
                pass

    def add_edge(self, edge):
               
        # edge is a single Edge object to add to Graph             
        if type(edge) == Edge:
            self.edges[edge._id] = {'src':edge.src,'dst':edge.dst,'edge':edge}
            
        return edge._id
            
    def delete_edge(self, edge=None):
        """
        delete_edge - deletes an Edge from the edges dict
        """
        if edge is not None:
            try:
                edge.src.delete_membership(edge)
                edge.dst.delete_membership(edge)
                del edge
            
            except KeyError:
                pass
        
    def add_subgraph(self, nodes, edges, update=False):
        """
        add_subgraph() - idempotently add Nodes and Edges to the current Graph
            nodes  - list of Node objects to add to Graph
            edges  - list of Edge objects to add to Graph
            update - if False, do not update existing Node and Edge objects
                     already in Graph; if True, update (clobber) existing
        """
        pass

if __name__ == "__main__":
    
    print('Creating graph...')
    g1 = Graph()
    print('g1.label: ', g1.label)
    print('Creating nodes...')
    n1 = Node()
    _id = g1.add_node(n1)
    print('Node n1: ', g1.nodes[_id])
    n2 = Node()
    _id = g1.add_node(n2)
    print('Node n2: ', g1.nodes[_id])
    
    
    e1 = Edge(n1, n2)

        
#    print('Edge e1: ', e1.label)
##    print('e1.src: ', e1.src.label)
##    print('e1.dst: ', e1.dst.label)
##    print('Creating edge e2...')
#    e2 = Edge(n1, n2)
#    print('Edge e2: ', e2.label)
#    
#    e2 = e1
    
#    print('e2.src: ', e1.src.label)
#    print('e2.dst: ', e1.dst.label)

#    print('Adding n1 to g1...')
#    g1.add_node(n1)
#    print('g1.nodes: ', g1.nodes)
#    print('Adding n2 to g1...')
#    g1.add_node(n2)
#    print('g1.nodes: ', g1.nodes)
#    print('Adding e1 to g1...')
#    g1.add_edge(e1)
#    print('g1.edges: ', g1.edges)

#    print('Delete e1 from g1...')
#    g1.delete_edge(e1)
    
    
#    print('g1.edges: ', g1.edges)
#    print('Delete n1 from g1...')
#    g1.delete_node(n1)
#    print('g1.nodes: ', g1.nodes)
#    print('Delete n2 from g1...')
#    g1.delete_node(n2)
#    print('g1.nodes: ', g1.nodes)
#    print('Exercise complete!')

