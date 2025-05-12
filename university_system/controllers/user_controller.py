from abc import ABC, abstractmethod

class UserController(ABC):
    @abstractmethod
    def menu(self):
        pass