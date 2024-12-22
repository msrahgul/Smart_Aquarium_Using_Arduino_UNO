import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class RegistrationPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Registration")
        self.master.geometry("500x300")

        self.create_registration_form()

    def create_registration_form(self):
        registration_frame = tk.Frame(self.master)
        registration_frame.pack(pady=20)

        username_label = tk.Label(registration_frame, text="Username:")
        username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(registration_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        name_label = tk.Label(registration_frame, text="Name:")
        name_label.grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(registration_frame)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        password_label = tk.Label(registration_frame, text="Password:")
        password_label.grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(registration_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        mobile_label = tk.Label(registration_frame, text="Mobile Number:")
        mobile_label.grid(row=3, column=0, padx=10, pady=5)
        self.mobile_entry = tk.Entry(registration_frame)
        self.mobile_entry.grid(row=3, column=1, padx=10, pady=5)

        register_button = tk.Button(registration_frame, text="Register", command=self.register_user)
        register_button.grid(row=4, columnspan=2, pady=10)

    def register_user(self):
        username = self.username_entry.get()
        name = self.name_entry.get()
        password = self.password_entry.get()
        mobile = self.mobile_entry.get()

        # Write user details to a text file
        with open("user_details.txt", "a") as file:
            file.write(f"Username: {username}, Name: {name}, Password: {password}, Mobile Number: {mobile}\n")
        messagebox.showinfo("Registration Successful", "Registration successful.")

# Usage example:
if __name__ == "__main__":
    root = tk.Tk()
    registration_page = RegistrationPage(root)
    root.mainloop()
