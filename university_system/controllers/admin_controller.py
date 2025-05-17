from university_system.controllers.user_controller import UserController
from university_system.models.database import Database
from university_system.models.admin import Admin
from university_system.utils.utils import *

### Color Controls ###

RESET  = "\033[0m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"

####


class AdminController(UserController):
    def __init__(self):
        self.admin = Admin()

    def menu(self):
        while True:
            print(f"{CYAN}\n--- Admin System Menu ---{RESET}")
            print(f"{CYAN}{indent}(c) Clear Database{RESET}")
            print(f"{CYAN}{indent}(g) Group Students by Grade{RESET}")
            print(f"{CYAN}{indent}(p) Partition Students (Pass/Fail){RESET}")
            print(f"{CYAN}{indent}(r) Remove Student{RESET}")
            print(f"{CYAN}{indent}(s) Show Student List{RESET}")
            print(f"{CYAN}{indent}(x) Exit Admin Menu{RESET}")
            
            choice = input(f"{CYAN}{indent}Enter choice: {RESET}").lower().strip()
            match choice:
                case "c":
                    print(f"{YELLOW}{indent}Clearing students database{RESET}")
                    self.admin.clearStudentData()
                case "g":
                    print(f"{YELLOW}{indent}Grade Grouping{RESET}")
                    self.admin.organizeByGrade()
                case "p":
                    print(f"{YELLOW}{indent}PASS/FAIL Partition{RESET}")
                    self.admin.categorizeByPassStatus()
                case "r":
                    self.admin.remove_student()
                case "s":
                    while True: 
                        print(f"{CYAN}{indent}(s) Show full Student List{RESET}")
                        print(f"{CYAN}{indent}(si) Sort Student by ID{RESET}")
                        print(f"{CYAN}{indent}(sn) Sort Student by Name{RESET}")
                        print(f"{CYAN}{indent}(se) Sort Student by Email{RESET}")
                        print(f"{CYAN}{indent}(x) Exit Sort Menu{RESET}")  

                        choice2 = input(f"{indent}Select how to sort: ").lower().strip()
                 
                        match choice2:
                           
                            case "s":
                                print(f"{YELLOW}{indent}Student List{RESET}")
                                self.admin.viewAllStudents()
                            case "si":
                                print(f"{YELLOW}{indent}Student List base on ID{RESET}")
                                self.admin.sortStudent(choice2)
                            case "sn":
                                print(f"{YELLOW}{indent}Student List base on name{RESET}")
                                self.admin.sortStudent(choice2)
                            case "se":
                                print(f"{YELLOW}{indent}Student List base on Email{RESET}")
                                self.admin.sortStudent(choice2)
                            case "x":
                                break
                case "x":
                    break
                case _:
                    print(f"{RED}{indent}Error: please either input c, g, p, r, s, or x{RESET}")
