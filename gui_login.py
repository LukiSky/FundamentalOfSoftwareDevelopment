import tkinter as tk
from tkinter import messagebox as mb
from gui_home import start_home_window
from university_system.controllers.student_controller import StudentController

root = tk.Tk()
root.state('zoomed') #full size window

root.title("Student Login")
root.configure(bg='black')
root.resizable(False, False)


box = tk.LabelFrame(root, text='Sign In', bg='black', fg='white', padx=20, pady=20, font=('Times New Roman', 10, 'bold'))
box.columnconfigure(0, weight=1)
box.columnconfigure(1, weight=3)
box.place(relx=0.5, rely=0.5, anchor='center')  # Center the box in the window

emailLb1 = tk.Label(box, text="Email:",justify='left', fg='white',
                    font=('Times New Roman', 12, 'bold'), bg='black')
emailLb1.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
passwordLb1 = tk.Label(box, text="Password:", fg='white', font=('Times New Roman', 12, 'bold'),
                       bg="black")
passwordLb1.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

emailText = tk.StringVar()
emailField = tk.Entry(box, textvariable=emailText)
emailField.grid(column=1, row=0, padx=5, pady=5)
emailField.focus()

passwordTxt = tk.StringVar()
passwordField = tk.Entry(box, textvariable=passwordTxt, show="*")
passwordField.grid(column=1, row=1, padx=5, pady= 5)

cancelBtn = tk.Button(box, text="Cancel")
cancelBtn.grid(column=1, row=3, sticky=tk.W, padx=30, pady=5)

student = StudentController()


def login():
    email = emailText.get().strip()
    password = passwordTxt.get().strip()

    try:
        studentId = student.login_gui(email, password)
        root.destroy() 
        start_home_window(studentId)
    except ValueError as e:
        mb.showerror("Login Failed", str(e))

loginBtn = tk.Button(box, text="Login", command=login)
loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()