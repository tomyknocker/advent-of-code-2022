class CaveScan:
    def __init__(self, width, length):
        self._rock_map = []
        for x in range(length):
            self._rock_map.append(['.'] * width)
        self._bottom = 1
        self._left = 500
        self._right = 500
        self.start_position = 500, 0
        self.sand_units = 0

    def add_rocks(self, start, end):
        x1, y1 = start
        x2, y2 = end
        # horizontal rock
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for a in range(y1, y2 + 1):
                self._rock_map[a][x1] = '#'
        # vertical rock
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for b in range(x1, x2 + 1):
                self._rock_map[y1][b] = '#'
        # update rock array borders
        self._left = min(self._left, x1, x2)
        self._right = max(self._right, x1, x2)
        self._bottom = max(self._bottom, y1, y2)

    def throw_sand(self) -> bool:
        # put sand at start position

        x, y = self.start_position
        sand_is_moving = True
        while sand_is_moving:
            if y > self._bottom + 1:
                return True
            # down
            if self._rock_map[y + 1][x] in ['.', '~']:
                # sand falls down
                y = y + 1
                self._rock_map[y][x] = '~'
                continue
            # left
            if self._rock_map[y + 1][x - 1] in ['.', '~']:
                x = x - 1
                y = y + 1
                self._rock_map[y][x] = '~'
                continue
            # right
            if self._rock_map[y + 1][x + 1] in ['.', '~']:
                x = x + 1
                y = y + 1
                self._rock_map[y][x] = '~'
                continue
            sand_is_moving = False
            self._rock_map[y][x] = 'o'
            self.sand_units += 1
            # sand blocks entrance (for PART 2)
            if (x, y) == self.start_position:
                sand_is_moving = False
                return True

        return False


with open('input', mode='r') as f:
    cave_map = CaveScan(1000, 1000)
    while line := f.readline().strip():
        rock_path = [tuple(int(coord) for coord in point.split(',')) for point in line.split('->')]
        for x in range(0, len(rock_path) - 1):
            cave_map.add_rocks(rock_path[x], rock_path[x + 1])

# add flor (for PART 2)
y = cave_map._bottom + 2
x1 = cave_map.start_position[0] - y - 1
x2 = cave_map.start_position[0] + y + 1
cave_map.add_rocks((x1, y), (x2, y))

sand_fell_over = False
while not sand_fell_over:
    sand_fell_over = cave_map.throw_sand()


print(cave_map._bottom, cave_map._left, cave_map._right)
for line in cave_map._rock_map[0:cave_map._bottom + 2]:
    for x in line[cave_map._left - 2:cave_map._right + 2]:
        print(x, end='')
    print()

print(f"PART1: {cave_map.sand_units=}")
print(f"PART2: {cave_map.sand_units=}")