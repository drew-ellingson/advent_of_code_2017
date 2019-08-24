with open('input.txt') as my_file:
    line = [int(n) for n in my_file.readline().split(',')]

knot = list(range(256))
current_pos = 0
skip_size = 0


def one_step(knot, length, skip_size, current_pos):
    doubled_knot = knot + knot
    reverse_section = doubled_knot[current_pos: current_pos+length]
    reverse_section.reverse()
    flipped_db_knot = doubled_knot[:current_pos] + reverse_section + doubled_knot[current_pos + length:]
    output = [0] * len(knot)
    for i in range(len(knot)):
        output[(current_pos + i) % len(knot)] = flipped_db_knot[current_pos + i]
    current_pos = (current_pos + length + skip_size) % len(knot)
    skip_size += 1

    return output, skip_size, current_pos


for item in line:
    knot, skip_size, current_pos = one_step(knot, item, skip_size, current_pos)

print(knot[0] * knot[1])
