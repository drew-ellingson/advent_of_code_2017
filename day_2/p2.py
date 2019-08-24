# making assumption of distinct values in a given line
def line_division(line):
    quotients = [[int(x / y) if x % y == 0 else 0 for x in line] for y in line]
    flat_quotients = [item for row in quotients for item in row]
    return max(flat_quotients)


with open('input.txt') as input_file:
    lines = [line.strip('\n').split('\t') for line in input_file.readlines()]
    lines = [[int(x) for x in line] for line in lines]

my_sum = sum(map(line_division, lines))

print(my_sum)
