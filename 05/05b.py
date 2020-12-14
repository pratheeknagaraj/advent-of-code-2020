#!/usr/bin/python3

with open('05_input', 'r') as f:
    lines = f.readlines()

lines = [r.strip() for r in lines]

def get_seat_id(code):
    row_str = code[0:7]
    col_str = code[7:10]
    row_num = row_str.replace('F','0').replace('B','1')
    col_num = col_str.replace('L','0').replace('R','1')
    row = int(row_num, 2)
    col = int(col_num, 2)
    seat_id = row * 8 + col
    #print(row, col, seat_id)
    return seat_id

seat_ids = [get_seat_id(code) for code in lines]
seat_ids = sorted(seat_ids)

first, last = seat_ids[0], seat_ids[-1]
missing = set(range(first, last+1)) - set(seat_ids)
print(next(iter(missing)))
