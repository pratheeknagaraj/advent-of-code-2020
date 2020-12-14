#!/usr/bin/python3

with open('08_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

visited = set()

line_num = 0

accumulator = 0

while True:
    if line_num in visited:
        break
    visited.add(line_num)

    cur = lines[line_num]
    inst, num = cur.split()

    #print(cur, accumulator)
    
    if inst == 'nop':
        line_num += 1
    elif inst == 'acc':
        accumulator += int(num)
        line_num += 1
    elif inst == 'jmp':
        line_num += int(num)

print(accumulator)
