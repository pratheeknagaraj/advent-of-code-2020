#!/usr/bin/python3

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

count = 0
for m in message_lines:
    if m in allowed_set:
        count += 1
print(count)
