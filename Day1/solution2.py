elf1 = 0
elf2 = 0
elf3 = 0
kcal = 0
with open('./input', mode='r') as f:
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

print(f"part 1: most calories = {elf1}")
print(f"part 2: sum of 3 biggest cal stacks: {elf1+elf2+elf3}")
