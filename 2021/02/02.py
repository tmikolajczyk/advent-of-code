# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: aoc_venv
#     language: python
#     name: aoc
# ---

# ## Part 1

# +
import pandas as pd

df = pd.read_csv('input.txt', sep=' ', names=['move', 'size'], index_col=0)

h = 0
v = 0
for index, row in df.iterrows():
    if index == 'forward':
        h += row[0]
    else:
        if index == 'down':
            v += row[0]
        elif index == 'up':
            v -= row[0]
print(h * v)
# -

# ## Part 2

# +
h = 0
v = 0
a = 0
for index, row in df.iterrows():
    if index != 'forward':
        if index == 'down':
            a += row[0]
        elif index == 'up':
            a -= row[0]
    else:
        h += row[0]
        v += row[0] * a

print(h * v)
# -


