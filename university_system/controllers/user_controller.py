from abc import ABC, abstractmethod
from university_system.util.util import *

class UserController(ABC):
    @abstractmethod
    def menu(self):
        pass