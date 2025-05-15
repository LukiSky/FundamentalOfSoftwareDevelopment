from university_system.models.database import Database
from university_system.models.subject import Subject
from university_system.utils.utils import *
from university_system.utils.utils import *

class SubjectController():
    def __init__(self, student_id):
        self.student_id = student_id
        self.subjects = self.load_subjects()
    
    def load_subjects(self):
        subject_dicts = Database.load_subjects(self.student_id)
        subjects = []
        for data in subject_dicts:
            subject = Subject()
            subject.id = data["id"]
            subject.mark = data["mark"]
            subject.grade = data["grade"]
            subjects.append(subject)
        return subjects
    
    def menu(self):
        while True:
            choice = input(f"{indent2}Student Course Menu (c/e/r/s/x): ").lower().strip()
            match choice:
                case "c":
                    print(f"{indent2}Updating Password")
                    self.change_password()
                case "e":
                    self.enroll_subject()
                case "r":
                    self.remove_subject()
                case "s":
                    self.display_subjects()
                case "x":
                    break
                case _:
                    print(f"{indent2}Error: please either input c, e, r, s, or x")

    
    def change_password(self):
        from university_system.university import University
        newPassword = input(f"{indent2}New password: ")
        university = University()
        while not university.is_valid_password(newPassword):
            print(f"{indent2}Invalid password. Try again.")
            newPassword = input(f"{indent2}New password: ")

        confirmPassword = input(f"{indent2}Confirm password: ")
        while(newPassword != confirmPassword):
            print(f"{indent2}Password does not match - try again")
            confirmPassword = input(f"{indent2}Confirm password: ")
        students = Database.load_data()
    
        for student in students:
            if student["id"] == self.student_id:
                student["password"] = newPassword
                break
        Database.save_data(students)
    
    def enroll_subject_gui(self):
        if len(self.subjects) >= 4:
            return False
        print(self.subjects)
        new_subject = Subject()
        existing_ids = {s.id for s in self.subjects}

        while new_subject.id in existing_ids:
            new_subject = Subject()

        self.subjects.append(new_subject)
        self.save_subjects()

        return [new_subject]

    def enroll_subject(self):
        if len(self.subjects) >= 4:
            print(f"{indent2}Students are allowed to enrol in 4 subjects only")
            return

        new_subject = Subject()
        existing_ids = {s.id for s in self.subjects}

        while new_subject.id in existing_ids:
            new_subject = Subject()

        self.subjects.append(new_subject)
        self.save_subjects()
        print(f"{indent2}Enrolling in Subject-{new_subject.id}")
        print(f"{indent2}You are now enrolled in {len(self.subjects)} out of 4 subjects")

    def remove_subject(self):
        if not self.subjects:
            print(f"{indent2}No subjects enrolled to remove")
            return

        subject_id = input(f"{indent2}Remove Subject by ID: ")
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                self.save_subjects()
                print(f"{indent2}Dropping Subject-{subject_id}")
                print(f"{indent2}You are now enrolled in {len(self.subjects)} out of 4 subjects")
                return

        print(f"{indent2}Subject ID {subject_id} not found")

    def display_subjects(self):
        print(f"{indent2}Showing {len(self.subjects)} subjects")
        for subject in self.subjects:
            print(f"{indent2}[ Subject::{subject.id:>3} -- mark = {subject.mark:>3} -- grade =  {subject.grade:>3} ]")

    def save_subjects(self):
        subject_dicts = [s.get_subject_json() for s in self.subjects]
        Database.save_subjects(self.student_id, subject_dicts)
