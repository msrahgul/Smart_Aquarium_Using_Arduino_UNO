import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import serial
import time

BAUD_RATE = 9600
PORT = 'COM12'
db = mysql.connector.connect(host="localhost", user="root", password="Rahgul@2006", database="Smart_Aquarium_User")
cursor = db.cursor()

class SmartAquariumApp:
    def __init__(self, username):
        self.board = None
        self.root = tk.Tk()
        self.root.title("Smart Aquarium Control Panel")
        self.root.geometry("1280x768")

        image = Image.open("background_image_1.jpg")
        image = image.resize((1280, 768), Image.BILINEAR)
        image = image.resize((1280, 768))
        self.background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self.root, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_main_interface(username)

    def show_main_interface(self, Name):
        control_frame = tk.LabelFrame(self.root, text=f"Welcome {Name}", padx=10, pady=10, bg="white", fg="black")
        control_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button_read = tk.Button(control_frame, text="Display Sensor Readings", command=self.display_sensor_readings,
                                bg="#008CBA", fg="white", font=("Comic Sans MS", 14, "bold"))
        button_read.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

        button_feed = tk.Button(control_frame, text="Feed Fish", command=self.feed_fish, bg="#f44336", fg="white",
                                font=("Comic Sans MS", 14, "bold"))
        button_feed.grid(row=1, column=0, padx=10, pady=10, ipadx=20, ipady=10)

        button_change_water = tk.Button(control_frame, text="Change Water", command=self.change_water, bg="#4CAF50",
                                        fg="white", font=("Comic Sans MS", 14, "bold"))
        button_change_water.grid(row=2, column=0, padx=10, pady=10, ipadx=20, ipady=10)

        def close_main():
            cl_dsr = messagebox.askokcancel("Quit", "Are you sure you want to logout?")
            if cl_dsr:
                self.logout()
        button_logout = tk.Button(self.root, text="Logout", command=close_main,
                                  bg="red", fg="white", font=("Comic Sans MS", 12))
        button_logout.place(relx=0.95, rely=0.1, anchor=tk.NE)
        def Profile():
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            for user in users:
                if user[0]==Name:
                    messagebox.showinfo("PROFILE","Name :"+Name+"\nUsername :"+user[1]+"\nMobile Number :"+user[3])
        button_profile = tk.Button(self.root, text="Profile", command=Profile,
                                  bg="Blue", fg="white", font=("Comic Sans MS", 12))
        button_profile.place(relx=0.95, rely=0.03, anchor=tk.NE)

    def logout(self):
        if self.board:
            self.board.exit()
        self.root.destroy()

    def display_sensor_readings(self):
        def close_dsr():
            secondary_window.destroy()

        def sensor_read():
            ser = serial.Serial(PORT,BAUD_RATE)
            turbidity_value = ser.readline().decode().strip()
            Sensor_reading_1.config(text=str(turbidity_value))
            water_level_percentage = ser.readline().decode().strip()
            Sensor_reading_2.config(text=str(water_level_percentage))
            
        secondary_window = tk.Toplevel()
        secondary_window.title("Sensor Reading")
        secondary_window.geometry("1280x768")

        # Load and display the image
        try:
            background_image = Image.open("SENSOR_READING.jpeg")
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = tk.Label(secondary_window, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            messagebox.showerror("Image Error", "Image file not found")
            return
        except Exception as e:
            messagebox.showerror("Image Error", "IMAGE NOT FOUND")
            return

        sensor_reading_label = tk.LabelFrame(secondary_window, text="The Sensor Reading is as follows:", font=("Comic Sans MS", 18))
        sensor_reading_label.place(relx=0.5, rely=0.5, anchor='center')

        Sensor_reading_1 = tk.Label(sensor_reading_label, text="", font=("Comic Sans MS", 18))
        Sensor_reading_1.grid(row=1, column=0)
        
        Sensor_reading_2 = tk.Label(sensor_reading_label, text="", font=("Comic Sans MS", 18))
        Sensor_reading_2.grid(row=2, column=0)


        Refresh = tk.Button(sensor_reading_label, text="REFRESH", command=sensor_read, bg="blue", fg="white",
                            font=("Comic Sans MS", 8, "bold"))
        Refresh.grid(row=0, column=2)

        button_close = tk.Button(secondary_window, text="Close window", command=close_dsr, bg="red", fg="white",
                                 font=("Comic Sans MS", 14, "bold"))
        button_close.place(x=1200, y=700, anchor='center')

        secondary_window.mainloop()

    def feed_fish(self):
        feed_window = tk.Toplevel()
        feed_window.title("FEED FISH")
        feed_window.geometry("720x480")

            # Background Image
        feed_bg_image = Image.open("fish_feed_background.jpg")
        feed_bg_image = feed_bg_image.resize((720, 480), Image.BILINEAR)
        feed_bg_photo = ImageTk.PhotoImage(feed_bg_image)
        bg_label = tk.Label(feed_window, image=feed_bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = feed_bg_photo

            # Title
        title_label = tk.Label(feed_window, text="Feed Your Fish", fg="white", bg="#1f618d", font=("Algerian", 20))
        title_label.pack(pady=20)

        def feed_action():
            ser = serial.Serial('COM12', 9600)
            def move_servo(angle):
                ser.write(str(angle).encode())
                time.sleep(0.1)  # Wait for servo to reach the desired position
            move_servo(90)
            move_servo(0)
            ser.close()

        feed_button = tk.Button(feed_window, text="Feed", command=feed_action, bg="#4CAF50", fg="white",font=("Comic Sans MS", 14, "bold"))
        feed_button.pack(pady=20)

        def close_dsr():
            feed_window.destroy()

        button_close = tk.Button(feed_window, text="Close window", command=close_dsr, bg="red", fg="white",
                                     font=("Comic Sans MS", 14, "bold"))
        button_close.place(x=600, y=400, anchor='center')

        feed_window.mainloop()

    def change_water(self):
        Change_Water_Window = tk.Toplevel()
        Change_Water_Window.title("CHANGE WATER")
        Change_Water_Window.geometry("720x480")

        # Background Image
        Change_Water_bg_image = Image.open("Changewater.jpeg")
        Change_Water_bg_image = Change_Water_bg_image.resize((720, 480), Image.BILINEAR)
        Change_Water_bg_photo = ImageTk.PhotoImage(Change_Water_bg_image)
        bg_label = tk.Label(Change_Water_Window, image=Change_Water_bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = Change_Water_bg_photo

        # Title
        title_label = tk.Label(Change_Water_Window, text="Change Your Water", fg="black",
                               font=("Algerian", 20))
        title_label.pack(pady=20)

        def handle_water_change():
            ser = serial.Serial('COM12', 9600)
            RELAY_1_ON = b'1'
            RELAY_1_OFF = b'2'
            RELAY_2_ON = b'3'
            RELAY_2_OFF = b'4'

            def control_relays(command):
                ser.write(command)
            messagebox.showinfo("STATUS","CLEANING IN PROGRESS")
            try:
                # Wait for Arduino to signal readiness
                while True:
                    if ser.readline().strip() == b'Ready':
                        print("Arduino is ready")
                        break

                while True:
                    distance_str = ser.readline().decode().strip()
                    Change_water_status.config(text="DISTANCE"+str(distance_str))
                    if distance_str:
                        distance = int(distance_str[:-2])
                        if distance < 12:
                            control_relays(RELAY_1_ON)
                        elif distance > 5:
                            control_relays(RELAY_2_ON)
                        else:
                            control_relays(RELAY_1_OFF)
                            control_relays(RELAY_2_OFF)

                    time.sleep(1)
            except:
                ser.close()
        Change_Water_button = tk.Button(Change_Water_Window, text="Change Water", command=handle_water_change,
                                        bg="#4CAF50", fg="white",
                                        font=("Comic Sans MS", 14, "bold"))
        Change_Water_button.pack(pady=20)

        Change_water_status = tk.Label(Change_Water_Window, text="", fg="black",font=("Comic Sans MS", 20))
        Change_water_status.pack(pady=20)

        def close_dsr():
            Change_Water_Window.destroy()

        button_close = tk.Button(Change_Water_Window, text="Close window", command=close_dsr, bg="red", fg="white",
                                 font=("Comic Sans MS", 14, "bold"))
        button_close.place(x=600, y=400, anchor='center')

        Change_Water_Window.mainloop()


class LoginPage:
    def __init__(self, master, login_callback):
        self.master = master
        self.master.title("Login")
        self.master.geometry("1920x1080")
        self.login_callback = login_callback
        self.board = None

        image = Image.open("background_image.jpg")
        image = image.resize((1920, 1080), Image.BILINEAR)
        image = image.resize((1920, 1080))
        self.background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_login_form()

    def create_login_form(self):
        login_frame = tk.Frame(self.master, bg="black", bd=5, highlightthickness=0, highlightbackground="black")
        login_frame.place(x=540, y=200, anchor='center')

        username_label = tk.Label(login_frame, text="Username:", fg="white", bg="black", font=("Algerian", 14))
        username_label.grid(row=0, column=0, padx=5, pady=5)

        self.username_entry = tk.Entry(login_frame, font=("Bernard MT Condensed", 14))
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        password_label = tk.Label(login_frame, text="Password:", fg="white", bg="black", font=("Algerian", 14))
        password_label.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = tk.Entry(login_frame, show="*", font=("Bernard MT Condensed", 14))
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        login_button = tk.Button(login_frame, text="Login", command=self.login, bg="#4caf50", fg="white",
                                 font=("Algerian", 14))
        login_button.grid(row=2, column=0, columnspan=1, padx=10)

        register_button = tk.Button(login_frame, text="Register", command=self.register, bg="#f44336", fg="white",
                                    font=("Algerian", 14))
        register_button.grid(row=2, column=1, columnspan=2, padx=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        val = False
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            if username == user[1] and password == user[2]:
                val = True
                Name = user[0]
                break

        if val:
            self.master.destroy()
            self.login_callback(Name)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def register(self):
        def save_user_details():
            name = name_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            mobile = mobile_entry.get()

            sql = "INSERT INTO users (Name, Username, Password, Mobile) VALUES (%s, %s, %s, %s)"
            val = (name, username, password, mobile)
            cursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Registration Successful", "User details saved successfully.")
            register_window.destroy()

        register_window = tk.Tk()
        register_window.title("Registration")

        name_label = tk.Label(register_window, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(register_window)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        username_label = tk.Label(register_window, text="Username:")
        username_label.grid(row=1, column=0, padx=10, pady=5)
        username_entry = tk.Entry(register_window)
        username_entry.grid(row=1, column=1, padx=10, pady=5)

        password_label = tk.Label(register_window, text="Password:")
        password_label.grid(row=2, column=0, padx=10, pady=5)
        password_entry = tk.Entry(register_window, show="*")
        password_entry.grid(row=2, column=1, padx=10, pady=5)

        mobile_label = tk.Label(register_window, text="Mobile Number:")
        mobile_label.grid(row=3, column=0, padx=10, pady=5)
        mobile_entry = tk.Entry(register_window)
        mobile_entry.grid(row=3, column=1, padx=10, pady=5)

        register_button = tk.Button(register_window, text="Register", command=save_user_details)
        register_button.grid(row=4, columnspan=2, pady=10)
        register_window.mainloop()

def open_smart_aquarium_app(username):
    app = SmartAquariumApp(username)

def main():
    root = tk.Tk()
    login_page = LoginPage(root, open_smart_aquarium_app)  # Pass the login_callback function directly
    root.mainloop()

if __name__ == "__main__":
    main()
