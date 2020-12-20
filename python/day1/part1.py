from data import data
from itertools import combinations

# Getting Expenses list
expenses = all_expenses = list(combinations(data, 2))

# function for getting sum of year 2020
def sums_of_2020(values):
    return sum(values) == 2020


# filter results for all expenses with the function
result = list(filter(sums_of_2020, all_expenses))

# assigning the value
for r in result:
    first, second = r

print(first * second)
