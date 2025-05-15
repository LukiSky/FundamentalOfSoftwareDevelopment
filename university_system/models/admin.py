from university_system.models.database import Database
from university_system.utils.utils import *

class Admin:

    def checkStudentEmpty(self):
        students = Database.load_data()
        if not students:
            print(f"{indent2}<Nothing to Display>")
            return True
        return False

    def clearStudentData(self):
        if self.checkStudentEmpty():
            return
        confirm = input(f"{indent}Are you sure you want to clear the database (Y)ES/ (N)O: ").strip()

        if confirm.lower() == "y":
            Database.save_data([])
            print(f"{indent}Students data cleared")
        elif confirm.lower() == "n":
          return
        else:
            print(f"{indent}Operation cancelled — input must be 'Y' or 'N' only.")

    def getGrade(self, student):
        from university_system.university import University
        subjects = student.get("subjects", [])
        marks = [sub.get("mark", 0) for sub in subjects]
        avg = sum(marks) / len(marks) if marks else 0
        grade = University.calcGrade(avg)
        return grade, avg

    def organizeByGrade(self):
        if self.checkStudentEmpty():
            return
        students = Database.load_data()
        groups = {"HD": [], "D": [], "C": [], "P": [], "Z": []}

        for student in students:
            grade, avg = self.getGrade(student)
            student_info = f"{student['name']} :: {student['id']} --> GRADE: {grade} - MARK: {avg:.2f}"
            groups[grade].append(student_info)

        for grade, students_in_group in groups.items():
            if len(students_in_group) != 0:
                print(f"{indent}{grade}  --> {students_in_group}")

    def categorizeByPassStatus(self):
        if self.checkStudentEmpty():
            return
        students = Database.load_data()
        passed, failed = [], []

        for student in students:

            grade, avg = self.getGrade(student)
            student_info = f"{student['name']} :: {student['id']} --> GRADE: {grade}"

            if avg >= 50:
                passed.append(student_info)
            else:
                failed.append(student_info)
        print(f"{indent}Pass --> {passed}")
        print(f"{indent}Fail --> {failed}")


    def remove_student(self):
        if self.checkStudentEmpty():
            return
        student_id = input(f"{indent}Remove by ID: ")
        Database.remove_student_by_id(student_id)


    def viewAllStudents(self):
        if self.checkStudentEmpty():
            return
        students = Database.load_data()
        
        for s in students:
            print(f"{indent}{s['name']:<10} :: {s['id']} --> Email: {s['email']}")
    
    def sortStudent(self, typeOfSort):
        def myId(e):
            return e['id']
        def myEmail(e):
            return e['email']
        def myName(e):
            return e['name']
        
        if self.checkStudentEmpty():
            return
        students = (Database.load_data())
        if(typeOfSort == "si"):
            students.sort(key=myId)
        elif(typeOfSort == "se"):
            students.sort(key=myEmail)
        elif(typeOfSort == "sn"):
            students.sort(key=myName)
      
        for s in students:
            print(f"{indent}{s['name']:<10} :: {s['id']} --> Email: {s['email']}")

