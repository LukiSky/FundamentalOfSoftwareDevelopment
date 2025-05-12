from university_system.controllers.user_controller import UserController
from university_system.model.database import Database
from university_system.utils.utils import *
from university_system.model.exception import LoginError, ValidationError
from university_system.model.student import Student

class StudentController(UserController):
    def __init__(self):
        self.students = Student()

    def menu(self):
        while True:
            choice = input(f"{indent}Student System (l/r/x): ").lower().strip()
            match choice:
                case "l":
                    print(f"{indent}Student Sign In")
                    while True:
                        try:
                            self.students.login()
                            break
                        except ValueError as e:
                            print(f"{indent}{e}")
                case "r":
                    print(f"{indent}Student Sign Up")
                    while True:
                        try:
                            self.students.register()
                            break
                        except ValueError as e:
                            print(f"{indent}{e}")
                case "x":
                    break
                case _:
                    print(f"{indent}Error: please either input l, r, or x")