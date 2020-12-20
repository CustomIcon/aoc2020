with open("trees.txt", "r") as f:
    lines = f.readlines()

x_x = 0

slope_x = 3
slope_y = 1

trees = 0
for y_y, each_line in enumerate(lines):
    if each_line[x_x] == "#":
        trees += 1
    x_x = (x_x + slope_x) % len(each_line[:-1])
print("p1:{trees}".format(trees=trees))

all_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
all_trees = 1
for slope in all_slopes:
    print("Slope: ", slope)
    slope_x, slope_y = slope
    trees = 0
    x_x = 0
    for y_y, each_line in enumerate(lines):
        if y_y % slope_y == 0:
            if each_line[x_x] == "#":
                trees += 1
            x_x = (x_x + slope_x) % len(each_line[:-1])
    print("Trees on slope: ", trees)
    all_trees *= trees

print("p2: ", all_trees)
