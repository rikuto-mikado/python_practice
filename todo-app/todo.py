tasks = []

while True:
    action = input('Add(a), View(v), Delete(d), or Quit(q):').lower()

    if action == 'a':
        task = input('Enter task: ')
        tasks.append(task)
        print('Task added!!')

    elif action == 'v':
        if tasks:
            print('Tasks: ', tasks)
        else:
            print('No tasks!!')
    
    elif action == 'd':
        if tasks:
            task = input('Enter task to delete: ')
            if task in tasks:
                tasks.remove(task)
                print('Task deleted!!')
            else:
                print('Task not found!!')
        else:
            print('No tasks!!')
    
    elif action == 'q':
        print('Goodbye!!')
        break

    else:
        print('Invalid action, try again!!')
