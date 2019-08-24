import math

with open('input.txt') as my_file:
    input_num = int(my_file.readline())

east_west_steps = []
north_south_steps = []
addresses = [(1, 0, 0, 1)]  # number, x_val, y_val, sum value

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


def adjacent(addr1, addr2):
    """ tell if two addresses are adjancent via edge or corner """
    if abs(addr1[1] - addr2[1]) <= 1 and abs(addr1[2]-addr2[2]) <= 1 and addr1 != addr2:
        return True
    return False


am_i_done = False
x = 0

while not am_i_done:
    x += 1
    prev_addr = addresses[x-1]

    intm_new_addr = (x+1,
                     prev_addr[1] + east_west_steps[x-1],
                     prev_addr[2] + north_south_steps[x-1],
                     0
                     )

    new_addr = (intm_new_addr[0],
                intm_new_addr[1],
                intm_new_addr[2],
                sum([cand[3] if adjacent(cand, intm_new_addr) else 0 for cand in addresses[0:x]])
                )

    addresses.append(new_addr)

    if new_addr[3] > input_num:
        print(new_addr[3])
        am_i_done = True

print(addresses)
