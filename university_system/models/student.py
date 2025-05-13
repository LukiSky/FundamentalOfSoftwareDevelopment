from university_system.util.util import *
class Student:
    def __init__(self, name, email, password, id):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def get_student_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

