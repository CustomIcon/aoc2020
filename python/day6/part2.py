from collections import Counter
from part1 import groups

total = 0

for group in groups:
    print(f"\nGroup: {group}")
    group_size = len(group)
    print(f"Length of group: {group_size}")
    counts = Counter("".join(group))
    print(counts)
    counts = Counter(list(counts.values()))[group_size]
    total+=counts

print(f"p2:", total)