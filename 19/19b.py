#!/usr/bin/python3

import re
import sys

from itertools import product

with open('19_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

split = lines.index('')

rule_lines = lines[:split]

message_lines = lines[split+1:]

rules = {}
cache = {}

def parse_rule(p):
    if '"' in p:
        return p.replace('"','')
    n = tuple([int(n) for n in p.split()])
    return n

for r in rule_lines:
    num, cond = r.split(':')
    cond = cond.strip()
    rule = []
    if '|' in cond:
        left, right = cond.split('|')
        left, right = parse_rule(left), parse_rule(right)
        rule = [left, right]
        rules[int(num)] = tuple(rule)
    elif '"' in cond:
        rule = parse_rule(cond)
        rules[int(num)] = rule
        cache[int(num)] = [rule]
    else:
        rule = [parse_rule(cond)]
        rules[int(num)] = tuple(rule)


def recurse(v):
    if v in cache:
        return cache[v]
    #print(v) 
    allowed = []
    for p in rules[v]:
        new = []
        for e in p:
            new.append(recurse(e))
        a = list(product(*new))
        b = []
        for i in a:
            b.append(''.join(i))
        allowed.append(b)

    allowed = [item for sublist in allowed for item in sublist]

    if len(allowed) > 2**30:
        #print(allowed)
        print("Match list too long")
        sys.exit(1)

    cache[v] = allowed
    return allowed

#print(rules)

allowed_set = set(recurse(0))
#print(allowed_set)

#print(f"8: {len(cache[8])}")
#print(f"11: {len(cache[11])}")
#print(f"31: {len(cache[31])}")
#print(f"42: {len(cache[42])}")

# Rule 0
# 0: 8 11

# Old Rules
# 8: 42
# 11: 42 31

# New Rules
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

match_42 = '(' + '|'.join(cache[42]) + ')'
match_31 = '(' + '|'.join(cache[31]) + ')'

#print("Match 42: ", match_42)
#print("Match 31: ", match_31)

# Old
#match_8 = match_42
#match_11 = match_42 + match_31
#match_0 = '^' + match_8 + match_11 + '$'

# New

# 42,42,42...,42,42,42,31,31,..,31,31
# Where number of 42 groups is greater than 31 groups

re_objs = []

for i in range(1,10):
    match_0 = '^' + match_42 + '+' + match_42 + f'{{{i}}}' + match_31 + f'{{{i}}}' + '$'
    re_obj = re.compile(match_0)
    re_objs.append(re_obj)
    #print("Match 0: ", match_0)

allowed = set()

for i, m in enumerate(message_lines):
    for re_obj in re_objs:
        if re_obj.search(m):
            key = (i,m)
            if key not in allowed:
                #print(m)
                allowed.add(key)

print(len(allowed))
