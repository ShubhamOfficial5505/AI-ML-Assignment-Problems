def print_even_num(a, b):
    for i in range(a, b + 1):
        if (i % 2 == 0):
            print(i)

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print_even_num(a, b)