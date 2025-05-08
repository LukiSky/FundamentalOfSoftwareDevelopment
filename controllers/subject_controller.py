from database import Database
from university import University
from util.util import *

from models import Subject

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
            choice = input(f"{emptySpace}Student Course Menu (c/e/r/s/x): ").lower()
            match choice:
                case "c":
                    print(f"{emptySpace}Updating Password")
                    self.changePassword()
                case "e":
                    self.enroll_subject()
                case "r":
                    self.remove_subject()
                case "s":
                    self.display_subjects()
                case "x":
                    break
                case _:
                    print(f"{emptySpace}Error: please either input c, e, r, s, or x")

    
    def changePassword(self):
        newPassword = input(f"{emptySpace}New password: ")
        university = University()
        while not university.is_valid_password(newPassword):
            print(f"{emptySpace}Invalid password. Try again.")
            newPassword = input(f"{emptySpace}New password: ")

        confirmPassword = input(f"{emptySpace}Confirm password: ")
        while(newPassword != confirmPassword):
            print("Password does not match - try again")
            confirmPassword = input(f"{emptySpace}Confirm password: ")
        students = Database.load_data()
    
        for student in students:
            if student["id"] == self.student_id:
                student["password"] = newPassword
                break
        Database.save_data(students)
    
    def enroll_subjectGUI(self):
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
            print("Students are allowed to enroll in 4 subjects only.")
            return

        new_subject = Subject()
        existing_ids = {s.id for s in self.subjects}

        while new_subject.id in existing_ids:
            new_subject = Subject()

        self.subjects.append(new_subject)
        self.save_subjects()
        print(f"{emptySpace}Subject {new_subject.id} enrolled successfully!")
        print(f"{emptySpace}Mark: {new_subject.mark}, Grade: {new_subject.grade}")
        print(f"{emptySpace}Total Enrolled Subjects: {len(self.subjects)}")

    def remove_subject(self):
        if not self.subjects:
            print("No subjects enrolled to remove.")
            return

        subject_id = input("Enter Subject ID to remove: ")
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                self.save_subjects()
                print(f"{emptySpace}Subject {subject_id} removed successfully!")
                return

        print(f"{emptySpace}Subject ID {subject_id} not found.")

    def display_subjects(self):
        if not self.subjects:
            print("No subjects enrolled.")
            return

        print(f"{emptySpace}Enrolled Subjects:")
        for subject in self.subjects:
            print(f"ID: {subject.id}, Mark: {subject.mark}, Grade: {subject.grade}")

    def save_subjects(self):
        subject_dicts = [s.get_subject_json() for s in self.subjects]
        Database.save_subjects(self.student_id, subject_dicts)

