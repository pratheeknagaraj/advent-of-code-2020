#!/usr/bin/python3

with open('18_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

def eval2(s):
    parts = s.split()
    left = 0
    operator = '+'
    for p in parts:
        if p.isnumeric():
            if operator == '+':
                left += int(p)
            else:
                left *= int(p)
        else:
            operator = p
    return left

def recurse(s):
    start = 0
    if '(' not in s:
        return eval2(s)

    max_groups = 5
    count_groups = 0

    while '(' in s:
        pos = s.find('(', start)

        next_open = s.find('(', pos+1)
        next_close = s.find(')', pos+1)

        if next_open != -1 and next_open < next_close:
            start = next_open
        else:
            s = s[:pos] + str(recurse(s[pos+1:next_close])) + s[next_close+1:]
            #print("NEW S:", s)
            count_groups += 1

    return eval2(s)

total = 0

for l in lines:
    val = recurse(l)
    #print("VAL:", val)
    total += val

print(total)
