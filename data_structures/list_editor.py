get_list = list(range(11))
def display_game():
    print("\nHere is the current list:")
    print(get_list)

def position_choice():
    while True:
        choice = input("Enter the position where you want to replace the number (0-10): ")
        if choice.isdigit() and 0 <= int(choice) <= 10:
            return int(choice)
        print('Invalid input!! please enter a number between 0 and 10')

def replacement_choice():
    get_list[position] = input('Enter the number you want to replace: ')

display_game()
position = position_choice()
replacement_choice()
display_game()
