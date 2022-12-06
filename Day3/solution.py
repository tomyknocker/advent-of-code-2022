def item_priority(item:int) -> int:
    if 97 <= item <=122:
        priority = item - 96
    if 65 <= item <= 90:
        priority = item - 38
    # print (f"{item=} {chr(item)} {priority=}")
    return priority

priorities_sum = 0
badges_sum = 0
team = 0
with open('input', mode='rb') as f:
    elf_sacks = f.readlines()
    for line in elf_sacks:
        sack=line.strip()
        pocket_size = len(sack)//2
        pocket_a, pocket_b = sack[:pocket_size], sack[pocket_size:]   
        priorities_sum += next((item_priority(x) for x in pocket_a if x in pocket_b))

    for elf in range(0,len(elf_sacks),3):
        badges_sum += next(( item_priority(item) for item in elf_sacks[elf].strip()
                                                 if item in elf_sacks[elf+1] and item in elf_sacks[elf+2]))


print(f"{priorities_sum=}")
print(f"{badges_sum=}")
