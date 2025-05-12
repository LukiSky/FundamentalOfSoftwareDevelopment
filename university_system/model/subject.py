import random
from university_system.utils.utils import *

class Subject:
    def __init__(self):
        self.id = f"{random.randint(1, 999):03d}"  
        self.mark = random.randint(25, 100)        
        self.grade = self.calcGrade(self.mark)     
    @staticmethod
    def calcGrade(mark):
        if mark >= 85:
            return "HD"
        elif mark >= 75:
            return "D"
        elif mark >= 65:
            return "C"
        elif mark >= 50:
            return "P"
        return "Z"

    def get_subject_json(self):
        return {
            "id": self.id,
            "mark": self.mark,
            "grade": self.grade
        }

