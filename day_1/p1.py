with open('input.txt') as p1_input:
    input_str = str(p1_input.readlines()[0])

my_sum = 0

for x in range(0, len(input_str)):
    curr_num = int(input_str[x])
    next_num = (int(input_str[0]) if x == len(input_str)-1
                else int(input_str[x+1]))

    if curr_num == next_num:
        my_sum += curr_num

print(my_sum)
