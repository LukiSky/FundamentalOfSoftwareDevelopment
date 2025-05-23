import tkinter as tk
from tkinter import ttk
from university_system.models.subject import Subject
from university_system.gui.alert_view import AlertView

class EnrolmentFrame(tk.Tk):
    def __init__(self, root, student_id):
        super().__init__()
        self.title("Student Enrolment")
        self.root = root

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.student_id = str(student_id)
        self.subject = Subject(self.student_id)

        self._build_ui()
        self._render_subjects()
        self.root.mainloop()

    def _build_ui(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 16))

        ttk.Label(self, text="Enrol subjects for student ID: " + self.student_id,
                  font=("Helvetica", 28, "bold")).pack(pady=30)

        ttk.Button(self, text="Enrol Subject", command=self._enroll_subject, style="TButton").pack(pady=10)

        self.subject_box = tk.LabelFrame(self, text="Enroled Subjects", padx=40, pady=30,
                                         font=("Helvetica", 20, "bold"))
        self.subject_box.pack(padx=40, pady=50, fill="both", expand=True)

    def _enroll_subject(self):
        mySubjects = self.subject.enroll_subject_gui()

        if mySubjects:
            new_subject = mySubjects[0]
            total_enrolled = len(self.subject.load_subjects())
            message = (
                f"Enrolling in Subject - {new_subject.id}\n\n"
                f"You are now enroled in {total_enrolled} out of 4 subjects"
            )
            self.showMessage("Enrolment Successful", message)
            self._render_subjects()
        else:
            self.showMessage("Enrolment Error", "Students are allowed to \n enroll in 4 subjects only.")

    def _render_subjects(self):
        for widget in self.subject_box.winfo_children():
            widget.destroy()
        for s in self.subject.load_subjects():
            label_text = f"Subject ID: {s.id} | Mark: {s.mark} | Grade: {s.grade}"
            tk.Label(self.subject_box, text=label_text, anchor="w", font=("Helvetica", 18)).pack(
                fill='x', padx=10, pady=6
            )

    def showMessage(self, title, msg):
        AlertView(self.root, title, msg)

# For Test run
if __name__ == "__main__":
    app = EnrolmentFrame("425505")
    app.mainloop()