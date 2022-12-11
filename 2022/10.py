from aocd import get_data, submit
import numpy as np

day = 10
year = 2022
data = get_data(day=day, year=year)
data = data.split("\n")

X = 1
cycle = 0
signal = {}

for indx, line in enumerate(data):
    try:
        instruction, value = line.split()
        for i in range(2):
            cycle += 1
            signal[cycle] = X * cycle
            if i == 1:
                X += int(value)
    except ValueError:
        cycle += 1
        signal[cycle] = X * cycle

result1 = 0
for i in range(20, 221, 40):
    result1 += signal[i]
submit(result1)


X = 1
cycle = 0
result2 = np.full(([6, 40]), '.')

def draw(X, cycle, result2):
	beam = (cycle - 1) % 40
	if X - 1 <= beam <= X + 1: 
		line = cycle // 40 
		result2[line, cycle - line * 40] = '#'

for indx, line in enumerate(data):
    try:
        instruction, value = line.split()
        for i in range(2):
            cycle += 1
            draw(X, cycle, result2)
            if i == 1:
                X += int(value)
    except ValueError:
        cycle += 1
        draw(X, cycle, result2)

[print(''.join(l)) for l in result2.tolist()]

# result2 = "____REPLACE_WITH_8_PRINTED_LETTERS____"
submit(result2)
