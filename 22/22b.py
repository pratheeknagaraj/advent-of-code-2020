#!/usr/bin/python3

import time

from collections import deque

with open('22_input', 'r') as f:
    data = f.read()

p1_data, p2_data = data.split('\n\n')

class Game:

    def __init__(self, name, c1, c2):
        self.p1_deck = deque(c1)
        self.p2_deck = deque(c2)

        self.name = name
        self.sub_game_counter = 0
        self.round_num = 1

        self.seen = set()

        self.winner = None

    def state(self):
        return ','.join(str(i) for i in self.p1_deck) + '|' + ','.join(str(i) for i in self.p2_deck)

    def run(self):
        while self.p1_deck and self.p2_deck:
            state = self.state()
            if state in self.seen:
                #print("Previous state repeated, short-circuiting with Player 1 victory")
                return 1
            else:
                self.seen.add(state)

            #print(self.name)
            #print(self.round_num)
            #print(self.p1_deck)
            #print(self.p2_deck)
            #print()
            p1_play = self.p1_deck.popleft()
            p2_play = self.p2_deck.popleft()

            p1_rem = len(self.p1_deck)
            p2_rem = len(self.p2_deck)

            if p1_play <= p1_rem and p2_play <= p2_rem:
                # Create sub-game for winner
                self.sub_game_counter += 1
                #print("Creating sub-game")
                subgame_name = self.name + '-' + str(self.sub_game_counter)
                subgame = Game(subgame_name, list(self.p1_deck)[:p1_play], list(self.p2_deck)[:p2_play])
                winner = subgame.run()
                if winner == 1:
                    self.p1_deck.append(p1_play)
                    self.p1_deck.append(p2_play)
                else:
                    self.p2_deck.append(p2_play)
                    self.p2_deck.append(p1_play)
            elif p1_play > p2_play:
                self.p1_deck.append(p1_play)
                self.p1_deck.append(p2_play)
            else:
                self.p2_deck.append(p2_play)
                self.p2_deck.append(p1_play)
            self.round_num += 1
            #time.sleep(0.1)
        if self.p1_deck:
            return 1
        else:
            return 2


p1_cards = [int(c.strip()) for c in p1_data.split('\n')[1:] if c]
p2_cards = [int(c.strip()) for c in p2_data.split('\n')[1:] if c]

game = Game("1", p1_cards, p2_cards)
winner_num = game.run()

winner = game.p1_deck if winner_num == 1 else game.p2_deck
bottom_to_top = list(winner)[::-1]
score = sum([(i+1)*c for i,c in enumerate(bottom_to_top)])

print(score)
