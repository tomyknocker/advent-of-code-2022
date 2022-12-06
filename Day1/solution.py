with open('./input', mode='r') as f:
    calories_data = f.read().replace('\n', ',').replace(',,', '\n')
    elfs = [(x, sum([int(y) for y in calories.split(',')]))
            for x, calories in enumerate(calories_data.splitlines(), start=1)]

    elfs_sorted = sorted(elfs, key=lambda el: el[1], reverse=True)

    x = sum([x[1] for x in elfs_sorted[0:3]])

print(f"Elf {elfs_sorted[0][0]} has the most calories: {elfs_sorted[0][1]}")
print(f"Sum of 3 biggest calories stacks: {x}")
