from tkinter import *
import math
import json

# ----- Variables -------#

BACKGROUND_COLOR = "#B1DDC6"



# ------------ UI --------------#

window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

# canvas setup
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Image
card_front_img = PhotoImage(file='flash-cards/images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)

#language text
language_text = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))

# word text
word = canvas.create_text(400, 263, text="School", font=("Ariel", 60, "bold"))

# Grid position
canvas.grid(column=1, row=1, columnspan=2)

# Correct button
correct_image = PhotoImage(file="flash-cards/images/right.png")
correct_button = Button(image=correct_image)
correct_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
correct_button.grid(column=1, row=2)

# Wrong button
wrong_image = PhotoImage(file="flash-cards/images/wrong.png")
wrong_button = Button(image=wrong_image)
wrong_button.config(highlightthickness=0)
wrong_button.grid(column=2, row=2)


mainloop()