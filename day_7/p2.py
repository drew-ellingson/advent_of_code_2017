with open('input.txt') as my_file:
    lines = [line.strip('\n').split(' ') for line in my_file.readlines()]
    lines = [{'node': line[0],
              'weight': int(line[1][1:-1]),
              'children': [] if len(line) < 3 else [child.strip(',') for child in line[3:]],
              'total_weight': 0
              } for line in lines]


def get_total_weight(node_dict):
    child_dicts = list(filter(lambda x: x['node'] in node_dict['children'], lines))
    if len(child_dicts) == 0:
        return node_dict['weight']
    else:
        return node_dict['weight'] + sum([get_total_weight(child) for child in child_dicts])


def is_balanced(node_dict):
    child_dicts = list(filter(lambda x: x['node'] in node_dict['children'], lines))
    weights = [child['total_weight'] for child in child_dicts]
    return len(set(weights)) == 1


for line in lines:
    line['total_weight'] = get_total_weight(line)

unbalanced_nodes = list(filter(is_balanced, lines))
unbalanced_children = [node['children'] for node in unbalanced_nodes]
unbalanced_children = [child for childlist in unbalanced_children for child in childlist]

problem_child = list(filter(lambda x: x['node'] not in unbalanced_children, unbalanced_nodes))

# found answer manually based on output from the below: 
print([(child['node'], child['weight'], child['total_weight']) for child in problem_child])
