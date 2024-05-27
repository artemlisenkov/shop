from base_class import Utensil


class Spoon(Utensil):
    def __init__(self, material, length, color, monotonic):
        super().__init__(material, length, color, monotonic)

    def produce(self):
        pass
