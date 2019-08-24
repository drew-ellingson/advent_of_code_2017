with open('input.txt') as p1_input:
    input_str = str(p1_input.readlines()[0])

my_sum = 0
input_len = len(input_str)
class_reps = int(len(input_str)/2)

for x in range(0, class_reps):
    curr_num = int(input_str[x])
    next_num = int(input_str[x+class_reps])

    if curr_num == next_num:
        my_sum += curr_num

print(2*my_sum)
