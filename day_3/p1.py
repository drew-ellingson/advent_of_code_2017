import math

with open('input.txt') as my_file:
    input_num = int(my_file.readline())

east_west_steps = []
north_south_steps = []
addresses = [(1, 0, 0)]  # number, x_val, y_val

# create two lists giving the east-west and north-south movement between a
# given number and the subsequent
x = 0
while len(east_west_steps) <= input_num:
    x += 1
    for y in range(1, int(math.floor(x+1)/2)):
        if x % 4 == 1:
            east_west_steps.append(-1)
            north_south_steps.append(0)
        elif x % 4 == 3:
            east_west_steps.append(1)
            north_south_steps.append(0)
        elif x % 4 == 2:
            east_west_steps.append(0)
            north_south_steps.append(-1)
        elif x % 4 == 0:
            east_west_steps.append(0)
            north_south_steps.append(1)

for x in range(1, input_num):
    prev_addr = addresses[x-1]
    new_addr = (x+1,
                prev_addr[1] + east_west_steps[x-1],
                prev_addr[2] + north_south_steps[x-1])

    addresses.append(new_addr)

print(addresses[input_num-1])
print(sum(addresses[input_num-1][1:]))
