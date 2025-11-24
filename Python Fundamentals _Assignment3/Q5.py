info = {
    "Shubham": 90,
    "Rohan": 67,
    "Virat": 98
}

while(True):
    user_input = input("Enter operation: ")
    match user_input:
        case 'A':
            name = input("Enter student's name: ")
            marks = int(input("Enter student's marks: "))
            info.update({ name: marks })
            print("Student Data Added successfully")
        case 'B':
            name = input("Enter student's name: ")
            updated_marks = int(input("Enter updated marks: "))
            info[name] = updated_marks
            print(f"Marks for { name } has been updated to { updated_marks }")
        case 'C':
            name = input("Enter student's name: ")
            marks = info.get(name)
            print(f"Name: { name } \nMarks: { marks }")
        case 'D':
            for name, marks in info.items():
                print(f"Name: { name } \t Marks: { marks }")
        case _:
            print("Quit!")
            break