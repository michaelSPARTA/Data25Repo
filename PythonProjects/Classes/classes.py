class Dog:

    def __init__(self, name, colour, age):  # initialisation
        animal_kind = 'canine'  # class variable
        self.name = name
        self.colour = colour
        self.age = age

    def bark(self): # method
        return 'woof'


Fudge = Dog('Fudge', 'Beige', 11) # instantiation
Fudge.animal_kind = 'Cat'
print(Fudge.animal_kind)

Make a car class
    colour max speed make
    fuc drive car(speed increase)