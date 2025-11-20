def print_digits(n):
    while(n != 0):
        print(n % 10)
        n = int(n / 10)

n = int(input("Enter n: "))

print_digits(n)