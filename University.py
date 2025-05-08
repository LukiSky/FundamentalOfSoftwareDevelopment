import re
from controllers import student_controller
import controllers.admin_controller as admin_controller
from util.util import *


class University:
    def menu(self):
        while True:
            choice = input("University System: (A)dmin, (S)tudent, or X: ").lower()
            match choice:
                case "a":
                    admin = admin_controller()
                    admin.menu()
                case "s":
                    student = student_controller()
                    student.menu()
                case "x":
                    print("Thank You")
                    break
                case _:
                    print("Error: please either input A, S, or X")

    def is_valid_password(self, password):
        first_upper = password[0].isupper()
        over_5_letters = sum(c.isalpha() for c in password) >= 5
        ends_with_3num = re.search(r"\d{3,}$", password)
        return bool(first_upper and over_5_letters and ends_with_3num)

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@university\.com$'
        return bool(re.match(pattern, email))
    
    @staticmethod
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


