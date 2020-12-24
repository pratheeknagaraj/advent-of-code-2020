#!/usr/bin/python3

from collections import deque

with open('22_input', 'r') as f:
    data = f.read()

p1_data, p2_data = data.split('\n\n')

p1_cards = [int(c.strip()) for c in p1_data.split('\n')[1:] if c]
p2_cards = [int(c.strip()) for c in p2_data.split('\n')[1:] if c]

p1_deck = deque(p1_cards)
p2_deck = deque(p2_cards)

round_num = 1
while p1_deck and p2_deck:
    #print(round_num)
    #print(p1_deck)
    #print(p2_deck)
    p1_play = p1_deck.popleft()
    p2_play = p2_deck.popleft()
    if p1_play > p2_play:
        p1_deck.append(p1_play)
        p1_deck.append(p2_play)
    else:
        p2_deck.append(p2_play)
        p2_deck.append(p1_play)
    round_num += 1

winner = p1_deck if p1_deck else p2_deck
bottom_to_top = list(winner)[::-1]
score = sum([(i+1)*c for i,c in enumerate(bottom_to_top)])
print(score)
