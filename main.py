from knife import Knife
from spoon import Spoon
from fork import Fork
from tea_spoon import TeaSpoon


def choose_utensil():
    utensils = [Knife.__name__, TeaSpoon.__name__,
                Fork.__name__, Spoon.__name__]

    print(', '.join(utensils))
    choice = input("Which utensil would you like to order?")

    if choice not in utensils:
        print("Choose existent one.")
        return choose_utensil()
    else:
        for utensil in utensils:
            if utensil.__name__ == choice:
                return utensil


def choose_length():
    length = int(input("What length in cm (from 5 to 30):"))
    if length <= 5 or length >= 30:
        print("Does our shop look like for aliens?")
        raise ValueError("Length must be greater than 5, less than 30")
    else:
        return length


def is_monotonic(self):
    yes_no = input("Monotonous? (Y/n)")

    if yes_no.lower() not in ["y", "yes", "ye"]:
        return False
    else:
        return True
