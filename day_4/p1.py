from collections import Counter

with open('input.txt') as my_file:
    lines = [line.strip('\n').split(' ') for line in my_file]

valid_phrases = list(filter(lambda line: set(Counter(line).values()) == {1}, lines))

print(len(valid_phrases))
