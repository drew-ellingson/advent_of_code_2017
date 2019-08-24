with open('input.txt') as my_file:
    init_dist = list(map(int, my_file.readline().split('\t')))


def get_max_index(any_dist):
    """return the first index of the max value in the list"""
    return any_dist.index(max(any_dist))


def redistribute(any_dist):
    """one redistribution step to other memory blocks"""
    output_dist = any_dist.copy()
    max_index = get_max_index(output_dist)
    blocks = output_dist[max_index]
    output_dist[max_index] = 0

    for x in range(blocks):
        output_dist[(max_index + x + 1) % len(output_dist)] += 1
    return output_dist


dist_hist = [init_dist]
current_hist = init_dist
duplicates = False

while not duplicates:
    next_dist = redistribute(current_hist)
    if next_dist in dist_hist:
        duplicates = True
        print(len(dist_hist) - dist_hist.index(next_dist))
        break
    dist_hist.append(next_dist)
    current_hist = next_dist
