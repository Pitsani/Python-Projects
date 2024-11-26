def readFile(filepath="todos.txt"):
    with open(filepath, 'r') as file_l:
        todos_l = file_l.readlines()
        return todos_l

def openFile(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file_l:
        file_l.writelines(todos_arg)

