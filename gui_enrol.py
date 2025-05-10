import tkinter as tk
from tkinter import ttk, messagebox
from university_system.controllers.subject_controller import SubjectController


def start_enrollment_window(student_id):
    root = tk.Tk()
    root.title("Student Enrolment")
    root.state('zoomed')

    subject_controller = SubjectController(str(student_id))

    def enroll():
        mySubjects = subject_controller.enroll_subjectGUI()

        if mySubjects:
            new_subject = mySubjects[0]
            total_enrolled = len(subject_controller.load_subjects())
            message = (
                f"Enrolling in Subject- {new_subject.id}\n\n"
                f"You are now enrolled in {total_enrolled} out of 4 subjects"
            )
            messagebox.showinfo("Enrollment Successful", message)
            render_subjects()
        else:
            messagebox.showerror("Enrollment Error", "Students are allowed to enroll in 4 subjects only.")

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 16))

    ttk.Label(root, text="Enroll subjects for student ID: " + student_id, font=("Helvetica", 22, "bold")).pack(pady=30)
    ttk.Button(root, text="Enroll Subject", command=enroll, style="TButton").pack(pady=10)

    subject_box = tk.LabelFrame(root, text="Enroled Subjects", padx=40, pady=30, font=("Helvetica", 18, "bold"))
    subject_box.pack(padx=40, pady=50, fill="both", expand=True)

    def render_subjects():
        for widget in subject_box.winfo_children():
            widget.destroy()
        for s in subject_controller.load_subjects():
            label_text = f"Subject ID: {s.id} | Mark: {s.mark} | Grade: {s.grade}"
            tk.Label(subject_box, text=label_text, anchor="w", font=("Helvetica", 16)).pack(fill='x', padx=10, pady=6)
    
    render_subjects()

    root.mainloop()

# Optional for standalone testing
if __name__ == "__main__":
    start_enrollment_window("425505")
