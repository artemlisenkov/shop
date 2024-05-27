from base_class import Utensil


class TeaSpoon(Utensil):
    def __init__(self, material, length, color):
        super().__init__(material, length, color, False)

    def produce(self):
        pass
