from database import Database
from models.admin import Admin
from util.util import *

from controllers.user_controller import UserController




class AdminController(UserController):
    def __init__(self):
        self.admin = Admin()

    def menu(self):
        
        while True:
            print("\n--- Admin System Menu ---")
            print(f"{emptySpace}(c) Clear Database")
            print(f"{emptySpace}(g) Group Students by Grade")
            print(f"{emptySpace}(p) Partition Students (Pass/Fail)")
            print(f"{emptySpace}(r) Remove Student")
            print(f"{emptySpace}(s) Show Student List")
            print(f"{emptySpace}(si) Sort Student by ID")
            print(f"{emptySpace}(sn) Sort Student by Name")
            print(f"{emptySpace}(se) Sort Student by Email")
            print(f"{emptySpace}(x) Exit Admin Menu")
            choice = input("  Enter choice: ").lower().strip()
            match choice:
                case "c":
                    print("Clearings students database")
                    Database.clear_all_data()
                case "g":
                    print("Grade Grouping")
                    self.admin.organizeByGrade()
                case "p":
                    print("PASS/FAIL Partition")
                    self.admin.categorizeByPassStatus()
                case "r":
                    self.admin.remove_student()
                case "s":
                    print("Student List")
                    self.admin.viewAllStudents()
                case "si":
                    print("Student List base on ID")
                    self.admin.sortStudent(choice)
                case "sn":
                    print("Student List base on name")
                    self.admin.sortStudent(choice)
                case "se":
                    print("Student List base on Email")
                    self.admin.sortStudent(choice)
                case "x":
                    break
                case _:
                    print("Error: please either input c, g, p, r, s, or x")
