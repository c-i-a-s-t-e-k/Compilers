class Memory:

    def __init__(self, name): # memory name
        self.name = name
        self.memory = dict()

    def has_key(self, name):  # variable name
        return (name in self.memory.keys())

    def get(self, name):         # gets from memory current value of variable <name>
        return self.memory[name]

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.memory[name] = value


class MemoryStack:
                                                                             
    def __init__(self, memory=None): # initialize memory stack with memory <memory>
        self.values = []
        self.names = []
        for name, vale in memory:
            self.values.append(vale)
            self.names.append(name)

    def get(self, name):             # gets from memory stack current value of variable <name>
        value_index = None
        for i, name_val in enumerate(self.names):
            if name_val == name:
                value_index = i
        if value_index is None:
            return None
        else:
            return self.values[value_index]
        

    def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
        self.names.append(name)
        self.values.append(name)

    def set(self, name, value): # sets variable <name> to value <value>
        name_index = None
        for i, value_tocheck in enumerate(self.values):
            if value == value_tocheck:
                name_index = i

        if name_index is not None:
            self.names[name_index] = name
        

    def push(self, memory): # pushes memory <memory> onto the stack
        for name, value in memory:
            self.names.append(name)
            self.values.append(value)

    def pop(self):          # pops the top memory from the stack
        name = self.names.pop()
        value = self.values.pop()
        return name, value

