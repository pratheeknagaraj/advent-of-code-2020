#!/usr/bin/python3

with open('02_input', 'r') as f:
    lines = f.readlines()

passwords = [p.strip() for p in lines]

valid_count = 0

for line in passwords:
    parts = line.strip().split()
    cts = parts[0].split('-')
    min_count, max_count = int(cts[0]), int(cts[1])
    letter = parts[1][0]
    string = parts[2]

    letter_count = string.count(letter)
    #print(min_count, max_count, letter, string, letter_count)
    if min_count <= letter_count <= max_count:
        valid_count += 1

print(valid_count)
