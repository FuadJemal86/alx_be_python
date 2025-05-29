

num1 = float (input("Enter the first number: "))
num2 = float (input("Enter the second number:"))

operation = input(' Choose the operation (+, -, *, /):')

if operation == "+": 
    addition = float(num1 + num2)
    print(f'The result is {addition}')
elif operation == "-":
    subtract = float(num1 - num2)
    print(f'The result is {subtract}')
elif operation == "*":
    multiply = float(num1 * num2)
    print(f'The result is {multiply}')
elif operation == "/":
    if num2 != 0:
        divide = float(num1/num2)
    else:
        print('Cannot divide by zero.')

    