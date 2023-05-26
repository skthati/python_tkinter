from tkinter import *
import math

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_url = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as df:
        df.write(f"{web_url} | {username} | {password} |\n ")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file='password-manager/logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=1)

website_label = Label(text="Website URL: ")
website_label.grid(column=0, row=2)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=2, columnspan=2)

username_label = Label(text="Username: ")
username_label.grid(column=0, row=3)

username_entry = Entry(width=35)
username_entry.grid(column=1, row=3, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=4)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=4)

generate_password_button = Button(text="Generate Password", width=11)
generate_password_button.grid(column=2, row=4)

add_password_button = Button(text="Add", width=32, command=save)
add_password_button.grid(column=1, row=5, columnspan=2)

mainloop()