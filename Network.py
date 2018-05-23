from random import randint
from Node import Node

class Network(list):

    def __init__(self, number_of_nods):
        self.chain = []
        for number in range(int(number_of_nods)):
            self.chain.append(Node()) 
        for node in self.chain:
            node.update_known_nodes(self.chain)


        
    def repr(self):
        return self.chain