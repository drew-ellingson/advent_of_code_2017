with open('input.txt') as my_file:
    lines = [line.strip('\n').split(' <-> ') for line in my_file.readlines()]
    graph_dict = {int(line[0]):[int(pipe) for pipe in line[1].split(', ')] for line in lines}

connected_to_0 = [0]

""" thinking of this as a walk on a graph, adds the nodes one step further"""
def add_layer(_graph_dict, _connected_nodes):
    for node in _connected_nodes:
        _connected_nodes = _connected_nodes + _graph_dict[node]
    return list(set(_connected_nodes))


stable = False  # iterate until orbit remains unchanged under add_layer

while not stable:
    next_step_nodes = add_layer(graph_dict, connected_to_0)
    if set(next_step_nodes) == set(connected_to_0):
        stable = True
    connected_to_0 = next_step_nodes

print(len(connected_to_0))
