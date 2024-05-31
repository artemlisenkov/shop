from base_class import Utensil


class TeaSpoon(Utensil):
    def __init__(self, material, length):
        super().__init__(material, length, False)

    def produce(self):
        print(f"Producing a teaspoon:\n"
              f"1. Melting the {self.material}.\n"
              f"2. Pouring into small spoon mold.\n"
              f"3. Cooling and finishing.\n"
              f"Final: You have ordered a teaspoon with parameters:"
              f"Material: {self.material}\n"
              f"Length: {self.length}\n")
