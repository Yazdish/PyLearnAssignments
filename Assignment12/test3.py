class Vehicle:
    def __init__(self):
        self.speed = ...
        self.color = ...
        self.model = ...

    def turn_on(self):
        ...

    def turn_off(self):
        ...

    def gear_change(self):
        ...

    def fly(self):
        ...


class Airplane(Vehicle):
    def __init__(self):
        super().__init__()
        self.capacity = ...
        self.country = ...

    def fly(self):
        ...


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.license_plate = ...



jimbo = Airplane()
pride = Car()

pride.license_plate = "12B384-IRAN32"
pride.color = "white"



