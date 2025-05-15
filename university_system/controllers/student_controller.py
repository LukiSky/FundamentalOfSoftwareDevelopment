import random
from university_system.controllers.subject_controller import SubjectController
import random
from university_system.controllers.subject_controller import SubjectController
from university_system.controllers.user_controller import UserController
from university_system.models.database import Database
from university_system.models.student import Student
from university_system.utils.utils import *
from university_system.models.exception import ValidationError, LoginError
from university_system.util.util import *
from university_system.models.student import Student


from university_system.util.util import *

class StudentController(UserController):
    def __init__(self):

        self.students = Student()


    def menu(self):
        while True:
            choice = input(f"{emptySpace}Student System (l/r/x): ").lower()
       
            match choice:
                case "l":
                    print(f"{indent}Student Sign In")
                    while True:
                        try:
                            self.students.login()
                            break
                        except ValidationError as e:
                            print(f"{indent}{e}")
                        except ValueError as e:
                            print(f"{indent}{e}")
                case "r":
                    print(f"{emptySpace}Student Sign Up")
                    while True:
                        try:
                            self.students.register()
                            break
                        except ValidationError as e:
                            print(f"{indent}{e}")
                        except ValueError as e:
                            print(f"{indent}{e}")
                case "x":
                    break
                case _:
                    print(f"{emptySpace}Error: please either input l, r, or x")


    def loginGUI(self, email, password):
        while True:
            for student in self.students:
                if student["email"] == email and student["password"] == password:
                    print(f"{emptySpace}Welcome, {student['name']}!")              
                    return student["id"]
            return False
            