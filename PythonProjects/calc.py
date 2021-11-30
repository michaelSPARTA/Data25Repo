def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def main():
    choice = input('Enter 1 for addition and 2 for subtraction:  ')
    choice_out = ''
    while choice:
        if choice == '1':
            choice_out = 'add'
            break
        elif choice == '2':
            choice_out = 'subtract'
            break
        else:
            choice = input('Try again, enter 1 for addition and 2 for subtraction:  ')

    first = input(f'Enter the first number you would like to {choice_out}:  ')
    second = input(f'Now enter the second number you would like to {choice_out}:  ')
    while first:
        if choice == '1' and first.isnumeric() and second.isnumeric():
            return f'{first} + {second} = {add(int(first), int(second))}'
        elif choice == '2' and first.isnumeric() and second.isnumeric():
            return f'{first} - {second} = {subtract(int(first), int(second))}'
        else:
            first = input(f'Try again, enter the first number you would like to {choice_out}:  ')
            second = input(f'Now enter the second number you would like to {choice_out}:  ')


print(main())

