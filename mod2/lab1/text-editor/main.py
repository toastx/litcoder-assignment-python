class CustomStack:
    def __init__(self):
        self.text = ""
        self.stack = []
        self.cursor = 0

    def insert(self, value):
        self.text = self.text[:self.cursor] + value + self.text[self.cursor:]
        self.stack.append(("insert", value))
        self.cursor += len(value)

    def delete(self, value):
        deleted_text = self.text[self.cursor - value:self.cursor]
        self.text = self.text[:self.cursor - value] + self.text[self.cursor:]
        self.stack.append(("delete", deleted_text))
        self.cursor -= min(value, len(deleted_text))

    def get(self, value):
        if 0 <= value < len(self.text):
            char_at_index = self.text[value]
            print(char_at_index)
        else:
            print("Invalid index")

    def undo(self):
        if self.stack:
            operation, value = self.stack.pop()
            if operation == "insert":
                self.cursor -= len(value)
                self.text = self.text[:self.cursor] + self.text[self.cursor + len(value):]
            elif operation == "delete":
                self.text = self.text[:self.cursor] + value + self.text[self.cursor:]
                self.cursor += len(value)


def process_predefined_commands(commands):
    custom_stack = CustomStack()
    for command in commands:
        command_type, *args = command.split()
        if command_type == '1':
            custom_stack.insert(args[0])
        elif command_type == '2':
            custom_stack.delete(int(args[0]))
        elif command_type == '3':
            custom_stack.get(int(args[0])-1)
        elif command_type == '4':
            custom_stack.undo()


input_text = "1 abc,3 3,2 2,3 1"
input_arr = input_text.split(',')
process_predefined_commands(input_arr)
