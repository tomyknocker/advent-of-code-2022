class CPU:

    def __init__(self):
        self.cycle = 0
        self._register_x = 1
        self._signal_strength = []

    @property
    def signal_strength(self):
        return self._signal_strength


    def print_on_screen(self):
        if pixel_pos := self.cycle % 40:
            if self._register_x <= pixel_pos <= self._register_x+2:
                pixel = '#'
            else:
                pixel = ' '
            print(pixel, end='')
        else:
            print('')
    def _cpu_output(self):
        self.print_on_screen()
        if not (self.cycle - 20) % 40:
            self._signal_strength.append((self.cycle, self.cycle * self._register_x))
        return

    def _cpu_cycle(self):
        self.cycle += 1
        self._cpu_output()
        return None

    def cpu_command(self, command, *args):
        if command == 'noop':
            self._cpu_cycle()
        if command == 'addx':
            self._cpu_cycle()
            self._cpu_cycle()
            self._register_x += args[0]


communicator = CPU()
print(f"PART2:")
with open('input', mode='r') as f:
    while line := f.readline().strip():
        match line.split():
            case ['addx', param]:
                value = int(param)
                communicator.cpu_command('addx', value)
            case ['noop']:
                communicator.cpu_command('noop')

ss_sum = 0
for cpu_cycle, signal_strength in communicator.signal_strength:
    if cpu_cycle in {20, 60, 100, 140, 180, 220}:
        ss_sum += signal_strength
# print(communicator.signal_strength)
print(f"PART1: {ss_sum=}")

