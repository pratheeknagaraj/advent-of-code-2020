#!/usr/bin/python3

with open('04_input', 'r') as f:
    lines = f.readlines()

lines = [r.strip() for r in lines]

def valid(p):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional = ['cid']

    for r in required:
        if r not in p:
            #print(f"Missing: {r}")
            return False

    return True

passports = []

passport = {}

valid_count = 0

for line in lines:
    if len(line) == 0:
        if passport:
            if valid(passport):
                valid_count += 1
                #print(passport)

            passports.append(passport)
            passport = {}
    else:
        parts = line.split()
        for part in parts:
            key, val = part.split(':')
            passport[key] = val

if passport:
    if valid(passport):
        valid_count += 1
        #print(passport)

print(valid_count)

