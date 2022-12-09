from aocd import get_data, submit
import numpy as np

day = 8
year = 2022
data = get_data(day=day, year=year)
data = data.split("\n")
data = [[int(i) for i in list(l)] for l in data]
data = np.array(data)

res = 0
ds = data.shape
for ir in range(ds[0]):
    if ir == 0 or ir == ds[0] - 1:
        continue
    for ic in range(ds[1]):
        if ic == 0 or ic == ds[1] - 1:
            continue
        val = data[ir, ic]
        left = all(val > data[ir, :ic])
        top = all(val > data[:ir, ic])
        right = all(val > data[ir, ic+1:])
        bottom = all(val > data[ir+1:, ic])
        if sum([left, top, right, bottom]) > 0:
            res += 1

# outside grid
result1 = res + ds[0] * 2 + (ds[1] * 2 - 4)

submit(result1)


result2 = []
for ir in range(ds[0]):
    if ir == 0 or ir == ds[0] - 1:
        continue
    for ic in range(ds[1]):
        if ic == 0 or ic == ds[1] - 1:
            continue
        if ir == 1 and ic == 2:
            print("f")
        val = data[ir, ic]
        # left
        try:
            arr = np.where(data[ir, :ic] >= val)[0]
            if len(arr) == 0:
                indx = 0
            else:
                indx = arr[-1]
        except IndexError:
            indx = 0
        left = len(data[ir, indx:ic])
        
        # top
        try:
            arr = np.where(data[:ir, ic] >= val)[0]
            if len(arr) == 0:
                indx = 0
            else:
                indx = arr[-1]
        except IndexError:
            indx = 0
        top = len(data[indx:ir, ic])
        
        # right
        try:
            arr = np.where(data[ir, ic+1:] >= val)[0]
            if len(arr) == 0:
                indx = ds[0] - 1
            else:
                indx = arr[0]
        except IndexError:
            indx = ds[0]
        right = len(data[ir, ic+1:ic+1+indx+1])
        
        # bottom
        try:
            arr = np.where(data[ir+1:, ic] >= val)[0]
            if len(arr) == 0:
                indx = ds[1] - 1
            else:
                indx = arr[0]
        except IndexError:
            indx = ds[0]
        bottom = len(data[ir+1:ir+1+indx+1, ic])
        
        result2.append(sum([left*top*right*bottom]))

result2 = max(result2)
submit(result2)
