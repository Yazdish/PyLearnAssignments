class car:
    def __init__(self,c,m,b):
        self.color = c
        self.wheels_count = 4
        self.maximum_speed = m
        self.company = b

    def turn_on(self):
        ...

    def turn_off(self):
        ...
    
    def booooogh(self):
        ...

my_service = car("yellow",90,"benz")
my_car1 = car("blue",160,"Audi")
my_car2 = car("black", 220, "FORD")

print(my_car2.company)