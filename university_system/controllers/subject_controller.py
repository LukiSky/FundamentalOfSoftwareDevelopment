from university_system.models.subject import Subject
from university_system.utils.utils import *
from university_system.utils.color import *

class SubjectController():
    def __init__(self, student_id):
          self.subject = Subject(student_id)

    def menu(self):
        while True:
            choice = input(f"{CYAN}{indent2}Student Course Menu (c/e/r/s/x): {RESET}").lower().strip()
            match choice:
                case "c":
                    print(f"{YELLOW}{indent2}Updating Password{RESET}")
                    self.subject.change_password()
                case "e":
                    self.subject.enroll_subject()
                case "r":
                    self.subject.remove_subject()
                case "s":
                    self.subject.display_subjects()
                case "x":
                    break
                case _:
                    print(f"{RED}{indent2}Error: please either input c, e, r, s, or x{RESET}")