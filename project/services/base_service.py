from project.validators import Validators
from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.capacity = capacity
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not Validators.check_name_and_kind(value, "Service name cannot be empty!"):
            self._name = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if Validators.check_capacity(value, "Service capacity cannot be less than or equal to 0!"):
            self._capacity = value

    @abstractmethod
    def details(self):
        pass

