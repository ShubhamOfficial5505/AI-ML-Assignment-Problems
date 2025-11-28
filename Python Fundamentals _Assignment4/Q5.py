# Hierarchical Inheritance (1 Base class, 2 Derived classes)

# Base Class
class Vehicle:
    # called automatically by python at the time of object creation (Performs Initialization)
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Derived Class
class  Car(Vehicle):
    # called automatically by python at the time of object creation (Performs Initialization)
    def __init__(self, brand, model, seats):
        super().__init__(brand, model) # Acts as a trigger to tell python to call the Base class's constructor
        self.seats = seats

# Derived Class
class Bike(Vehicle):
    # called automatically by python at the time of object creation (Performs Initialization)
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model) # Acts as a trigger to tell python to call the Base class's constructor
        self.engine_cc = engine_cc

car = Car("Toyota", "Camry", 5) # Acts as a trigger to tell python to call the Derived class's (Car) constructor
bike = Bike("Harley-Davidson", "Street Glide Special", 1868) # Acts as a trigger to tell python to call the Derived class's (Bike) constructor

print(car.brand, car.model, car.seats)
print(bike.brand, bike.model, bike.engine_cc)