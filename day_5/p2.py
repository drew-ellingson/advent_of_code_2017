with open('input.txt') as my_file:
    lines = [int(line.strip('\n')) for line in my_file.readlines()]

out_of_bounds = False
current_index = 0
iterations = 0

while not out_of_bounds:
    iterations += 1
    next_index = current_index + lines[current_index]
    if next_index < 0 or next_index >= len(lines):
        out_of_bounds = True
        break

    lines[current_index] += (-1 if lines[current_index] >= 3 else 1)
    current_index = next_index

print(iterations)
