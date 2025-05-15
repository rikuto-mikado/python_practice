todos = []

while True:
    user_action = input("This is todo list, what do you want to do??: ")

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "remove":
            todo = input("Enter a todo to remove: ")
            if todo in todos:
                print(f"Removed {todo} from the list successfully")
                todos.remove(todo)
            else:
                print(f"{todo} not found in the list")
        case "exit":
            print("Exiting the program")
            break
