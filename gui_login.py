
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb



from gui_enrol import start_enrollment_window
from university_system.controllers.student_controller import StudentController

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width * 1)  
window_height = int(screen_height * 0.8) 

root.geometry(f"{window_width}x{window_height}")
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


def myLogin():
    email = emailText.get()
    password = passwordTxt.get()
    studentId = student.loginGUI(email, password)

    if studentId:
        mb.showinfo("Login Successful", "Correct email and password")
        root.destroy()  # Close login window
        start_enrollment_window(studentId)  # ✅ Pass the student ID
    else:
        mb.showerror("Login Failed", "Incorrect email or password")



loginBtn = tk.Button(box, text="Login", command=myLogin)
loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()
