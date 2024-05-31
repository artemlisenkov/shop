from knife import Knife
from spoon import Spoon
from fork import Fork
from tea_spoon import TeaSpoon


def choose_utensil():
    utensils = [Knife.__name__, TeaSpoon.__name__,
                Fork.__name__, Spoon.__name__]

    print(', '.join(utensils))
    choice = input("Which utensil would you like to order? \n")

    if choice not in utensils:
        print("Choose existent one.")
        return choose_utensil()
    else:
        for utensil in utensils:
            if utensil == choice:
                return utensil


def choose_material(monotonic: bool):
    materials = ["gold", "silver", "bronze", "steel", "plastic"]

    print(', '.join(materials).title())
    choice1 = input("Which material would you like? \n").lower()

    if not monotonic:
        if choice1 not in materials:
            print("Choose existent one.")
            raise ValueError()
        else:
            return choice1
    else:
        choice2 = input("Which second material would you like? \n")
        if choice1 in materials and choice2 in materials:
            return [choice1, choice2]
        else:
            print("Choose existent one.")
            raise ValueError()


def choose_length() -> float:
    length = float(input("What length in cm (from 5 to 30): \n"))
    if 5 <= length <= 30:
        return length
    else:
        print("Does our shop look like for aliens?")
        raise ValueError("Length must be greater than 5, less than 30")


def is_monotonic() -> bool:
    yes_no = input("Monotonous? (Y/n): \n")

    if yes_no.lower() not in ["y", "yes", "ye"]:
        return False
    else:
        return True


def create():
    utensil_type = choose_utensil()
    length = choose_length()

    utensil_classes = {
        "Knife": Knife,
        "Spoon": Spoon,
        "Fork": Fork,
        "TeaSpoon": TeaSpoon
    }

    utensil_class = utensil_classes[utensil_type]

    if utensil_type == "Knife":
        mono = is_monotonic()
        material = choose_material(mono)
        product = utensil_class(material, length, mono)
    else:
        material = choose_material(False)
        product = utensil_class(material, length)

    return product


def main():
    order = create()
    order.produce()
    print("You will receive your order in 2 weeks max. Thank You!")


if __name__ == "__main__":
    main()
