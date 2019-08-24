with open('input.txt') as input_file:
    lines = [line.strip('\n').split('\t') for line in input_file.readlines()]
    lines = [[int(x) for x in line] for line in lines]

my_sum = sum(map(lambda line: max(line)-min(line), lines))

print(my_sum)
