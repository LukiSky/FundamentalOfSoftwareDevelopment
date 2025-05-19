from university_system.models.database import Database
from university_system.models.subject_entity import SubjectEntity
from university_system.utils.utils import *
from university_system.utils.color import *

class Subject:
    def __init__(self, student_id):
        self.student_id = student_id
        self.subjects = self.load_subjects()
    
    def load_subjects(self):
        subject_dicts = Database.load_subjects(self.student_id)
        subjects = []
        for data in subject_dicts:
            subject = SubjectEntity()
            subject.id = data["id"]
            subject.mark = data["mark"]
            subject.grade = data["grade"]
            subjects.append(subject)
        return subjects

   
    def change_password(self):
        from university_system.university import University
        newPassword = input(f"{CYAN}{indent2}New password: {RESET}")
        university = University()
        while not university.is_valid_password(newPassword):
            print(f"{RED}{indent2}Invalid password. Try again.{RESET}")
            newPassword = input(f"{CYAN}{indent2}New password: {RESET}")

        confirmPassword = input(f"{CYAN}{indent2}Confirm password: {RESET}")
        while(newPassword != confirmPassword):
            print(f"{RED}{indent2}Password does not match - try again{RESET}")
            confirmPassword = input(f"{CYAN}{indent2}Confirm password: {RESET}")
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
        new_subject = SubjectEntity()
        existing_ids = {s.id for s in self.subjects}

        while new_subject.id in existing_ids:
            new_subject = SubjectEntity()

        self.subjects.append(new_subject)
        self.save_subjects()

        return [new_subject]

    def enroll_subject(self):
        if len(self.subjects) >= 4:
            print(f"{RED}{indent2}Students are allowed to enrol in 4 subjects only{RESET}")
            return

        new_subject = SubjectEntity()
        existing_ids = {s.id for s in self.subjects}

        while new_subject.id in existing_ids:
            new_subject = SubjectEntity()

        self.subjects.append(new_subject)
        self.save_subjects()
        print(f"{YELLOW}{indent2}Enrolling in Subject-{new_subject.id}{RESET}")
        print(f"{YELLOW}{indent2}You are now enrolled in {len(self.subjects)} out of 4 subjects{RESET}")

    def remove_subject(self):
        if not self.subjects:
            print(f"{RED}{indent2}No subjects enrolled to remove{RESET}")
            return

        subject_id = input(f"{CYAN}{indent2}Remove Subject by ID: {RESET}")
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                self.save_subjects()
                print(f"{YELLOW}{indent2}Dropping Subject-{subject_id}{RESET}")
                print(f"{YELLOW}{indent2}You are now enrolled in {len(self.subjects)} out of 4 subjects{RESET}")
                return

        print(f"{RED}{indent2}Subject ID {subject_id} not found{RESET}")

    def display_subjects(self):
        print(f"{YELLOW}{indent2}Showing {len(self.subjects)} subjects{RESET}")
        for subject in self.subjects:
            print(f"{indent2}[ Subject::{subject.id:>3} -- mark = {subject.mark:>3} -- grade =  {subject.grade:>3} ]")

    def save_subjects(self):
        subject_dicts = [s.get_subject_json() for s in self.subjects]
        Database.save_subjects(self.student_id, subject_dicts)
