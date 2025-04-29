# Basic polymorphism example using classes

class Vehicle:
    def __init__(self, name, sound, speed):
        self.name = name
        self.sound = sound
        self.speed = speed

    def make_sound(self):
        return self.sound
    
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name, sound = "Vroom", speed = 40)

class Train(Vehicle):
    def __init__(self, name):
        super().__init__(name, sound = "Choo choo", speed = 80)

class Plane(Vehicle):
    def __init__(self, name):
        super().__init__(name, sound = "Swoosh", speed = 500)

car1 = Car("Charlie")
car1.speed += 40
car2 = Car("Cathy")

train1 = Train("Thomas")
train2 = Train("Tish")

plane1 = Plane("Penny")
plane2 = Plane("Pierre")

storage_list = [car1, car2, train1, train2, plane1, plane2]

for vehicle in storage_list:
    print(f"{vehicle.name} goes {vehicle.make_sound()} at {vehicle.speed}")

for vehicle in storage_list:
    if car1.speed > vehicle.speed:
        print(f"{car1.name} goes {car1.speed - vehicle.speed} mph faster than {vehicle.name}")
    elif vehicle.speed > car1.speed:
        print(f"{car1.name} goes {vehicle.speed - car1.speed} mph slower than {vehicle.name}")
    else:
        print(f"{car1.name} goes the same speed as {vehicle.name}")