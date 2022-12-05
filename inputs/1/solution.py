#!/usr/bin/env python3

#1
def solution():
    with open('input', mode='r') as f:
        calories_data = f.read().replace('\n', ',').replace(',,', '\n')
        elfs = [(x, sum([int(y) for y in calories.split(',')]))
                for x, calories in enumerate(calories_data.splitlines(), start=1)]

        elfs_sorted = sorted(elfs, key=lambda el: el[1], reverse=True)

        x = sum([x[1] for x in elfs_sorted[0:3]])

    print(f"Elf {elfs_sorted[0][0]} has the most calories: {elfs_sorted[0][1]}")
    print(f"Sum of 3 biggest calories stacks: {x}")

#2
def solution2():
    elf1 = 0
    elf2 = 0
    elf3 = 0
    kcal = 0
    with open('input', mode='r') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                kcal += int(line)
            else:
                if kcal > elf1:
                    kcal, elf1 = elf1, kcal
                if kcal > elf2:
                    kcal, elf2 = elf2, kcal
                if kcal > elf3:
                    kcal, elf3 = elf3, kcal
                kcal = 0

    print(elf1)
    print(elf1+elf2+elf3)


if __name__ == '__main__':
    solution()
    solution2()