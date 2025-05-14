import tkinter as tk
from tkinter import ttk

class HomeFrame:
    def __init__(self, student_id):
        self.student_id = student_id
        self.root = tk.Tk()
        self.root.title("Student Home")
        self.root.state('zoomed')

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.setup_ui()
        self.root.mainloop()

    def setup_ui(self):
        center_frame = ttk.Frame(self.root)
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Texts
        welcome_label = ttk.Label(center_frame, text=f"Welcome, Student {self.student_id}!", font=("Helvetica", 28, "bold"))
        welcome_label.pack(pady=(30, 10))

        instruction_label = ttk.Label(center_frame, text="Please select a menu option below.", font=("Helvetica", 18))
        instruction_label.pack(pady=(0, 30))

        # Menu
        menu_frame = ttk.LabelFrame(center_frame, padding=(40, 20), labelanchor='n')
        menu_frame.pack()

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 16))

        enrol_btn = ttk.Button(menu_frame, text="Enrol Subjects", command=self.enrol_subjects, width=20, style="TButton")
        enrol_btn.pack(pady=20)

        # view_btn = ttk.Button(menu_frame, text="View Subjects", command=self.view_subjects, width=20, style="TButton")
        # view_btn.pack(pady=10)

    def enrol_subjects(self):
        EnrolmentFrame(self.root, self.student_id)

    # def view_subjects(self):
    #     SubjectFrame(self.student_id)


# # For Test run
# if __name__ == "__main__":
#     HomeFrame("790337")