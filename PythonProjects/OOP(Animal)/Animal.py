class Animal:

    def __init__(self):
        self.is_alive = True
        self.has_spine = True
        self.has_eyes = True
        self.has_lungs = True

    def breathe(self):
        print('One breath in, one breath out')

    def eat(self):
        print('nom nom nom')

    def procreate(self):
        print('Time to find a mate')


# cat = Animal()
# cat.breathe()
