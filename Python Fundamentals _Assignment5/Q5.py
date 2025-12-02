try:
    f = open("data.txt", "r") # Trying to open a file in read mode which doesn't exist -> Exception
except FileNotFoundError:
    print("File not found!")