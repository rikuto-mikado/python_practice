def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print('Invalid input, please enter a number')

num1 = get_number('Enter the first number: ')
num2 = get_number('Enter the second number: ')
print(f"The sum of {num1} and {num2} is {num1 + num2}")
