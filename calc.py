def calc():
    num1 = int(input('Please enter a number: '))
    num2 = int(input('Please enter another number: '))
    operator = input('Please enter an operator (+, -, *, /, %): ')

    if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Enter a valid operator.")


