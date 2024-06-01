from base_class import Utensil


class Knife(Utensil):
    def __init__(self, material, length, monotonic):
        super().__init__(material, length, monotonic)
        self.sharpness = 0

    def blade(self):
        blade_sharpness = int(input("Choose sharpness? [1;5]: \n"))

        if 1 <= blade_sharpness <= 5:
            self.sharpness = blade_sharpness
        else:
            print("Choose the sharpness between 1 and 5")
            self.blade()

    def produce(self):
        print(f"1. Producing a knife:\n"
              f"2. Melting {' and '.join(self.material)}.\n")

        self.blade()

        print(f"3. Sharpening the blade.\n"
              f"4. Polishing the surface.\n"
              f"Final: You ordered a Knife with parameters: \n")

        if isinstance(self.material, list):
            print(f"Material: {', '.join(self.material)}")
        else:
            print(f"Material: {self.material}")

        print(f"Sharpness: {self.sharpness} \n"
              f"Length: {self.length} \n")
