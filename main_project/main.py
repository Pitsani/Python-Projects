import second
import time

now = time.strftime("%b %d, %Y  %H:%M:%S")
print("It is", now)

while True:
    user_input = input("Enter add, show, edit, complete, exit: ")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:]

        todos = second.readFile()

        todos.append(todo+"\n")

        second.openFile(todos)

    elif user_input.startswith('show'):
        todos = second.readFile()
        new_todos = [item.strip('\n') for item in todos]
        for index, i in enumerate(new_todos):
            print(f"{index+1}-{i}")

    elif user_input.startswith('edit'):
        try:
            todos = second.readFile()
            number = int(user_input[5:])
            number=number-1
            new_todo = input("Enter a new to do: ")
            todos[number] = new_todo + '\n'

            second.openFile(todos)
        except ValueError:
            print("Your command is invalid!\n")
            continue

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])
            todos = second.readFile()
            index = number-1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            second.openFile(todos)

            message = f"Todo '{todo_to_remove}' was removed."
            print(message)
        except IndexError:
            print("No item with this number!\n")
            continue


    elif user_input.startswith('exit'):
            break
    else:
        print("Invalid command")
            
