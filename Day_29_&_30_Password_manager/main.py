from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_info = website_entry.get()
    mail_info = mail_entry.get()
    password_info = password_entry.get()
    new_data = {
        web_info: {
            "email": mail_info,
            "password": password_info,
        }
    }

    if len(web_info) == 0 or len(password_info) == 0:
        messagebox.showerror(title="Error", message="Don't leave any field empty")

    else:
        try:
            with open("Password Keeper.json", "r") as data_file:
                new_file = json.load(data_file)
                new_file.update(new_data)
        except:
            with open("Password Keeper.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("Password Keeper.json", "w") as data_file:
                json.dump(new_file, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #
def lookup_password():
    web_info = website_entry.get()
    try:
        with open("Password Keeper.json", "r") as data_file:
            password_finder = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No data file found!")
    else:
        for key in password_finder:
            if key == web_info:
                mail = password_finder[key]["email"]
                password = password_finder[key]["password"]
                messagebox.showinfo(f"{key}", f"Email: {mail}\n" f"Password: {password}")
                pyperclip.copy(password)
            else:
                messagebox.showerror(title="Error!", message=f"No details for {web_info} found in the directory")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Toyo's Password Generator")
window.config(padx=50, pady=50)

my_canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=image)
my_canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entry
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()
mail_entry = Entry(width=51)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "adetbabz@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

#Button
password_button = Button(text="Generate Password", command=generate_password, width=17)
password_button.grid(row=3, column=2)
add_button = Button(text="add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=17, command=lookup_password)
search_button.grid(row=1, column=2)







window.mainloop()
