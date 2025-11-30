with open("names.txt", "w") as f_write:
    for line in range(1, 6):
        name = input("Enter name: ")
        f_write.write(name)
        if(line != 5):
            f_write.write("\n")

print()

with open("names.txt", "r") as f_read:
    names = [name[: len(name) - 1] if "\n" in name else name for name in f_read.readlines()]
    for name in names:
        print(name)