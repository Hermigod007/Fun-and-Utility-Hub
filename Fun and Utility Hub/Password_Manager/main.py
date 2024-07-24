from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

class PasswordManager:
    def __init__(self):
        self.window = Tk()
        self.window.config(padx=50, pady=50)

        self.canvas = Canvas(height=200, width=200)
        self.lock_image = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.lock_image)
        self.canvas.grid(column=1, row=0)

        self.website_label = Label(text="Website:")
        self.website_label.config(font=("Arial", 12, "bold"))
        self.website_label.grid(column=0, row=1)

        self.website_textbox = Entry(width=42)
        self.website_textbox.focus()
        self.website_textbox.grid(column=1, row=1, columnspan=2)

        self.email_label = Label(text="Email/Username:")
        self.email_label.config(font=("Arial", 12, "bold"))
        self.email_label.grid(column=0, row=2)

        self.email_textbox = Entry(width=42)
        self.email_textbox.grid(column=1, row=2, columnspan=2)

        self.password_label = Label(text="Password:")
        self.password_label.config(font=("Arial", 12, "bold"))
        self.password_label.grid(column=0, row=3)

        self.generate_password_button = Button(text="Generate Password", command=self.generate_password, width=14)
        self.generate_password_button.grid(column=2, row=3)

        self.password_textbox = Entry(width=24)
        self.password_textbox.grid(column=1, row=3, pady=5)

        self.add_button = Button(text="Add", command=self.data_entered, width=36, pady=3)
        self.add_button.grid(column=1, row=4, columnspan=2)

        self.search_button = Button(text="Search", width=10, command=self.find_password)
        self.search_button.grid(column=2, row=1, columnspan=2)

        self.window.mainloop()

    def find_password(self):
        value = self.website_textbox.get()
        try:
            with open("data.json") as data_file:
                data_dict = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="ERROR", message="No Data File Found")
        else:
            if value in data_dict:
                val = data_dict[value]
                messagebox.showinfo(title="Search",
                                    message=f"Your Email is: {val['email']}\n Your Password is: {val['password']}\n")
            else:
                messagebox.showerror(title="ERROR", message="No Details for website exists")

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
        password_numbers = [random.choice(symbols) for _ in range(random.randint(2, 4))]
        password_symbols = [random.choice(numbers) for _ in range(random.randint(2, 4))]

        password_list = password_letters + password_numbers + password_symbols

        random.shuffle(password_list)

        password = "".join(password_list)

        print(f"Your password is: {password}")

        self.password_textbox.insert(0, password)
        pyperclip.copy(password)

    def update_json_data(self, new_data):
        with open("data.json", mode="w") as file:
            json.dump(new_data, file, indent=4)

            self.website_textbox.delete(0, END)
            self.email_textbox.delete(0, END)
            self.password_textbox.delete(0, END)

    def data_entered(self):
        a = self.website_textbox.get()
        b = self.email_textbox.get()
        c = self.password_textbox.get()

        new_data = {
            a: {
                "email": b,
                "password": c,
            }
        }

        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            messagebox.showinfo(title="Recheck", message="Please enter info in all the data fields")
        else:
            try:
                with open("data.json", mode="r") as file:
                    info = json.load(file)
                    info.update(new_data)
            except FileNotFoundError:
                self.update_json_data(new_data)
            else:
                self.update_json_data(info)










