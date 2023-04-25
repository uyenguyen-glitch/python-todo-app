#from functions import get_todos, write_todos
import functions

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos("todos.txt")

        todos.append(todo + "\n")

        functions.write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos("todos.txt")

            new_todo = input("Enter your todo: ")

            todos[number] = new_todo + "\n"

            functions.write_todos("todos.txt", todos)
        except ValueError:
            print("You command is invalid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(input(user_action[9:]))

            todos = functions.get_todos("todos.txt")

            number -= 1

            todo_to_remove = todos[number].strip("\n")

            todos.pop(number)

            functions.write_todos("todos.txt", todos)
            print(f"Todo {todo_to_remove} was removed from the list")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!!!")
