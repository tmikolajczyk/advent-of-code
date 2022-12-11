from aocd import get_data, submit
import numpy as np

day = 9
year = 2022
data = get_data(day=day, year=year)
data = data.split("\n")

def move(d, m, coords):
    if d == 'R':
        coords[0] += m
    elif d == 'D':
        coords[1] -= m
    elif d == 'L':
        coords[0] -= m
    elif d == 'U':
        coords[1] += m
    return coords

# initial state
arr = np.zeros([1000, 1000])
x = 500
y = 500
coords_h = [x, y]
coords_t = [x, y]

my_res = 0
my_d = {}

previous_dir = data[0].split(" ")[0]
for di, d in enumerate(data):
    if np.sum(arr) != my_res:
        my_res += np.sum(arr)
        my_d[di-1] = int(my_res)
    i, j = d.split(" ")
    j = int(j)
    if di == 3:
        print('df')
    if i == previous_dir:
        for indx, jj in enumerate(range(1, j+1)):
            coords_xremember = coords_h.copy()
            coords_h = move(i, 1, coords_h)
            check = abs(coords_t[0] - coords_h[0]) > 1 or abs(coords_t[1] - coords_h[1]) > 1
            if j == 1 and check:
                coords_t = coords_xremember
            elif not check:
                continue
            else:
                if indx > 0:
                    coords_t = move(i, 1, coords_t)
                    arr[coords_t[0], coords_t[1]] = 1
    else:
        for indx, jj in enumerate(range(1, j+1)):
            coords_xremember = coords_h.copy()
            coords_h = move(i, 1, coords_h)
            check = abs(coords_t[0] - coords_h[0]) > 1 or abs(coords_t[1] - coords_h[1]) > 1
            if check and indx == 0:
                coords_t = coords_xremember
                arr[coords_t[0], coords_t[1]] = 1
            if indx == 0 and j == 1:
                continue
            elif indx <= 1:
                coords_t = coords_xremember
                arr[coords_t[0], coords_t[1]] = 1
            elif indx > 1:
                coords_t = move(i, 1, coords_t)
                arr[coords_t[0], coords_t[1]] = 1

result1 = int(np.sum(arr))
submit(result1)
