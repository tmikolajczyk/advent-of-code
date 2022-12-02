
from aocd import get_data, submit
import numpy as np

day = 2
year = 2022
data = get_data(day=day, year=year)

scores = {"X": 1, "Y": 2, "Z": 3}
combinations = {'A X': 3, 'A Y': 6, 'A Z': 0, 'B X': 0, 'B Y': 3, 'B Z': 6, 'C X': 6, 'C Y': 0, 'C Z': 3}
for k, v in combinations.items():
    combinations[k] = v + scores.get(k.split(" ")[-1])

result1 = sum([combinations.get(el) for el in data.split('\n')])
submit(result1)


combinations = {'A X': 0, 'A Y': 3, 'A Z': 6, 'B X': 0, 'B Y': 3, 'B Z': 6, 'C X': 0, 'C Y': 3, 'C Z': 6}
strategies = {
    'A': {'X': 3, 'Y': 1, 'Z': 2},
    'B': {'X': 1, 'Y': 2, 'Z': 3},
    'C': {'X': 2, 'Y': 3, 'Z': 1}
}
for k, v in combinations.items():
    k1, k2 = k.split(" ")
    combinations[k] = v + strategies.get(k1).get(k2)

result2 = [combinations.get(el) for el in data.split('\n')]
submit(sum(result2))
