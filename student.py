from abc import ABC, abstractmethod
import json
import os
import random
import re

DATA_FILE = "student.datfdfdsaddsa"

class User(ABC):
    @abstractmethod
    def menu(self):
        pass


def calcGrade(mark):
      if mark >= 85:
          return "HD"  
      elif mark >= 75:
          return "D"  
      elif mark >= 65:
          return "C" 
      elif mark >= 50:
          return "P" 
      elif mark >= 0:
          return "Z"   

class Subject_Enrollment():
    def __init__(self, student_id):
        self.student_id = student_id
        self.subjects = self.load_subjects()

    def load_subjects(self):
        students = University.load_data()
        for student in students:
            if student["id"] == self.student_id:
                return student.get("subjects", []) or []
        return []

    def saveSubjects(self):
        students = University.load_data()
        for student in students:
            if student["id"] == self.student_id:
                student["subjects"] = self.subjects
                break
        University.save_data(students)

    def menu(self):
        while True:
            choice = input("  Student Course Menu (c/e/r/s/x): ").lower()
            match choice:
                case "c":
                    print("     Updating Password")
                    self.changePassword()
                case "e":
                    self.enrollSubjects()
                case "r":
                    self.removeSubject()
                case "s":
                    self.showSubjects()
                case "x":
                    break
                case _:
                    print("   Error: please either input c, e, r, s, or x")

    def changePassword(self):
        newPassword = input("   New password: ")
        confirmPassword = input("   Confirm password: ")
        while(newPassword != confirmPassword):
            print("Password does not match - try again")
            confirmPassword = input("   Confirm password: ")
        students = University.load_data()
    
        for student in students:
            if student["id"] == self.student_id:
                student["password"] = newPassword
                break
        University.save_data(students)

        

    def enrollSubjects(self):
        if len(self.subjects) >= 4:
            print("   Student are allowed to enrol in 4 subjects only")
            return

        existingId = {s["id"] for s in self.subjects}
        while True:
            subjectID = f"{random.randint(1, 999):03d}"
            if subjectID not in existingId:
                break

        mark = random.randint(25, 100)
        grade = calcGrade(mark)

        self.subjects.append({
            "id": subjectID,
            "mark": mark,
            "grade": grade
        })

        self.saveSubjects()
        print(f"   Enrolling in Subject ID {subjectID}")
        print(f"   You are now enrolled in {len(self.subjects)} out of 4 subjects")

    def removeSubject(self):
        if not self.subjects:
            print("   No subjects enrolled to remove.")
            return

        subjectID = input("   Enter Subject ID to remove: ")
        for s in self.subjects:
            if s["id"] == subjectID:
                self.subjects.remove(s)
                self.saveSubjects()
                print(f"   Subject {subjectID} removed.")
                return
        print("   Subject ID not found in enrolled list.")

    def showSubjects(self):
        if not self.subjects:
            print("   No subjects enrolled.")
        else:
            print("   Enrolled Subjects:")
            for s in self.subjects:
                print(f"    [ Subject::{s['id']} -- Mark = {s['mark']} -- Grade = {s['grade']}]")

    def calcGrade(self, mark):
      if mark >= 85:
          return "HD"  
      elif mark >= 75:
          return "D"  
      elif mark >= 65:
          return "C" 
      elif mark >= 50:
          return "P" 
      elif mark >= 0:
          return "Z"   





class Student(User):
    def menu(self):
        while True:
            choice = input("    Student System (l/r/x): ").lower()
            match choice:
                case "l":
                    print("   Student Sign In")
                    self.login()
                case "r":
                    print("   Student Sign Up")
                    self.register()
                case "x":
                    break
                case _:
                    print("   Error: please either input l, r, or x")

    def checkPasswordFormat(self, password, email):
        if not password[0].isupper() or sum(c.isalpha() for c in password) < 5 or not re.search(r"\d{3,}$", password) or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        return True

    def login(self):
      email = input("   Email: ")
      password = input("    Password: ")
      students = University.load_data()
      
      if not self.checkPasswordFormat(password, email):
          print("   Incorrect email or password format")
          return

      for student in students:
          if student["email"] == email and student["password"] == password:
              print(f"   Welcome, {student['name']}!")
              subject_enrollment = Subject_Enrollment(student["id"])
              subject_enrollment.menu()
              return

      print("   Student does not exist or credentials are incorrect.")


    def register(self):
        email = input(" Email: ")
        password = input("  Password: ")
        students = University.load_data()
        for student in students:
            if student["email"] == email:
                print(f"    Student {student['name']} already exists.")
                return
        if not self.checkPasswordFormat(password, email):
            print("   Incorrect email or password format")
            return
        else:
            print("   email and password formats acceptable")

        name = input("  Name: ")
        existing_ids = {student.get("id") for student in students if "id" in student}
        while True:
            new_id = f"{random.randint(1, 999999):06d}"
            if new_id not in existing_ids:
                print(f"    Enrolling Student {name}")
                students.append({
                    "id": new_id,
                    "name": name,
                    "email": email,
                    "password": password
                })
                University.save_data(students)
                return


class Admin(User):
    def menu(self):
        while True:
            choice = input("  Admin System (c/g/p/r/s/x): ").lower()
            match choice:
                case "c":
                  
                    self.clear_database()
                case "g":
                    print("Grade Grouping")
                    self.group_students()
                case "p":
                    print("PASS/FAIL Partition")
                    self.partition_students()
                case "r":
                  
                    self.remove_student()
                case "s":
                    print("Student List")
                    self.show_students()
                case "x":
                    break
                case _:
                    print("Error: please either input c, g, p, r, s, or x")

    def clear_database(self):
        if self.checkStudentEmpty():
            return
        confirm = input("Are you sure you want to clear the database (Y)ES/ (N)O: ").lower()
        if confirm.lower() == "Y":
            University.save_data([])
            print("Students data cleared")
        elif confirm.lower() == "N":
          return
        else:
            print("Operation cancelled — input must be 'Y' or 'N' only.")

    def group_students(self):
      if self.checkStudentEmpty():
          return

      students = University.load_data()
      groups = {"HD": [], "D": [], "C": [], "P": [], "Z": []}

      for student in students:
          subjects = student.get("subjects", [])
          marks = [sub.get("mark", 0) for sub in subjects]
          avg = sum(marks) / len(marks) if marks else 0
          grade = calcGrade(avg)
          student_info = f"{student['name']} :: {student['id']} --> GRADE: {grade} - MARK: {avg:.2f}"
          groups[grade].append(student_info)


      for grade, students_in_group in groups.items():
          if len(students_in_group) != 0:
            print(f"{grade} --> {students_in_group}")


    def partition_students(self):
        if self.checkStudentEmpty():
            return
        students = University.load_data()
        passed, failed = [], []

        for student in students:
            subjects = student.get("subjects", [])
            marks = [sub.get("mark", 0) for sub in subjects]
            avg = sum(marks) / len(marks) if marks else 0
            grade = calcGrade(avg)
            student_info = f"{student['name']} :: {student['id']} --> GRADE: {grade}"

            if avg >= 50:
                passed.append(student_info)
            else:
                failed.append(student_info)

        print(f"  Fail --> {failed}")
        print(f"  Fail --> {passed}")

    def remove_student(self):
        if self.checkStudentEmpty():
            return
        student_id = input("Remove by ID: ")
        students = University.load_data()
        new_students = [s for s in students if s["id"] != student_id]

        if len(students) == len(new_students):
            print(f"  Student {student_id} does not exist")
        else:
            University.save_data(new_students)
            print(f"  Removing Student {student_id} Account")

    def show_students(self):
        if self.checkStudentEmpty():
            return
        students = University.load_data()
  
        for s in students:
            print(f"{s['name']} :: {s['id']} --> Email: {s['email']}")
    def checkStudentEmpty(self):
        students = University.load_data()
        if not students:
            print("   < Nothing to Display>")
            return True
        return False

class University:

    @staticmethod
    def load_data():
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Error: The data file is empty or corrupted.")
                return []
            return data

    @staticmethod
    def save_data(data):
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)

    def menu(self):
        while True:
            choice = input("University System: (A)dmin, (S)tudent, or X: ").lower()
            match choice:
                case "a":
                    admin = Admin()
                    admin.menu()
                case "s":
                    student = Student()
                    student.menu()
                case "x":
                    print("Thank You")
                    break
                case _:
                    print("Error: please either input A, S, or X")

if __name__ == '__main__':
    myUniv = University()
    myUniv.menu()
