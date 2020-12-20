from part1 import expenses, sums_of_2020
from itertools import combinations

# making Tuples
result = list(filter(sums_of_2020,list(combinations(expenses, 3))))


print(result)
