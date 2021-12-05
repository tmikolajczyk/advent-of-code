# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: aoc
#     language: python
#     name: aoc
# ---

# ## Part 1

import numpy as np
arr = list(np.loadtxt('input.txt'))
result = sum([(arr[int(ind)+1] - number > 0) for ind, number in enumerate(arr) if ind < (len(arr)-1)])
print(result)

# ## Part 2

arr = [np.sum(arr[int(ind):int(ind)+3]) for ind, number in enumerate(arr)]
result = sum([(arr[a+1]) - b > 0  for a, b in enumerate(arr) if a < (len(arr)-1)])
print(result)




