import json
import os

from university_system.util.util import *

class Database:
    DATA_FILE = "university_system/data/student.data"
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
                print("Error: The data file is empty or corrupted.")
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
        print(f" Data saved to {os.path.abspath(Database.DATA_FILE)}")

    @staticmethod
    def remove_student_by_id(student_id):
        students = Database.load_data()
        updated_students = [s for s in students if s["id"] != student_id]
        if len(students) == len(updated_students):
            print(f"{emptySpace}Student {student_id} does not exist")
        else:
            Database.save_data(updated_students)
            print(f"{emptySpace}Removing Student {student_id} Account")

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


