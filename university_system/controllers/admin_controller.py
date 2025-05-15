from university_system.controllers.user_controller import UserController
from university_system.models.database import Database
from university_system.models.admin import Admin
from university_system.utils.utils import *

class AdminController(UserController):
    def __init__(self):
        self.admin = Admin()

    def menu(self):
        while True:
            print("\n--- Admin System Menu ---")
            print(f"{indent}(c) Clear Database")
            print(f"{indent}(g) Group Students by Grade")
            print(f"{indent}(p) Partition Students (Pass/Fail)")
            print(f"{indent}(r) Remove Student")
            print(f"{indent}(s) Show Student List")
            print(f"{indent}(x) Exit Admin Menu")
            
            choice = input(f"{indent}Enter choice: ").lower().strip()
            match choice:
                case "c":
                    print(f"{indent}Clearing students database")
                    self.admin.clearStudentData()
                case "g":
                    print(f"{indent}Grade Grouping")
                    self.admin.organizeByGrade()
                case "p":
                    print(f"{indent}PASS/FAIL Partition")
                    self.admin.categorizeByPassStatus()
                case "r":
                    self.admin.remove_student()
                case "s":
                    while True: 
                        print(f"{indent}(s) Show full Student List")
                        print(f"{indent}(si) Sort Student by ID")
                        print(f"{indent}(sn) Sort Student by Name")
                        print(f"{indent}(se) Sort Student by Email")
                        print(f"{indent}(x) Exit Sort Menu")  

                        choice2 = input(f"{indent}Select how to sort: ").lower().strip()
                        match choice2:
                            case "s":
                                print(f"{indent}Student List")
                                self.admin.viewAllStudents()
                            case "si":
                                print(f"{indent}Student List base on ID")
                                self.admin.sortStudent(choice)
                            case "sn":
                                print(f"{indent}Student List base on name")
                                self.admin.sortStudent(choice)
                            case "se":
                                print(f"{indent}Student List base on Email")
                                self.admin.sortStudent(choice)
                            case "x":
                                break
                case "x":
                    break
                case _:
                    print(f"{indent}Error: please either input c, g, p, r, s, or x")
