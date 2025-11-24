string = input("Enter string: ")

spaces_count = 0
for ch in string:
    if(ch == " "):
        spaces_count += 1

print(spaces_count)