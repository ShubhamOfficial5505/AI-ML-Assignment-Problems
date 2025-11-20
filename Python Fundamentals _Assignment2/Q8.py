def calculator(a, b, operation):
    match operation:
        case '+':
            print(a + b)
        case '-':
            print(a - b)
        case '*':
            print(a * b)
        case '/':
            print(a / b)
        case _:
            print("Undefined Operation!")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
operation = input("Enter Operation: ")

calculator(a, b, operation)