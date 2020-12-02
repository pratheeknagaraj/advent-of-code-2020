#!/usr/bin/python3

with open('02_input', 'r') as f:
    lines = f.readlines()

passwords = [p.strip() for p in lines]

valid_count = 0

for line in passwords:
    parts = line.strip().split()
    cts = parts[0].split('-')

    # Not zero-indexed
    pos1, pos2 = int(cts[0]) - 1, int(cts[1]) - 1

    letter = parts[1][0]
    string = parts[2]

    string_count = (letter == string[pos1]) + (letter == string[pos2])
    if string_count == 1:
        valid_count += 1

print(valid_count)
