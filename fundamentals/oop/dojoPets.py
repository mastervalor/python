class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 50
        self.noise = noise
        super().__init__()
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self
# noise() - prints out the pet's sound
    def noises(self):
        print(self.noise)
        return self