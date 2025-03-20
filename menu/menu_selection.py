def get_menu_choice():
    while True:
        try:
            choice = int(input("Choose an option:\n1: Start Game\n2: View Rules\n3: Exit\nEnter your choice: "))
            if choice <= 1 or choice <= 3:
                return choice
            else: 
                print('Please enter a number beween 1 and 3.')
        except ValueError:
            print("Invalid input. Please enter a number.")

menu_choice = get_menu_choice()

if menu_choice == 1:
    print('Starting game...')
elif menu_choice == 2:
    print('Viewing rules...')
else:
    print("Exiting game...Goodbye!!")
