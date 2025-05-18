from university_system.controllers.user_controller import UserController
from university_system.models.database import Database
from university_system.utils.utils import *
from university_system.models.exception import LoginError, ValidationError
from university_system.models.student import Student

### Color Controls ###

RESET  = "\033[0m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"

####


class StudentController(UserController):
    def __init__(self):
        self.students = Student()

    def menu(self):
        while True:
            choice = input(f"{CYAN}{indent}Student System (l/r/x): {RESET}").lower().strip()
            match choice:
                case "l":
                    print(f"{GREEN}{indent}Student Sign In{RESET}")
                    while True:
                        try:
                            self.students.login()
                            break
                        except ValueError as e:
                            print(f"{indent}{e}")
                case "r":
                    print(f"{GREEN}{indent}Student Sign Up{RESET}")
                    while True:
                        try:
                            self.students.register()
                            break
                        except ValueError as e:
                            print(f"{indent}{e}")
                case "x":
                    break
                case _:
                    print(f"{RED}{indent}Error: please either input l, r, or x{RESET}")