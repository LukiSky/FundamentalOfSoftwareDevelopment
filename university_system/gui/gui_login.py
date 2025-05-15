import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

from university_system.gui.AlertView import AlertView

from university_system.gui.gui_home import HomeFrame
from university_system.models.student import Student


class LoginFrame(tk.LabelFrame):

    def __init__(self, root) -> None:
        super().__init__(root)
        self.root = root
        self.student = Student()
        self.configure(bg='#262626')

        self.box = tk.LabelFrame(root, text='Login', bg='#262626', fg='white', padx=20, pady=20, font=('Helvetica', 28, 'bold'))
        self.box.columnconfigure(0, weight=1)
        self.box.columnconfigure(1, weight=3)
        self.box.place(relx=0.5, rely=0.5, anchor='center')

        self.emailLb1 = tk.Label(self.box, text="Email:",justify='left', fg='white',
                            font=('Helvetica', 18, 'bold'), bg=root["bg"])
        self.emailLb1.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        self.passwordLb1 = tk.Label(self.box, text="Password:", fg='white', font=('Helvetica', 18, 'bold'),
                            bg=root["bg"])
        self.passwordLb1.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

        self.emailText = tk.StringVar()
        self.emailField = tk.Entry(self.box, textvariable=self.emailText)
        self.emailField.grid(column=1, row=0, padx=5, pady=5)
        self.emailField.focus()

        self.passwordTxt = tk.StringVar()
        self.passwordField = tk.Entry(self.box, textvariable=self.passwordTxt, show="*")
        self.passwordField.grid(column=1, row=1, padx=5, pady= 5)

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 15))

        self.cancelBtn = ttk.Button(self.box, text="Cancel", command=self.close_window, style="TButton")
        self.cancelBtn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        self.loginBtn = ttk.Button(self.box, text="Login", command=self.login, style="TButton")
        self.loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

    def login(self):
        email = self.emailText.get().strip()
        password = self.passwordTxt.get().strip()
        print(email)
        print(password)
        try:
            studentId = self.student.login_gui(email, password)
            if(studentId):
                self.root.destroy() 
                HomeFrame(studentId)
            else:
                # AlertView(self.root, "Fail in here", "Im in here")
                mb.showerror("Login in here","Please input the correct password and email")
                # AlertView
        except ValueError as e:

            self.showError("Login Failed", str(e))

    def close_window(self):
        self.root.destroy()

    def showError(self, title, msg):
        AlertView(self.root, title, msg)