# GUI_Enroll.py
import tkinter as tk
from tkinter import Listbox, ttk, messagebox



def enrollNewSubject(student_id):
    subject_controller = subject_controller(str(student_id))
    
    mySubjects = subject_controller.enroll_subjectGUI()

    if mySubjects:
        new_subject = mySubjects[0]
        total_enrolled = len(subject_controller.load_subjects())
        message = (
            f"Subject {new_subject.id} enrolled successfully!\n"
            f"Mark: {new_subject.mark}, Grade: {new_subject.grade}\n"
            f"Total Enrolled Subjects: {total_enrolled}"
        )
        messagebox.showinfo("Enrollment Successful", message)

        for s in subject_controller.load_subjects():
            print(f"ID: {s.id}, Mark: {s.mark}, Grade: {s.grade}")

        return new_subject.id, new_subject.mark, new_subject.grade
    else:
        messagebox.showerror("Enrollment Error", "Students are allowed to enroll in 4 subjects only.")
        return None

def start_enrollment_window(student_id):
    root = tk.Tk()
    root.title("Main App (Test Harness)")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width * 0.5)  
    window_height = int(screen_height * 0.8) 

    root.geometry(f"{window_width}x{window_height}")
    subject_controller = subject_controller(str(student_id))
    listbox = Listbox(root,
                  bg="white",
                  font=("constantia",35),
                  width=12)
    listbox.pack()

    for s in subject_controller.load_subjects():
        print(s)
        listbox.insert(listbox.size(),f"ID:{s.id},Mark:{s.mark},Grade:{s.grade}")


    listbox.config(height=listbox.size(), width=window_width)

    ttk.Label(root, text="Enroll subjects for student ID: " + student_id).pack(pady=10)
    
    ttk.Button(root, text="Enroll Subject", command=lambda: enrollNewSubject(student_id)).pack(pady=10)

    root.mainloop()

# Optional for standalone testing
if __name__ == "__main__":
    start_enrollment_window("550431")
