class DirNode:
    def __init__(self, size:int, name:str, parent=None):
        self.parent = parent
        self.elements = []
        self.name = name
        self.size = size
        # print(f"___ add {name=} {size=}, to {parent}")

    def add(self, size:int, name:str):
        node = DirNode(size, name, self)
        # if not any(item for item in self.elements if item.name == name):
        self.elements.append(node)
        # print(node.print_path())

    def print_path(self):
        if self.parent:
            path_str = self.parent.print_path() + '/' + self.name
        else:
            path_str = self.name
        # path_str += '/' + self.name
        return path_str

    def goup(self):
        return self.parent

    def goto(self, name):
        for node in self.elements:
            if node.name == name:
                return node

    def calculate_size(self, dir_list:list[tuple[int,str]]):
        if self.elements:
            self.size = sum(item.calculate_size(dir_list) for item in self.elements)
            dir_list.append((self.size,self.name))
            # print(f"DIR {self.name} = {self.size}")
        return self.size



with open('input7', mode='r') as f:
    file_system = DirNode(0, '/')
    current_node = file_system
    while line := f.readline():
        match line.split():
            case ['$', 'cd', param]:  # command cd
                ls_output = False
                if param == '..':
                    current_node = current_node.goup()
                elif param == '/':
                    current_node = file_system
                else:
                    current_node = current_node.goto(param)

            case ['$', 'ls']:  # command ls
                ls_output = True

            case ['dir', dir_name]:
                if ls_output:
                    current_node.add(0, dir_name)

            case [value, file_name] if value.isnumeric():
                if ls_output:
                    current_node.add(int(value), file_name)

    # calculate size
    #list of (size,dirname)
    dir_list:list[tuple[int,str]] = []
    root_size = file_system.calculate_size(dir_list)
    sum_of_small_dirs = 0
    for directory in dir_list:
        if directory[0] <= 100_000:
            # print (directory)
            sum_of_small_dirs += directory[0]
    print(f"{root_size=}")
    print(f"PART 1 {sum_of_small_dirs=}")

    space_to_free_up = 30_000_000 - (70_000_000 - root_size)
    print(f"{space_to_free_up=}")
    dir_list_sorted = sorted(dir_list, key=lambda x:x[0])
    dir_to_remove = next(item for item in dir_list_sorted if item[0] > space_to_free_up)
    print(f"PART 2 {dir_to_remove=}")