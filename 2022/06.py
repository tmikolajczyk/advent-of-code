from aocd import get_data, submit

day = 6
year = 2022
data = get_data(day=day, year=year)

for a in range(len(data)):
    signal = data[a:a+4]
    if len(set(signal)) == 4:
        result1 = a+4
        break
submit(result1)

for a in range(len(data)):
    signal = data[a:a+14]
    if len(set(signal)) == 14:
        result2 = a+14
        break
submit(result2)