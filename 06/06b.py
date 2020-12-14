#!/usr/bin/python3

with open('06_input', 'r') as f:
    data = f.read()

groups = data.split('\n\n')

def count(group):
    persons = [p.strip() for p in group.split('\n') if p]
    all_qs = set()
    for i, person in enumerate(persons):
        if i > 0:
            all_qs = all_qs & set(person)
        else:
            all_qs = set(person)

    #print(len(all_qs))
    return len(all_qs)

print(sum([count(g) for g in groups]))
