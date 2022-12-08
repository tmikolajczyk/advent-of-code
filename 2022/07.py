from aocd import get_data, submit
import re

day = 7
year = 2022
data = get_data(day=day, year=year)

data = data.split("\n")

path = []
files = {}

for i, l in enumerate(data):
    line = l.split(" ")
    if i == 32:
        print(i)
    if line[1] == 'cd':
        if ".." in l:
            path.pop(-1)
        else:
            path.append(line[2])
    if re.findall(r"\d+", l):
        size = int(l.split(" ")[0])
        for i, p in enumerate(path):
            fpath = p
            if p != "/":
                fpath = "/".join(path[:i+1])
            if not fpath in files.keys():
                files[fpath] = []
            files[fpath].append(size)

result1 = {k: sum(v) for k, v in files.items() if sum(v) < 100000}
# submit(sum([a for a in result1.values()]))

dir_find = sum(files.get('/')) - int(7e7) + int(3e7)
result2 = min([sum(v) for k, v in files.items() if sum(v) > dir_find])
submit(result2)
