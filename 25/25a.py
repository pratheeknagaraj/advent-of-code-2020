#!/usr/bin/python3

with open('25_input', 'r') as f:
    lines = f.readlines()

p1 = int(lines[0].strip())
p2 = int(lines[1].strip())
#print(p1, p2)

def find_loop_num(subj_num, pub_num):
    limit = 10000000
    divisor = 20201227
    for i in range(limit):
        rem = pow(subj_num, i, divisor)
        if rem == pub_num:
            return i
    return None

subj_num = 7
loop1 = find_loop_num(subj_num, p1)
loop2 = find_loop_num(subj_num, p2)
#print(loop1, loop2)

divisor = 20201227
enc_key = pow(p1, loop2, divisor)
print(enc_key)
