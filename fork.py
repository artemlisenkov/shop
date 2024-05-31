from base_class import Utensil


class Fork(Utensil):
    def __init__(self, material, length):
        super().__init__(material, length, False)

    def produce(self):
        pass
