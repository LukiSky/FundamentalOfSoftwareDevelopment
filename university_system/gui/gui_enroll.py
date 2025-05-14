import tkinter as tk
from tkinter import Listbox, ttk, messagebox

from university_system.controllers.subject_controller import SubjectController

class EnrolmentFrame(tk.Tk):
    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id
        self.subject_controller = SubjectController(str(student_id))

        self.title("Student Enrolment")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self._build_ui()
        self._render_subjects()

    def _build_ui(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 16))

        ttk.Label(self, text="Enrol subjects for student ID: " + self.student_id,
                  font=("Helvetica", 28, "bold")).pack(pady=30)

        ttk.Button(self, text="Enrol Subject", command=self._enroll_subject, style="TButton").pack(pady=10)

        self.subject_box = tk.LabelFrame(self, text="Enrolled Subjects", padx=40, pady=30,
                                         font=("Helvetica", 20, "bold"))
        self.subject_box.pack(fill="both", expand=True, padx=20, pady=20)

    def _enroll_subject(self):
        self.lift()
        self.attributes('-topmost', True)
        self.after(0, lambda: self.attributes('-topmost', False))
        
        mySubjects = self.subject_controller.enroll_subjectGUI()

        if mySubjects:
            new_subject = mySubjects[0]
            total_enrolled = len(self.subject_controller.load_subjects())
            message = (
                f"Enrolling in Subject - {new_subject.id}\n\n"
                f"You are now enrolled in {total_enrolled} out of 4 subjects"
            )
            messagebox.showinfo("Enrolment Successful", message)
            self._render_subjects()
        else:
            messagebox.showerror("Enrolment Error", "Students are allowed to enroll in 4 subjects only.")

    def _render_subjects(self):
        # Clear previous widgets in the frame
        for widget in self.subject_box.winfo_children():
            widget.destroy()

        subjects = self.subject_controller.load_subjects()
        for s in subjects:
            ttk.Label(self.subject_box,
                      text=f"ID: {s.id}, Mark: {s.mark}, Grade: {s.grade}",
                      font=("Helvetica", 18)).pack(fill='x', padx=10, pady=6)



def enrollNewSubject(student_id):
    subject_controller = SubjectController(str(student_id))
    
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
    subject_controller = SubjectController(str(student_id))
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

    # ttk.Button(root, text="Show Subjects", command=lambda: enrollNewSubject(student_id)).pack(pady=10)


    root.mainloop()

# Optional for standalone testing
if __name__ == "__main__":
    start_enrollment_window("550431")