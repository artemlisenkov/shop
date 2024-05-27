from knife import Knife
from spoon import Spoon
from fork import Fork
from tea_spoon import TeaSpoon


def choose_len():
    length = int(input("What length in cm (from 5 to 30):"))
    if length <= 5 or length >= 30:
        print("Does our shop look like for aliens?")
        raise ValueError("Length must be greater than 5, less than 30")
    else:
        return length


