from base_class import Utensil


class Knife(Utensil):
    def __init__(self, material, length, monotonic):
        super().__init__(material, length, monotonic)

    def produce(self):
        pass
