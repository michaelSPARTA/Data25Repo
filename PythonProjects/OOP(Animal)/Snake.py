from Reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = False
        self.venom = None
        self.has_limbs = False

    def use_tongue_to_smell(self):
        print('Do I say it smells or tastes nice')


# sidney = Snake()
# print(sidney.cold_blooded)
