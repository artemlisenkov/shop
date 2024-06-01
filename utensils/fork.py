from utensils.base_class import Utensil


class Fork(Utensil):
    def __init__(self, material, length):
        super().__init__(material, length, False)
        self.tines = 0

    def choose_tines(self):
        tine = int(input("How many tines? (3, 4, 5)"))
        if tine in [3, 4, 5]:
            self.tines = tine
            return tine
        else:
            print("Choose 3, 4 or 5.")
            self.choose_tines()

    def produce(self):
        print(f"Producing a fork:\n"
              f"1. Shaping the {self.material}.\n",
              self.choose_tines(),
              f"2. Creating prongs.\n"
              f"3. Polishing and finishing.\n"
              f"Finish: You have ordered a Fork with parameters:"
              f"Material: {self.material}\n"
              f"Length: {self.length}\n"
              f"Tines: {self.tines}\n")
