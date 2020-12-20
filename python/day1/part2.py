from part1 import expenses, sums_of_2020, data
from itertools import combinations

# making Tuples
all_expenses = list(combinations(data, 3))

for r in list(filter(sums_of_2020, all_expenses)):
    first, second, third = r

print(first * second * third)
