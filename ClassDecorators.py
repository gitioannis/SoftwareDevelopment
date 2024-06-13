# A class method can be called without having created an instance of the class
# A static method is an independent function not related to any attributes or methods.

class Car:
    cars = []
    
    def __init__(self, Id, name):
        self.Id = Id
        self.name = name
        self.cars.append(self)

    @classmethod #decorator
    def totalCars(cls):
        return len(cls.cars)

    @staticmethod
    def beep(n):
        for i in range(n):
            print("Beep...")
    
    def __str__(self):
        return f"ID: {self.Id}, Name: {self.name}"
        
car1 = Car(1, "VW")
car1 = Car(2, "BMW")
car1 = Car(3, "Mercedes")

for car in Car.cars:
    print(car)

print(Car.totalCars())
Car.beep(3)