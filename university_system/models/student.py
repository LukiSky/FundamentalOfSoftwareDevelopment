import random
from university_system.models.student_entity import StudentEntity
from university_system.utils.utils import *
from university_system.controllers.subject_controller import SubjectController
from university_system.models.exception import LoginError, ValidationError
from university_system.models.database import Database

class Student:
    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        self.students = Database.load_data()
        
    def save_student(self, student):
        self.students.append(student)
        Database.save_data(self.students)
        self.load_students() 

    def login(self):
            email = input(f"{indent}Email: ")
            password = input(f"{indent}Password: ")

            if not self.checkPasswordEmailFormat(password, email):
                raise ValidationError("Incorrect email or password format")
            
            print(f"{indent}email and password formats acceptable")

            for student in self.students:
                if student["email"] == email and student["password"] == password:
                    # print(f"{emptySpace}Welcome, {student['name']}!")
                    subject_controller = SubjectController(student["id"])
                    subject_controller.menu()
                    return
                
            raise LoginError(f"{indent}Student does not exist")

    def login_gui(self, email, password):
        if len(email) == 0 or len(password) == 0:
            raise LoginError("Please complete all required fields")
        
        elif not self.checkPasswordEmailFormat(password, email):
            raise ValidationError()

        for student in self.students:
            if student["email"] == email and student["password"] == password:
                print(f"{indent}Welcome, {student['name']}!")              
                return student["id"]

        raise LoginError("Student does not exist") 


    def check_valid_student(self, email, password):
        for student in self.students:
            if student["email"] == email and student["password"] == password:
                return True
            else:
                return False           
    
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
        email = input(f"{indent}Email: ")
        password = input(f"{indent}Password: ")

        if not self.checkPasswordEmailFormat(password, email):
            raise ValidationError()
        
        print(f"{indent}email and password formats acceptable")

        for student in self.students:
            if student["email"] == email:
                raise LoginError(f"Student {student['name']} already exists.")

        name = input(f"{indent}Name: ")
        existing_ids = {student["id"] for student in self.students}
        new_id = f"{random.randint(1, 999999):06d}"
        
        if new_id not in existing_ids:
            print(f"{indent}Enrolling Student {name}")
            new_student = StudentEntity(new_id, name, email, password)
            self.save_student(new_student.get_student_json())

    def get_student_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }