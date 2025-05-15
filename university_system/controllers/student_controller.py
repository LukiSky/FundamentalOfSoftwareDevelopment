import random
from university_system.controllers.subject_controller import SubjectController
from university_system.controllers.user_controller import UserController
from university_system.database import Database
from university_system.models.student import Student


from university_system.util.util import *

class StudentController(UserController):
    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        self.students = Database.load_data()
    def save_student(self, student):
        self.students.append(student)
        Database.save_data(self.students)
        self.load_students() 
    def menu(self):
        while True:
            choice = input(f"{emptySpace}Student System (l/r/x): ").lower()
            match choice:
                case "l":
                    print(f"{emptySpace}Student Sign In")
                    self.login()
                case "r":
                    print(f"{emptySpace}Student Sign Up")
                    self.register()
                case "x":
                    break
                case _:
                    print(f"{emptySpace}Error: please either input l, r, or x")
    def login(self):
        while True:
            email = input(f"{emptySpace}Email: ")
            password = input(f"{emptySpace}Password: ")

            for student in self.students:
                if student["email"] == email and student["password"] == password:
                    print(f"{emptySpace}Welcome, {student['name']}!")
                    subject_controller = SubjectController(student["id"])
                    subject_controller.menu()
                    return
            print("   Student does not exist")
            break

    def loginGUI(self, email, password):
        while True:
            for student in self.students:
                if student["email"] == email and student["password"] == password:
                    print(f"{emptySpace}Welcome, {student['name']}!")              
                    return student["id"]
            return False
            break
    
    def checkPasswordEmailFormat(self, password, email):
        from university_system.university import University
        university = University()
      
        boolPassword = university.is_valid_password(password)
        boolEmail = university.is_valid_email(email)

        if(boolPassword == True and boolEmail == True):
            return True
        else:
            return False

    def register(self):
        email = input(" Email: ")
        password = input("  Password: ")

        if not self.checkPasswordEmailFormat(password, email):
            print("   Incorrect email or password format")
            return

        for student in self.students:
            if student["email"] == email:
                print(f"   Student {student['name']} already exists.")
                return

        name = input("  Name: ")
        existing_ids = {student["id"] for student in self.students}

        while True:
            new_id = f"{random.randint(1, 999999):06d}"
            try:
                if new_id not in existing_ids:
                    print(f"{emptySpace}Enrolling Student {name}")
                    new_student = Student(name, email, password, new_id)
                    self.save_student(new_student.get_student_json())
                    return
            except:
                print("Error: Id is out of range")