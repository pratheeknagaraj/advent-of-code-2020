#!/usr/bin/python3

import copy
import time

with open('21_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

ingredients_list = []
allergens_list = []

for l in lines:
    left, right = l.split('(')
    ingredients = left.strip().split()
    allergens = [a.replace(',','') for a in right.strip()[9:-1].split()]

    ingredients_list.append(ingredients)
    allergens_list.append(allergens)

#print(ingredients_list)
#print(allergens_list)

all_ingredients = set([item for sublist in ingredients_list for item in sublist])
all_allergens = set([item for sublist in allergens_list for item in sublist])

allergens_map = {a: copy.deepcopy(all_ingredients) for a in all_allergens}

allergy_ingredients = set()

def matched(allergens_map):
    return all([len(i) == 1 for i in allergens_map.values()])

iter_count = 0
while not matched(allergens_map):
    #print(allergens_map, allergy_ingredients)
    for a, i in allergens_map.items():
        if len(i) != 1:
            allergens_map[a] -= allergy_ingredients

    for a_list, i_list in zip(allergens_list, ingredients_list):
        for a in a_list:
            allergens_map[a] &= set(i_list)

    for a, i in allergens_map.items():
        if len(i) == 1:
            allergy_ingredients.add(next(iter(i)))

    iter_count += 1
    #print(iter_count)
    time.sleep(0.2)

#print(allergy_ingredients)
#print(allergens_map)

counter = 0

for i_list in ingredients_list:
    for i in i_list:
        if i not in allergy_ingredients:
            counter += 1

print(counter)
