from dojoPets import Pet

class Ninja(Pet):
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name , last_name , treats , pet_food, pet_name,pet_type,pet_tricks, pet_noise):
        self.first_name = first_name
        self.last_name= last_name
        self.treats = treats
        self.pet_food = pet_food
        super().__init__(pet_name,pet_type,pet_tricks, pet_noise)
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        super().play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        super().eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        super().noises()
        return self
    

ninja_bob = Ninja("bob", "smith", "sticks", "kibble", "simon", "dog", "shake", "bark")
ninja_bob.feed()
ninja_bob.walk()
ninja_bob.bathe()