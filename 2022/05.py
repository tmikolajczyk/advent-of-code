from aocd import get_data, submit
import numpy as np
import re

day = 5
year = 2022
data = get_data(day=day, year=year)

cranes = data.split("\n\n")[0]
instr = data.split("\n\n")[1]

all = [[] for i in range(9)]
for line in cranes.split("\n")[:-1]:
    line = list(line[1::4])
    for indx in range(len(all)):
        if not line[indx] == ' ':
            all[indx].append(line[indx])

arr = np.empty((0, 3), int)
for index, el in enumerate(instr.split("\n")):
    el = [int(el) for el in list(re.findall(r"\d+", el))]
    el = [e-1 if indx > 0 else e for indx, e in enumerate(el)]
    arr = np.vstack((arr, el))

sol1 = [x[:] for x in all]
for move, origin, target in arr:
    for a in range(move):
        sol1[target].insert(0, sol1[origin][0])
        sol1[origin].pop(0)

result1 = "".join([l[0] for l in sol1])
submit(result1)

sol2 = [x[:] for x in all]
for move, origin, target in arr:
    if line[0] == 1:
        sol2[target].insert(0, sol2[origin][0])
        sol2[origin].pop(0)
    else:
        sol2[target] = sol2[origin][:move] + sol2[target]
        sol2[origin] = sol2[origin][move:]

result2 = "".join([l[0] for l in sol1])
submit(result2)

