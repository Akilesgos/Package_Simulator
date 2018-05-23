import sys
from Network import Network
from Package import Package

args = sys.argv

iteration_results = []

for number in args[2]:
    package = Package()
    network = Network(args[1])
    network.chain[5].send_package(package.name)
    list_of_packages = list(map(lambda x: x.package, network.chain))
    filter_list_of_packeges = list(filter(lambda x: x == None, list_of_packages))
    deliver_percent = 100-(len(filter_list_of_packeges)*100/len(list_of_packages))
    iteration_results.append(deliver_percent)

sum_iteratin_results = sum(iteration_results)/len(iteration_results)
print('In {sum_iteratin_results} % cases all nodes recive package'.format(sum_iteratin_results=sum_iteratin_results))






