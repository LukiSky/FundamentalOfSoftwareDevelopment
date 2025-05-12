import tkinter as tk
from university_system.controllers.subject_controller import SubjectController

class SubjectFrame(tk.Tk):
    def __init__(self, student_id):
        super().__init__()
        self.title("View Subjects")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.student_id = str(student_id)
        self.subject_controller = SubjectController(self.student_id)

        total_enrolled_cnt = len(self.subject_controller.load_subjects())

        title_label = tk.Label(self, text="Current Enrolments", font=("Helvetica", 28, "bold"))
        title_label.pack(pady=(30, 10))

        subtext = tk.Label(self, text=f"Showing {total_enrolled_cnt} subjects", font=("Helvetica", 18))
        subtext.pack(pady=(0, 30))

        subject_box = tk.LabelFrame(self, text="Enroled Subjects", padx=40, pady=30, font=("Helvetica", 20, "bold"))
        subject_box.pack(padx=40, pady=50, fill="both", expand=True)

        for s in self.subject_controller.load_subjects():
            label_text = f"Subject ID: {s.id} | Mark: {s.mark} | Grade: {s.grade}"
            tk.Label(subject_box, text=label_text, anchor="w", font=("Helvetica", 18)).pack(fill='x', padx=10, pady=6)

# For Test run
if __name__ == "__main__":
    app = SubjectFrame("425505")
    app.mainloop()
