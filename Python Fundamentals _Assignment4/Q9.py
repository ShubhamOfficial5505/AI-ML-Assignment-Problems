# Multiple Inheritance (3 Base classes, 1 Derived class)

class Hervivore:
    def __init__(self):
        self.hunts = False

    def eats(self):
        print("Eats Plants")

class Carnivore:
    def __init__(self):
        self.hunts = True

    def eats(self):
        print("Eats Meat")

class Omnivore:
    def __init__(self):
        self.hunts = True

    def eats(self):
        print("Eats Plants as well as Meat")

class Bear(Omnivore, Carnivore, Hervivore):
    # Python couldn't find a constructor in the Bear class
    # Omnivore constructor gets called (MRO)
    # Carnivore/Hervivore classes weren't even checked
    pass 

# MRO (Method Resolution Order) is the order in which python looks for methods and attributes in an Inheritance Setup
# Bear -> Omnivore -> Carnivore -> Hervivore -> object (Root parent class of every class in python)
print(Bear.mro())

bear = Bear() # Acts as a trigger to tell python to call the Derived class's (Bear) constructor 
print(bear.hunts) # True (Omnivore)
bear.eats() # Eats Plants as well as Meat (Omnivore)