import tkinter as tk

from university_system.gui.gui_login import LoginFrame
from university_system.controllers.student_controller import StudentController

root = tk.Tk()
root.state('zoomed') #full size window
root.title("Student Login")
root.configure(bg='#262626')
root.resizable(False, False)

box = LoginFrame(root)
# box.pack( fill="both")

root.mainloop()

# while True:
    # break
# i = 5
# while i >= 0:
#     print("hey")
#     i-=1