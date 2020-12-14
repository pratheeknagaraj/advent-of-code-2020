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

    if not (1920 <= int(p['byr']) <= 2002):
        return False
    if not (2010 <= int(p['iyr']) <= 2020):
        return False
    if not (2020 <= int(p['eyr']) <= 2030):
        return False
    if 'cm' in p['hgt']:
        if not (150 <= int(p['hgt'].split('cm')[0]) <= 193):
            return False
    if 'in' in p['hgt']:
        if not (59 <= int(p['hgt'].split('in')[0]) <= 76):
            return False
    if (not p['hgt'].endswith('cm') and not p['hgt'].endswith('in')):
        return False
    hex_colors = set('0123456789abcdef')
    if not (p['hcl'].startswith('#') and len(p['hcl']) == 7 and all((h in hex_colors) for h in p['hcl'][1:])):
        return False
    if not (p['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')):
        return False
    if not (len(p['pid']) == 9 and p['pid'].isnumeric()):
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
                #print("Valid", passport)
            else:
                #print("Invalid", passport)
                pass

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
        #print("Valid", passport)
    else:
        #print("Invalid", passport)
        pass

print(valid_count)

