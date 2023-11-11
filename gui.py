import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import os
import requests

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Server Manager")
        self.root.geometry("1080x720")
        self.root.resizable(False, False)

        self.create_widgets()

        self.root.mainloop()
        
    def create_widgets(self):
        pass
    
    def login_window(self):
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Team Login")
        
        self.login_name = tk.StringVar()
        self.login_password = tk.StringVar()
        
        self.login_name_label = tk.Label(self.login_window, text="Benutzername: ")
        self.login_name_label.grid(row=0, column=0)
        self.login_name_entry = tk.Entry(self.login_window, textvariable=self.login_name)
        self.login_name_entry.grid(row=0, column=1)
        
        self.login_password_label = tk.Label(self.login_window, text="Passwort: ")
        self.login_password_label.grid(row=1, column=0)
        self.login_password_entry = tk.Entry(self.login_window, textvariable=self.login_password)
        self.login_password_entry.grid(row=1, column=1)
        
        self.login_button = tk.Button(self.login_window, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2)
        
    def login(self):
        pass
    
if __name__ == "__main__":
    app = App()