def one_step(knot, length, skip_size, current_pos):
    """one step of the knot hash algorithm"""
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


def list_xor(hash_block):
    """extends ^ to list of inputs"""
    output = hash_block[0]
    for x in range(1, len(hash_block)):
        output = output ^ hash_block[x]
    return output


def make_hash(input):
    ascii_input = [ord(n) for n in input]
    line = ascii_input + [17, 31, 73, 47, 23]
    knot = list(range(256))
    current_pos = 0
    skip_size = 0

    for hash_round in range(64):
        for item in line:
            knot, skip_size, current_pos = one_step(knot, item, skip_size, current_pos)

    sparse_hash = knot
    block_sparse_hash = [sparse_hash[16*i:16*i+16] for i in list(range(16))]

    dense_hash = [list_xor(hash_block) for hash_block in block_sparse_hash]
    hex_dense_hash = [hex(num)[2:] for num in dense_hash]

    return(''.join(hex_dense_hash))


with open('input.txt') as my_file:
    hash_seed = my_file.readline().strip('\n')

print(hash_seed)

print(make_hash(hash_seed))
