with open('input.txt') as my_file:
    lines = [line.strip('\n').split(' ') for line in my_file.readlines()]
    lines = [{'node': line[0],
              'weight': line[1][1:-1],
              'children': [] if len(line) < 3 else [child.strip(',') for child in line[3:]]
              } for line in lines]

nodes = [line['node'] for line in lines]
children = [child for childlist in [line['children'] for line in lines]
            for child in childlist]


root_node = list(filter(lambda x: x not in children, nodes))

print(root_node)
