from Animal import Animal


class Reptile(Animal):

    def __init__(self):
        super().__init__()      # Probably on the test. Learn it.
        self.cold_blooded = True
        self.heart_chambers = [3, 4]
        self.lays_eggs = 'Yes'

    def seek_heat(self):
        print('Where is the sun?')

    def use_venom(self):
        print('Use venom')

    def attract_mate_scent(self):
        print('Time to make a stink')


# jeremy_the_reptile = Reptile()
# print(jeremy_the_reptile.lays_eggs)
# print(jeremy_the_reptile.is_alive)
