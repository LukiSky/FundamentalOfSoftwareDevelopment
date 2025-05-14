import tkinter as tk

from university_system.gui.gui_login import LoginFrame
from university_system.controllers.student_controller import StudentController

root = tk.Tk()
root.state('zoomed') #full size window
root.title("Student Login")
root.configure(bg='#262626')
root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

model = StudentController()
box = LoginFrame(root, model)
box.pack(expand=True, fill="both")

root.mainloop()