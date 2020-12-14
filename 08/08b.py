#!/usr/bin/python3

with open('08_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

def run(lines):
    visited = set()

    line_num = 0

    accumulator = 0

    success = True

    while True:
        if line_num in visited:
            success = False
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

        if line_num >= len(lines):
            break

    return(accumulator, success)

programs = []

for i, line in enumerate(lines):
    if line.startswith('nop'):
        program = lines[:i] + [line.replace('nop', 'jmp')] + lines[i+1:]
        programs.append(program)
    elif line.startswith('jmp'):
        program = lines[:i] + [line.replace('jmp', 'nop')] + lines[i+1:]
        programs.append(program)

for program in programs:
    num, res = run(program)
    if res:
        print(num)
        break
