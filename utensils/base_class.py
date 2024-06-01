from abc import ABC, abstractmethod


class Utensil(ABC):
    def __init__(self, material: str, length: float, monotonic: bool):
        super().__init__()
        self.material = material
        self.length = length
        self.monotonic = monotonic

    @abstractmethod
    def produce(self):
        pass


class Meal(ABC):
    def __init__(self):
        super().__init__()
