
from aocd import get_data, submit
import numpy as np

day = 1
year = 2022
data = get_data(day=day, year=year)

result1 = [sum([int(b) for b in a.split('\n')]) for a in data.split('\n\n')]
submit(max(result1))

result2 = np.sum(np.sort(result1)[-3:])
submit(result2)