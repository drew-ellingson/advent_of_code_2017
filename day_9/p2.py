with open('input.txt') as my_file:
    line = my_file.readline()


def clean_exclamation(garbage):
    """remove exclamation points and subsequent character"""
    garbage = list(garbage)
    while '!' in garbage:
        index = garbage.index('!')
        garbage.pop(index)
        garbage.pop(index)
    return ''.join(garbage)


def compress_garbage(cleaner_garbage):
    """compresses any garbage to a '<>' string, and count garbage chars"""
    output_string = ''
    active_garbage = False
    garbage_count = 0
    for char in cleaner_garbage:
        if char == '>':
            active_garbage = False
        if not active_garbage:
            output_string = output_string + char
        else:
            garbage_count += 1
        if char == '<':
            active_garbage = True
    return output_string, garbage_count


def remove_commas(mostly_clean_garbage):
    """remove all commas from the trash string"""
    mostly_clean_garbage = list(mostly_clean_garbage)
    while ',' in mostly_clean_garbage:
        index = mostly_clean_garbage.index(',')
        mostly_clean_garbage.pop(index)
    return ''.join(mostly_clean_garbage)


def return_value(cleaned_string):
    """return the score of the cleaned string"""
    total_score = 0
    current_val = 0
    for char in cleaned_string:
        if char == '{':
            current_val += 1

        total_score += current_val

        if char == '}':
            current_val -= 1

    return int(total_score / 2)


garbange_count = compress_garbage(clean_exclamation(line))[1]

print(garbange_count)
