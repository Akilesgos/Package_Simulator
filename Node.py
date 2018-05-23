from random import randint, shuffle

class Node:
    def __init__(self):
        self.package = None
        self.known_nodes = []
        self.name = (
            '{first}.{second}.{third}.{four}'.format(first=randint(0, 255),
                                                     second=randint(0, 255),
                                                     third=randint(0, 255),
                                                     four=randint(0, 255)))

    def send_package(self, package):
        print('Node name ${node_name}, received package ${package}'.format(node_name=self.name, package=package))
        if self.package == package: # что ты себе не  
          print('i"ve alredy had package')
          return  

        self.package = package
        container = (len(self.known_nodes) - 1)
        shuffle(self.known_nodes)

        
        for node in self.known_nodes[0:4]:
            print('Sending package to ${other_node}'.format(other_node=node))
            node.send_package(package)


    def update_known_nodes(self, nodes):
        self.known_nodes = list(nodes)
        self.known_nodes.remove(self) 
    
    
        