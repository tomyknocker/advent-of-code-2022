def rps_round_score(opponent: str, player: str) -> int:
    score = 0
    # draw
    if opponent == player:
        score = 3
        # loose
    if (opponent, player) in [('A', 'C'), ('B', 'A'), ('C', 'B')]:
        score = 0
        # win
    if (opponent, player) in [('C', 'A'), ('A', 'B'), ('B', 'C')]:
        score = 6

        # add score for the shape:
    if player == 'A':
        score += 1
    if player == 'B':
        score += 2
    if player == 'C':
        score += 3
    return score


def rps_round_map(round_data: str) -> int:
    opp, player = round_data[0], round_data[2]
    if player == 'X':
        player = 'A'

    if player == 'Y':
        player = 'B'

    if player == 'Z':
        player = 'C'

    return rps_round_score(opp, player)


def rps_round_map2(round_data: str) -> int:
    opponent, player = round_data[0], round_data[2]
    rps_map = 'CABCA'

    if player == 'X':
        player = rps_map[rps_map.find(opponent, 1) - 1]

    if player == 'Y':
        player = rps_map[rps_map.find(opponent, 1)]

    if player == 'Z':
        player = rps_map[rps_map.find(opponent, 1) + 1]

    return rps_round_score(opponent, player)


def solution():
    with open('input', mode='r') as f:
        score = sum(map(rps_round_map, f.readlines()))
        f.seek(0)
        score2 = sum(map(rps_round_map2, f.readlines()))
    print(f"PART 1: {score=}")
    print(f"PART 2: {score2=}")


solution()
