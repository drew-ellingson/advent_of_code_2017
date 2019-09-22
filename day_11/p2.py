from collections import Counter
import math

with open('input.txt') as my_file:
    steps = my_file.readline().strip('\n').split(',')

max_value = 0
for n in range(len(steps)):
    substeps = steps[0:n]
    step_hist = Counter(substeps)

    north = step_hist['n'] - step_hist['s']
    ne = step_hist['ne'] - step_hist['sw']
    nw = step_hist['nw'] - step_hist['se']

    val = north + abs(ne-nw) + min(ne, nw)

    max_value = max(max_value, val)

print(max_value)
