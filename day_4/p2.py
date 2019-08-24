from collections import Counter

with open('input.txt') as my_file:
    lines = [line.strip('\n').split(' ') for line in my_file]

sorted_phrases = [[''.join(sorted(word)) for word in line] for line in lines]

good_phrases = list(filter(lambda x: len(set(x)) == len(x), sorted_phrases))

print(len(good_phrases))
