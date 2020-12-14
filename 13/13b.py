#!/usr/bin/python3

with open('13_input', 'r') as f:
    lines = f.readlines()

lines = lines[1:]

def mod_mult_inv(a, n):
    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr

    if r > 1:
        return None
    if t < 0:
        return t + n

    return t

def solve(bus_times):
    # bus times are relatively co-prime, use Chinese Remainder Theorem

    total = 0

    ids = [i[0] for i in bus_times]
    product = 1
    for i in ids:
        product *= i

    n = ids
    a = [i[0] - i[1] for i in bus_times]
    y = [product // n_i for n_i in n]
    z = [mod_mult_inv(y_i, n_i) for (y_i, n_i) in zip(y, n)]

    total = sum([a_i * y_i * z_i for (a_i, y_i, z_i) in zip(a, y, z)])
    return total % product

for line in lines:
    bus_list = line.strip().split(',')
    bus_times = [(int(i), t) for t, i in enumerate(bus_list) if i.isnumeric()]

    print(solve(bus_times))

