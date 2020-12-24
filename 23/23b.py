#!/usr/bin/python3

import copy

with open('23_input', 'r') as f:
    data = f.read()

cup_order = [int(i) for i in list(data.strip())]

class Cup:

    def __init__(self, num):
        self.num = num
        self.next = None
        self.lower = None

init_max = 10

# Initialize Cups

one = Cup(1)
init_cups = []
init_cups.append(one)
lower = one
for i in range(2,init_max):
    c = Cup(i)
    c.lower = lower
    init_cups.append(c)
    lower = c


#print(init_cups)
front = init_cups[cup_order[0]-1]
prev = front
for i in cup_order[1:]:
    prev.next = init_cups[i-1]
    prev = init_cups[i-1]

max_limit = 1_000_000
for i in range(init_max, max_limit+1):
    c = Cup(i)
    c.lower = lower
    lower = c
    prev.next = c
    prev = c

one.lower = lower
prev.next = front

cur = front

def print_cups(cur):
    seen = set()
    print(f'({cur.num})', end=' ')
    seen.add(cur.num)
    cur = cur.next
    while cur.next:
        if cur.num in seen:
            break
        print(f'{cur.num}', end=' ')
        seen.add(cur.num)
        cur = cur.next
    print()

def move(cur):
    p1 = cur.next
    p2 = p1.next
    p3 = p2.next
    #print(f"Picked: {p1.num}, {p2.num}, {p3.num}")

    cur.next = p3.next
    val = cur.lower
    while True:
        if val != p1 and val != p2 and val != p3:
            break
        else:
            val = val.lower
    #print(f"Destination: {val.num}")
    end = val.next
    val.next = p1
    p3.next = end
    return cur.next

moves = 10_000_000
for t in range(1, moves+1):
    #if t % 100_000 == 0:
    #    print(t)
    #print(f"Move: {t}")
    #print_cups(cur)
    cur = move(cur)
    #print()

#print_cups(cur)

n1 = one.next.num
n2 = one.next.next.num

#print(n1, n2)
print(n1 * n2)
