# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np

with open('input.txt','r') as f:
    input_list = eval(f.read())

# ## part 2

total_fuel = []
for possible_position in range(1, max(input_list)+1):
    total_fuel.append((possible_position, sum([np.abs(a - possible_position) for a in input_list])))

print(f'result of part 1, day 7: {total_fuel[np.argmin([u[1] for u in total_fuel])][1]}')

# ## part 2

total_fuel = []
for dist in range(1, max(input_list)+1):
    fuels = []
    for item in input_list:
        diff = np.abs(item - dist)
        sum_of_ranges = sum(range(1, diff+1))
        fuels.append(sum_of_ranges)
    fuels_sum = sum(fuels)
    total_fuel.append(fuels_sum)

print(f'result of part 2, day 7: {total_fuel[np.argmin(total_fuel)]}')


