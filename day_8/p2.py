with open('input.txt') as my_file:
    lines = [line.strip('\n').split(' ') for line in my_file.readlines()]

registers = list(set([line[0] for line in lines])
                 | set([line[4] for line in lines]))

reg_dict = {reg: 0 for reg in registers}


def compare(comp_list, reg_dict):
    """takes in [reg, comp, val] and returns true or false"""
    reg, comp, val = comp_list[0], comp_list[1], int(comp_list[2])
    if comp == '>':
        return reg_dict[reg] > val
    elif comp == '>=':
        return reg_dict[reg] >= val
    elif comp == '==':
        return reg_dict[reg] == val
    elif comp == '!=':
        return reg_dict[reg] != val
    elif comp == '<=':
        return reg_dict[reg] <= val
    elif comp == '<':
        return reg_dict[reg] < val
    else:
        return None


def perform_op(operation, reg_dict):
    """takes in [reg, op, val] and performs one operation"""
    reg, op, val = operation[0], operation[1], int(operation[2])
    if op == 'inc':
        reg_dict[reg] += val
    elif op == 'dec':
        reg_dict[reg] -= val
    return None


max_val = max(reg_dict.values())
for line in lines:
    if compare(line[4:], reg_dict):
        perform_op(line[0:3], reg_dict)
        max_val = max(max_val, max(reg_dict.values()))

print(max_val)
