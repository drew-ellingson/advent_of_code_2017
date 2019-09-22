from collections import Counter

with open('input.txt') as my_file:
    steps = my_file.readline().strip('\n').split(',')

step_hist = Counter(steps)

north = step_hist['n'] - step_hist['s']
ne = step_hist['ne'] - step_hist['sw']
nw = step_hist['nw'] - step_hist['se']

val = north + abs(ne-nw) + min(ne, nw)

print(val)
