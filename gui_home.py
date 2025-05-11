import tkinter as tk
from tkinter import ttk
from gui_enrol import start_enrollment_window
from gui_subject import show_subjects


def start_home_window(student_id):
    root = tk.Tk()
    root.title("Student Home")
    root.state('zoomed')
    
    center_frame = ttk.Frame(root)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Texts
    welcome_label = ttk.Label(center_frame, text=f"Welcome, Student {student_id}!", font=("Helvetica", 28, "bold"))
    welcome_label.pack(pady=(30, 10))

    instruction_label = ttk.Label(center_frame, text="Please select a menu option below.", font=("Helvetica", 18))
    instruction_label.pack(pady=(0, 30))

    # Menu
    menu_frame = ttk.LabelFrame(center_frame, padding=(40, 20), labelanchor='n')
    menu_frame.pack()

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 16))

    ttk.Button(menu_frame, text="Enrol Subjects", command=lambda: start_enrollment_window(student_id), width=20, style="TButton").pack(pady=20)
    ttk.Button(menu_frame, text="View Subjects", command=lambda: show_subjects(student_id), width=20, style="TButton").pack(pady=10)

    root.mainloop()

# Test run
if __name__ == "__main__":
    start_home_window("790337")