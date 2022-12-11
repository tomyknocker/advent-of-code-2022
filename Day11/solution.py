import operator

class Monkey:
    name: str
    items: list
    inspect_operation: callable
    test_operation: callable
    target_monkeys: tuple[int, int]

    def __init__(self, monkey_name, items: list, inspect_opr_str, test_opr_str, throw_true, throw_false):
        self.name = monkey_name
        self.items = items
        self.target_monkeys = throw_true, throw_false
        self.inspect_operation = self._parse_inspect_operation_str(inspect_opr_str)
        self.test_operation = self._parse_test_operation_str(test_opr_str)
        self.monkey_partner1: Monkey = None
        self.monkey_partner2: Monkey = None
        self.inspect_count = 0

    def find_partner_monkeys(self, monkey_list):
        # print(f"{self.name=} {self.target_monkeys=}")
        self.monkey_partner1 = monkey_list[self.target_monkeys[0]]
        self.monkey_partner2 = monkey_list[self.target_monkeys[1]]

    def monkey_turn(self):
        # current_items = self.items
        # self.items = []
        for item in self.items:
            if item['monkey'] == self.name:
                self.inspect_count += 1
                worry_level = self.inspect_operation(item['worry_level'])
                worry_level_relieved = worry_level #// 3
                item['worry_level'] = worry_level_relieved
                # print(f">> {self.name} {item=} -> {worry_level=} -> {worry_level_relieved=}")

                if self.test_operation(item['worry_level']):
                    item['monkey'] = self.monkey_partner1.name
                    # print(f"            -> Throw to {self.monkey_partner1.name}")
                else:
                    item['monkey'] = self.monkey_partner2.name
                    # self.monkey_partner2.catch_item(worry_level_relieved)
                    # print(f"            -> Throw to {self.monkey_partner2.name}")


    # def catch_item(self, item):
    #     self.items.append(item)
    #     pass

    def _parse_inspect_operation_str(self, inspect_opr_str):
        arg1_str, operator_str, arg2_str = inspect_opr_str.split(' ')
        arguments = [None,None]
        if arg1_str == 'old':
            arguments[0] = None
        else:
            arguments[0] = int(arg1_str)
        if arg2_str == 'old':
            arguments[1] = None
        else:
            arguments[1] = int(arg2_str)
        my_operator = None
        if operator_str == '+':
            my_operator = operator.add
        if operator_str == '-':
            my_operator = operator.sub
        if operator_str == '*':
            my_operator = operator.mul
        if operator_str == '/':
            my_operator = operator.truediv

        def insp_opr(x, op_args=arguments):
            if op_args[0] is not None:
                a = op_args[0]
            else:
                a = x

            if op_args[1] is not None:
                b = op_args[1]
            else:
                b = x
            return my_operator(a, b)
        return insp_opr

    def _parse_test_operation_str(self, test_opr_str):
        test_str, arg_str = test_opr_str.rsplit(' ', maxsplit=1)
        my_arg = [None]
        if not test_str == 'divisible by':
            raise Exception
        my_arg[0] = int(arg_str)

        def test_opr(x, a=my_arg):
            if (x % a[0]) != 0:
                divisible_by = False
            else:
                divisible_by = True
            return divisible_by
        return test_opr


global_items=[]
divisions=[]
monkey_list=[]
with open('input', mode='r') as f:
    while line := f.readline():
        line = line.strip()
        if line.startswith('Monkey'):
            monkey_name=line
            items = [int(x) for x in f.readline().strip().split(':')[1].split(',')]
            insp_opr = f.readline().strip().split('=')[1].strip()
            test_opr = f.readline().strip().split(':')[1].strip()
            _, divider = test_opr.rsplit(' ', maxsplit=1)
            monkey1 = f.readline().strip().split('throw to monkey')[1].strip()
            monkey2 = f.readline().strip().split('throw to monkey')[1].strip()
            my_monkey = Monkey(monkey_name=monkey_name,
                               items=global_items,
                               inspect_opr_str=insp_opr,
                               test_opr_str=test_opr,
                               throw_true=int(monkey1),
                               throw_false=int(monkey2))
            monkey_list.append(my_monkey)
            divisions.append(int(divider))
            for item in items:
                global_items.append({'monkey':monkey_name, 'worry_level':item})
# print(len(monkey_list))
for monkey in monkey_list:
    monkey.find_partner_monkeys(monkey_list)
    # print(monkey.name, monkey.items)

# print("PART1")
# for round in range(1, 21):
#     # print(f"   {round=}")
#     for monkey in monkey_list:
#         monkey.monkey_turn()
#
# insp_cnt = sorted([m.inspect_count for m in monkey_list], reverse=True)
# print(f"PART1:{insp_cnt[0]}*{insp_cnt[1]} = {insp_cnt[0]*insp_cnt[1]}")
magic_number = 1
for x in divisions:
    magic_number *= x
print(magic_number)
print("PART2")
for round in range(1, 10001):
    for monkey in monkey_list:
        monkey.monkey_turn()
    if round % 1000 == 0:
        print(f"   {round=}")
        for monkey in monkey_list:
            print(f"{monkey.name=} {monkey.inspect_count=}")

    #part 2 - normalize worry level
    for item in global_items:
        while item['worry_level'] > magic_number:
            item['worry_level'] %= magic_number

insp_cnt = sorted([m.inspect_count for m in monkey_list], reverse=True)
print(f"PART2:{insp_cnt[0]}*{insp_cnt[1]} = {insp_cnt[0]*insp_cnt[1]}")