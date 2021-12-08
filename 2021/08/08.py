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

# +
from aocd import get_data, submit
import numpy as np
from itertools import chain

day = 8
year = 2021
data = get_data(day=day, year=year)

# +
lines = data.splitlines()
rigth_lines = [l.split(' | ')[-1].split(' ') for l in lines]

rigth_lines_splitted = list(chain.from_iterable(zip(*rigth_lines)))
sum([len(a) in [2, 3, 4, 7] for a in rigth_lines_splitted])
# -


