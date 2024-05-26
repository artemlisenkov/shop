from abc import ABC, abstractmethod


class Utensil(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def produce(self):
        pass


class Meal(ABC):
    def __init__(self):
        super().__init__()
