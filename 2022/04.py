from aocd import get_data, submit

day = 4
year = 2022
data = get_data(day=day, year=year)


def split_and_make_range(l):
    return range(int(l.split("-")[0]), int(l.split("-")[-1])+1)

result1 = 0
result2 = 0
for d1 in data.split("\n"):
    r1 = split_and_make_range(d1.split(",")[0])
    r2 = split_and_make_range(d1.split(",")[1])
    if set(r1).issubset(r2) or set(r2).issubset(r1):
        result1 += 1
    if len(list(set(r1) & set(r2))) > 0:
        result2 += 1

submit(result1)
submit(result2)


