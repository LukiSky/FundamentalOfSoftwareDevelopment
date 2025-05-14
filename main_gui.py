import tkinter as tk

from university_system.gui.gui_login import LoginFrame
from university_system.controllers.student_controller import StudentController

root = tk.Tk()
root.state('zoomed') #full size window
root.title("Student Login타이틀")
root.configure(bg='#262626') #HEX COLOR(로그인창 색깔)검은색
root.resizable(False, False)#위 아래 창 사이즈 조절하는거, true  면 조절가능인데 우리는 False로 고정시킴

# screen_width = root.winfo_screenwidth()//2 #가로 사이즈 조절 100%
# screen_height = root.winfo_screenheight() #세로 사이즈 조절 100%
# root.geometry(f"{screen_width}x{screen_height}")

# model = StudentController()
box = LoginFrame(root) #frame불러오기
box.pack(expand=False, fill="both")

root.mainloop()