from tkinter import *
import math
import json
import pandas
import random

# ----- Variables -------#

BACKGROUND_COLOR = "#B1DDC6"

# ------- Read data from CSV -----------#
data = pandas.read_csv("flash-cards/data/french_words.csv")
data_dict = data.to_dict(orient="records")


# ------- Generate next card ------#

def next_card():
    card = random.choice(data_dict)
    canvas.itemconfig(canvas_bg, image=card_front_img)
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=card["French"])
    
# ------ Flip Card -----#

def flip_card():
    canvas.itemconfig(canvas_bg, image=card_back_img)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=card["English"])


# ------------ UI --------------#

window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

# canvas setup
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Image
card_front_img = PhotoImage(file='flash-cards/images/card_front.png')
card_back_img = PhotoImage(file='flash-cards/images/card_back.png')
canvas_bg = canvas.create_image(400, 263, image=card_front_img)

#language text
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

# word text
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Grid position
canvas.grid(column=1, row=1, columnspan=2)

# Correct button
correct_image = PhotoImage(file="flash-cards/images/right.png")
correct_button = Button(image=correct_image, command=next_card)
correct_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
correct_button.grid(column=1, row=2)

# Wrong button
wrong_image = PhotoImage(file="flash-cards/images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.config(highlightthickness=0)
wrong_button.grid(column=2, row=2)

next_card()

mainloop()