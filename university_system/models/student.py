import random
from university_system.models.student_entity import StudentEntity
from university_system.utils.utils import *
from university_system.controllers.subject_controller import SubjectController
from university_system.models.exception import LoginError, ValidationError
from university_system.models.database import Database

### Color Controls ###

RESET  = "\033[0m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"

####

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
                raise ValidationError()
            
            print(f"{YELLOW}{indent}email and password formats acceptable{RESET}")

            for student in self.students:
                if student["email"] == email and student["password"] == password:
                    # print(f"{emptySpace}Welcome, {student['name']}!")
                    subject_controller = SubjectController(student["id"])
                    subject_controller.menu()
                    return
                
            raise LoginError(f"{RED}{indent}Student does not exist{RESET}")

    def login_gui(self, email, password):
        if len(email) == 0 or len(password) == 0:
            raise LoginError(f"{RED}Please complete all required fields{RESET}")
        
        elif not self.checkPasswordEmailFormat(password, email):
            raise ValidationError()

        for student in self.students:
            if student["email"] == email and student["password"] == password:
                print(f"{indent}Welcome, {student['name']}!")              
                return student["id"]

        raise LoginError(f"{RED}Student does not exist{RESET}") 


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
        
        print(f"{YELLOW}{indent}email and password formats acceptable{RESET}")

        for student in self.students:
            if student["email"] == email:
                raise LoginError(f"{RED}Student {student['name']} already exists.{RESET}")

        name = input(f"{indent}Name: ")
        existing_ids = {student["id"] for student in self.students}
        new_id = f"{random.randint(1, 999999):06d}"
        
        if new_id not in existing_ids:
            print(f"{YELLOW}{indent}Enrolling Student {name}{RESET}")
            new_student = StudentEntity(new_id, name, email, password)
            self.save_student(new_student.get_student_json())

    def get_student_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }