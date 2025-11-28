class Person:
    def __init__(self, name, age = 18, address = "Lalpur, Ranchi - 834001"):
        self.name = name
        self.age = age
        self.address = address

p1 = Person("Shubham Kar")
p2 = Person("Kirti Jain", 20)
p3 = Person("Raunak Kumar", 24, "Sainikpuri, Secunderabad - 500094")

persons = [p1, p2, p3]

for person in persons:
    print(f"Name: { person.name }, Age: { person.age }, Address: { person.address }")