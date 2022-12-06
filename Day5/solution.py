def get_stacks_from_input(input_data) -> list:
    stacks = []
    for stack in zip(*reversed(input_data[:-1])):
        if stack[0] not in '[] ':
            stacks.append([crate for crate in stack if crate != ' '])
    return stacks


def get_moves_from_input(input_data):
    moves = input_data.split()
    if len(moves) >= 6:
        return int(moves[1]), int(moves[3]), int(moves[5])
    else:
        return 0, 0, 0


stacks = []
with open('input5', mode='r') as f:
    stacks_input = []
    while line := f.readline():
        if line == '\n':
            break
        stacks_input.append(line.strip('\n'))
    stacks = get_stacks_from_input(stacks_input)
    stacks2 = get_stacks_from_input(stacks_input)

    # move crates in stacks, input file read stopped at blank line so next we read only move commands
    for moveline in f.readlines():
        number_of_crates, from_stack, to_stack = get_moves_from_input(moveline)
        # part 1 - move crate 1 by 1
        for x in range(0, number_of_crates):
            crate = stacks[from_stack - 1].pop()
            stacks[to_stack - 1].append(crate)
            # part 2 - move all crates at once
        stacks2[from_stack - 1], crates = stacks2[from_stack - 1][0:-number_of_crates], stacks2[from_stack - 1][
                                                                                        -number_of_crates:]
        stacks2[to_stack - 1].extend(crates)

print('PART ONE: TOP CRATES = ' + ''.join([stack[-1] for stack in stacks]))
print('PART TWO: TOP CRATES = ' + ''.join([stack[-1] for stack in stacks2]))