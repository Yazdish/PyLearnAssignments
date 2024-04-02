class Animal:
    def __init__(self):
        self.age = ...
        self.name = ...
        self.speed = ...
        self.number_of_legs = ...


    def walk(self):
        ...

    def show(self):
        ...

    def eat(self):
        ...


class Eagle(Animal):
    def __init__ (self):
        super().__init__()
        self.emoji = "🦅"
        self.fly_max_height = 1200

    def fly(self):
        ...


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.emoji = "🐟"

    def swim(self):
        ...


nemo = Fish()
nemo.age = 4
print(nemo.emoji)
nemo.swim()
nemo.fly()