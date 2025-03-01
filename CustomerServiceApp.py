#Import libraries
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

#Defining the class and creating the login window
class CustomerServiceApp:
    def __init__(self):
        self.login_window = tk.Tk()
        self.login_window.title("Login")
        
        self.username_label = tk.Label(self.login_window, text="Username:") #label with the username
        self.username_label.pack()

        self.username_entry = tk.Entry(self.login_window) #first button to log in
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_window, text="Pa55w0rd")#label with the secure password
        self.password_label.pack()

        self.login_button = tk.Button(self.login_window, text="Login", command=self.check_credentials)
        self.login_button.pack()

    def check_credencials(self):
        username = self.username_entry.get()
        password = self.password.entry.get()

        if username == "admin" and password == "password":
            self.login_window = tk.Tk()
            self.main_window.title("Customer Service App")
            self.main_window.geometry("500x300")

        