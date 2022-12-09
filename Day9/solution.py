class Rope:
    def __init__(self, knots=2):
        self.knot_pos_x = [0] * knots
        self.knot_pos_y = [0] * knots
        self.knots = knots

    def move(self, direction: str) -> tuple[int, int]:
        if direction == 'R':
            self.knot_pos_x[0] += 1
        if direction == 'L':
            self.knot_pos_x[0] += -1
        if direction == 'U':
            self.knot_pos_y[0] += 1
        if direction == 'D':
            self.knot_pos_y[0] += -1
        # print(f"move {direction=} to pos: {self.head_pos_x,self.head_pos_y}")
        for x in range(1, self.knots):
            res = self.update_knots_position(x)
        return res

    def update_knots_position(self, knot):
        pos_diff_x = self.knot_pos_x[knot - 1] - self.knot_pos_x[knot]
        pos_diff_y = self.knot_pos_y[knot - 1] - self.knot_pos_y[knot]

        # move only if either of pos difference is bigger than 1
        if abs(pos_diff_x) > 1 or abs(pos_diff_y) > 1:
            if pos_diff_x > 1:
                pos_diff_x -= 1
            if pos_diff_x < -1:
                pos_diff_x += 1
            if pos_diff_y > 1:
                pos_diff_y -= 1
            if pos_diff_y < -1:
                pos_diff_y += 1
            self.knot_pos_x[knot] += pos_diff_x
            self.knot_pos_y[knot] += pos_diff_y
        return self.knot_pos_x[knot], self.knot_pos_y[knot]

tail_positions = {(0, 0)}
tail_positions2 = {(0, 0)}

def move_the_rope(rope: Rope, direction, moves):
    tail_positions = []
    for _ in range(0, moves):
        tail_pos = rope.move(direction)
        tail_positions.append(tail_pos)
    return tail_positions


my_rope = Rope()
my_rope_long = Rope(knots=10)
with open('input', mode='r') as f:
    while move := f.readline().strip():
        direction, moves = move.split()
        positions = move_the_rope(my_rope, direction, int(moves))
        positions2 = move_the_rope(my_rope_long, direction, int(moves))
        tail_positions |= set(positions)
        tail_positions2 |= set(positions2)

print(f"PART1: tail_position_count={len(tail_positions)}")
print(f"PART2: tail_position_count={len(tail_positions2)}")
