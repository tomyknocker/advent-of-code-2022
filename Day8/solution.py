forest = []
hidden_trees = []
view_score = []
with open('input', mode='r') as f:
    for x, line in enumerate(f.readlines()):
        forest.append([int(tree) for tree in line.strip()])

row_length = len(forest) - 1
column_length = len(forest[0]) - 1

hidden_trees = [[0] * len(forest[0]) for _ in range(len(forest))]
view_score = [[0] * len(forest[0]) for _ in range(len(forest))]
hidden_trees_count = 0
for row in range(1, row_length):
    highest_left, highest_right = 0, column_length
    for column in range(1, column_length):
        column_r = column_length - column
        if forest[row][highest_left] < forest[row][column]:
            highest_left = column
        else:
            hidden_trees[row][column] += 1
        if forest[row][highest_right] < forest[row][column_r]:
            highest_right = column_r
        else:
            hidden_trees[row][column_r] += 1

for column in range(1, column_length):
    highest_top, highest_bottom = 0, row_length
    for row in range(1, row_length):
        row_r = row_length - row
        if forest[highest_top][column] < forest[row][column]:
            highest_top = row
        else:
            hidden_trees[row][column] += 1
        if forest[highest_bottom][column] < forest[row_r][column]:
            highest_bottom = row_r
        else:
            hidden_trees[row_r][column] += 1

for column in range(1, column_length):
    for row in range(1, row_length):
        if hidden_trees[row][column] == 4:
            hidden_trees_count += 1
visible_trees_count = (row_length + 1) * (column_length + 1) - hidden_trees_count
print(f"PART1: {visible_trees_count=}")


def tree_view_score(forest, rows, columns, row, column):
    tree = forest[row][column]
    for x in range(1, column+1):
        tree2 = forest[row][column-x]
        if tree2 >= tree:
            break
    left_view = x
    for x in range(1, columns+1-column):
        tree2 = forest[row][column+x]
        if tree2 >= tree:
            break
    right_view = x
    for x in range(1, row+1):
        tree2 = forest[row-x][column]
        if tree2 >= tree:
            break
    top_view = x
    for x in range(1, rows+1-row):
        tree2 =forest[row+x][column]
        if tree2 >= tree:
            break
    bottom_view = x
    return left_view*right_view*top_view*bottom_view

highest_scenic_score = 0
for row in range(1, row_length):
    for column in range(1, column_length):
        view_score[row][column] = tree_view_score(forest,row_length, column_length, row, column)
        if view_score[row][column] > highest_scenic_score:
            highest_scenic_score = view_score[row][column]
print(f"PART2: {highest_scenic_score=}")