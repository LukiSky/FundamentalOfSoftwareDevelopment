import tkinter as tk
from university_system.controllers.subject_controller import SubjectController

def show_subjects(student_id):
    root = tk.Tk()
    root.title("View Subjects")
    root.state('zoomed')

    subject_controller = SubjectController(str(student_id))
    total_enrolled_cnt = len(subject_controller.load_subjects())

    title_label = tk.Label(root, text="Current Enrolments", font=("Helvetica", 28, "bold"))
    title_label.pack(pady=(30, 10))

    subtext = tk.Label(root, text=f"Showing {total_enrolled_cnt} subjects", font=("Helvetica", 18))
    subtext.pack(pady=(0, 30))

    subject_box = tk.LabelFrame(root, text="Enroled Subjects", padx=40, pady=30, font=("Helvetica", 20, "bold"))
    subject_box.pack(padx=40, pady=50, fill="both", expand=True)

    for s in subject_controller.load_subjects():
        label_text = f"Subject ID: {s.id} | Mark: {s.mark} | Grade: {s.grade}"
        tk.Label(subject_box, text=label_text, anchor="w", font=("Helvetica", 18)).pack(fill='x', padx=10, pady=6)

    root.mainloop()


# Test run
if __name__ == "__main__":
    show_subjects("425505")