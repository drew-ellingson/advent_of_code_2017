with open('input.txt') as my_file:
    lines = [line.strip('\n').split(' <-> ') for line in my_file.readlines()]
    graph_dict = {int(line[0]):[int(pipe) for pipe in line[1].split(', ')] for line in lines}

in_a_group = []


""" thinking of this as a walk on a graph, adds the nodes one step further"""
def add_layer(_graph_dict, _connected_nodes):
    for node in _connected_nodes:
        _connected_nodes = _connected_nodes + _graph_dict[node]
    return list(set(_connected_nodes))


# building a dictionary to track orbit info
orbits = {}
for program in graph_dict.keys():
    if program in in_a_group:
        continue
    in_current_group = [program]
    stable = False  # iterate until orbit remains unchanged under add_layer
    while not stable:
        next_step_nodes = add_layer(graph_dict, in_current_group)
        if set(next_step_nodes) == set(in_current_group):
            stable = True
        in_current_group = next_step_nodes
    in_a_group = in_a_group + in_current_group
    orbits[program] = in_current_group

print(len(orbits.keys()))
