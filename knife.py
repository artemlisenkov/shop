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
        print("1. Producing a knife:\n"
              "2. Melting {self.material}.\n")

        self.blade()

        print("3. Sharpening the blade.\n"
              "4. Polishing the surface.\n"
              "Final: You ordered a Knife with parameters: \n")

        if isinstance(self.material, list):
            print(f"Material: {', '.join(self.material)}")
        else:
            print(f"Material: {self.material}")

        print(f"Sharpness: {self.sharpness} \n"
              f"Length: {self.length} \n")
