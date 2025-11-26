class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if(new_name == ""):
            print("Name cannot be empty")
        else:
            self.__name = new_name

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, new_roll_no):
        if(new_roll_no not in range(1, 101)):
            print("Roll must must be in the range of 1 to 100")
        else:
            self.__roll_no = new_roll_no

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if(new_marks < 0):
            print("Marks cannot be negative")
        else:
            self.__marks = new_marks

student = Student("Shubham Kar", 81, 90)

print(student.get_name())
student.set_name("")
student.set_name("Shubham Kumar")
print(student.get_name())

print(student.get_roll_no())
student.set_roll_no(163)
student.set_roll_no(87)
print(student.get_roll_no())

print(student.get_marks())
student.set_marks(-5)
student.set_marks(89)
print(student.get_marks())