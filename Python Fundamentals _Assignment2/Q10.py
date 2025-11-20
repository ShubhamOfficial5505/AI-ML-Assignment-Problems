secret_number = 20

while(True):
    n = int(input("Guess the number: "))

    if (n < secret_number):
        print("Too low")
    elif (n > secret_number):
        print("Too high")
    else:
        print("Correct!")
        break
