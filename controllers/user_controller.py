from abc import ABC, abstractmethod
from util.util import *

class UserController(ABC):
    @abstractmethod
    def menu(self):
        pass