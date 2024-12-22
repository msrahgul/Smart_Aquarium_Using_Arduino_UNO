import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("500x300")

        self.create_login_form()

    def create_login_form(self):
        login_frame = tk.Frame(self.master)
        login_frame.pack(pady=20)

        username_label = tk.Label(login_frame, text="Username:")
        username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        password_label = tk.Label(login_frame, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        login_button = tk.Button(login_frame, text="Login", command=self.login_user)
        login_button.grid(row=2, columnspan=2, pady=10)

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check username and password
        if self.check_credentials(username, password):
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def check_credentials(self, username, password):
        # Read registered details from the file
        with open("user_details.txt", "r") as file:
            for line in file:
                details = line.strip().split(", ")
                saved_username = details[0].split(": ")[1]
                saved_password = details[2].split(": ")[1]
                if username == saved_username and password == saved_password:
                    return True
        return False

# Usage example:
if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()
