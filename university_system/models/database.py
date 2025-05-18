import json
import os
from university_system.utils.utils import *
<<<<<<< HEAD

class Database:
    DATA_FILE = "FundamentalOfSoftwareDevelopment/university_system/data/students.data"
=======

### Color Controls ###

RESET  = "\033[0m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"

####

class Database:
    DATA_FILE = "university_system/data/students.data"
>>>>>>> 74ad414099a2dfb4c0e430ca8882601a35a366d3

    @staticmethod
    def load_data():
        if not os.path.exists(Database.DATA_FILE):
            with open(Database.DATA_FILE, 'w') as f:
                json.dump([], f)
            return []
        with open(Database.DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"{RED}Error: The data file is empty or corrupted.{RESET}")
                return []

    @staticmethod
    def load_subjects(student_id):
        students = Database.load_data()
        for student in students:
            if student["id"] == student_id:
                return student.get("subjects", [])
        return []

    @staticmethod
    def save_data(data):
        with open(Database.DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        # print(f" Data saved to {os.path.abspath(Database.DATA_FILE)}")

    @staticmethod
    def remove_student_by_id(student_id):
        students = Database.load_data()
        updated_students = [s for s in students if s["id"] != student_id]
        if len(students) == len(updated_students):
<<<<<<< HEAD
            print(f"{indent}Student {student_id} does not exist")
        else:
            Database.save_data(updated_students)
            print(f"{indent}Removing Student {student_id} Account")
=======
            print(f"{RED}{indent}Student {student_id} does not exist{RESET}")
        else:
            Database.save_data(updated_students)
            print(f"{YELLOW}{indent}Removing Student {student_id} Account{RESET}")
>>>>>>> 74ad414099a2dfb4c0e430ca8882601a35a366d3

    @staticmethod
    def save_subjects(student_id, subjects):
        students = Database.load_data()
        for student in students:
            if student["id"] == student_id:
                student["subjects"] = subjects
                break
        Database.save_data(students)

    @staticmethod
    def clear_all_data():
        Database.save_data([])


