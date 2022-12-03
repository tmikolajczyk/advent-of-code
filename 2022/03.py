from string import ascii_lowercase as small
from string import ascii_uppercase as capital
from aocd import get_data, submit
import numpy as np


day = 3
year = 2022
data = get_data(day=day, year=year)

letters = list(small)
letters.extend(list(capital))
letters = {l: ind+1 for ind, l in enumerate(letters)}


result1 = 0
for d in data.split('\n'):
    letter = np.intersect1d(list(d[:int(len(d)/2)]), list(d[int(len(d)/2):]))
    result1 += letters.get(letter[0])
submit(result1)


result2 = 0
lst = data.split('\n')
for i in range(0, len(lst), 3):
    chunk = lst[i:i + 3]
    letter = [*set.intersection(*map(set, chunk))][0]
    result2 += letters.get(letter[0])
submit(result2)
        
