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
    """compresses any garbage to a '<>' string"""
    output_string = ''
    active_garbage = False
    for char in cleaner_garbage:
        if char == '<':
            active_garbage = True
        if not active_garbage:
            output_string = output_string + char
        if char == '>':
            active_garbage = False
    return output_string


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


clean_line = remove_commas(compress_garbage(clean_exclamation(line)))
print(return_value(clean_line))
