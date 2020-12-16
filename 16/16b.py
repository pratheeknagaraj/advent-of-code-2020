#!/usr/bin/python3

with open('16_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

ranges = lines[:lines.index('')]
my_ticket = lines[lines.index('your ticket:')+1]
nearby_tickets = lines[lines.index('nearby tickets:')+1:]

valid_nums = set()
valid_fields = dict()

for l in ranges:
    field, ranges = l.split(':')
    parts = ranges.strip().split()
    front, back = parts[0], parts[2]
    
    f_i, f_j = front.split('-')
    b_i, b_j = back.split('-')
    f_i, f_j = int(f_i), int(f_j)
    b_i, b_j = int(b_i), int(b_j)

    allowed_nums = set(range(f_i, f_j+1)).union(set(range(b_i, b_j+1)))
    
    valid_nums.update(set(range(f_i, f_j+1)))
    valid_nums.update(set(range(b_i, b_j+1)))

    valid_fields[field] = allowed_nums

ticket_len = len(nearby_tickets[0].split(','))
positions = []
for i in range(ticket_len):
    positions.append(set(valid_fields.keys()))

#print(positions)

valid_tickets = []

for nearby_ticket in nearby_tickets:
    invalid = False
    nums = [int(n) for n in nearby_ticket.split(',')]
    for n in nums:
        if n not in valid_nums:
            invalid = True
    if not invalid:
        valid_tickets.append(nums)

#print(valid_tickets)

for valid_ticket in valid_tickets:
    for pos, num in enumerate(valid_ticket):
        choices = list(positions[pos])
        for c in choices:
            if num not in valid_fields[c]:
                positions[pos].remove(c)
                #print(pos, c, num)
#print(positions)

# Eliminations

selected = set()

finished = False
while not finished:
    finished = True
    for elem in positions:
        if len(elem) == 1:
            selected.add(next(iter(elem)))
        else:
            finished = False
            for rem in list(elem):
                if rem in selected:
                    elem.remove(rem)

#print(positions)

final_fields = []
for pos in positions:
    final_fields.append(next(iter(pos)))

departure_keys = [f for f in valid_fields.keys() if f.startswith('departure')]

indicies = [final_fields.index(k) for k in departure_keys]

my_nums = [int(n) for n in my_ticket.split(',')]
depart_nums = [my_nums[i] for i in indicies]

product = 1
for d in depart_nums:
    product *= d
print(product)
