import tkinter as tk
from tkinter import ttk

class AlertView(tk.Toplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)
        self.grab_set()
        self.resizable(False, False)

        # Window size
        width, height = 400, 200
        x = self.winfo_screenwidth() // 2 - width // 2
        y = self.winfo_screenheight() // 2 - height // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)

        # Message
        label = ttk.Label(self, text=message, font=("Helvetica", 18), wraplength=360, justify="center")
        label.grid(row=0, column=0, pady=(50, 10), sticky="n")

        # OK button
        ok_btn = ttk.Button(self, text="OK", command=self.close, width=15)
        ok_btn.grid(row=1, column=0, pady=(0, 20))

        self.bind("<Return>", lambda e: self.close())  # Close on Enter

    def close(self):
        self.destroy()
