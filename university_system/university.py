import re
from university_system.controllers.admin_controller import AdminController
from university_system.controllers.student_controller import StudentController
from university_system.utils.color import *

class University:
    def __init__(self):
        self.admin = AdminController()
        self.student = StudentController()

    def menu(self):
        while True:
            choice = input(f"{CYAN}University System: (A)dmin, (S)tudent, or X: {RESET}").lower().strip()
            match choice:
                case "a":
                    self.admin.menu()
                case "s":
                    self.student.menu()
                case "x":
                    print(f"{YELLOW}Thank You{RESET}")
                    break
                case _:
                    print(f"{RED}Error: please either input A, S, or X{RESET}")

    def is_valid_password(self, password):
        first_upper = password[0].isupper()
        over_5_letters = sum(c.isalpha() for c in password) >= 5
        ends_with_3num = re.search(r"\d{3,}$", password)
        return bool(first_upper and over_5_letters and ends_with_3num)

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@university\.com$'
        return bool(re.match(pattern, email))
    
    def calcGrade(mark):
        if mark >= 85:
            return "HD"
        elif mark >= 75:
            return "D"
        elif mark >= 65:
            return "C"
        elif mark >= 50:
            return "P"
        return "Z"


