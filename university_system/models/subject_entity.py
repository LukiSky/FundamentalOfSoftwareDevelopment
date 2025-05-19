import random

class SubjectEntity:
    def __init__(self):
        from university_system.university import University
        self.id = f"{random.randint(1, 999):03d}"  
        self.mark = random.randint(25, 100)        
        self.grade = University.calc_grade(self.mark)  

    def get_subject_json(self):
        return {
            "id": self.id,
            "mark": self.mark,
            "grade": self.grade
        }