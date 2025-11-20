while(True):
    user_input = input("Enter a number or Quit: ")

    if(user_input == "Quit"):
        break

    num = int(user_input)
    if num < 0:
        print("Negative")
    elif num > 0:
        print("positive")
    else:
        print("Zero")
