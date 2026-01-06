from project.validators import Validators
from abc import abstractmethod, ABC

class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.weight = weight
        self.price = price
        self.kind = kind
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not Validators.check_name_and_kind(value, "Robot name cannot be empty!"):
            self._name = value

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        if not Validators.check_name_and_kind(value, "Robot kind cannot be empty!"):
            self._kind = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not Validators.check_price(value, "Robot price cannot be less than or equal to 0.0!"):
            self._price = value

    @abstractmethod
    def eating(self):
        pass



