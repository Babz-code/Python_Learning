from tkinter import *

import pandas
import pandas as pd
import random
from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# #Read Csv file
try:
    df = pd.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    original_df = pd.read_csv("data/french_words.csv")
    data = original_df.values.tolist()
else:
    data = df.values.tolist()

choice_text = []

def generate_words():
    global choice_text
    choice_text = random.choice(data)
    french_choice = choice_text[0]
    return french_choice

def next_words():
    global timer
    window.after_cancel(timer)
    new_word = generate_words()
    canva.itemconfig(initial_word, text=new_word, fill="black")
    canva.itemconfig(my_image, image=img_front)
    canva.itemconfig(my_text, text="French", fill="black")
    timer = window.after(3000, func=flip_card)

def flip_card():
    canva.itemconfig(my_image, image=img_back)
    canva.itemconfig(my_text, text="English", fill="white")
    canva.itemconfig(initial_word, fill="white", text=choice_text[1])

def is_known():
    data.remove(choice_text)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/Words_to_learn.csv", index=False)
    next_words()

choice_word = generate_words()
timer = window.after(3000, func=flip_card)

canva = Canvas(width=800, height=526, highlightthickness=0)
img_back = PhotoImage(file="images/card_back.png")
img_front = PhotoImage(file="images/card_front.png")
my_image = canva.create_image(400, 263, image=img_front)
canva.config(bg=BACKGROUND_COLOR)
my_text = canva.create_text(400, 150, text="French", font=("ariel", 40, "italic"))
initial_word = canva.create_text(400, 263, text=f"{choice_word}", font=("ariel", 60, "bold"))
canva.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")


# The buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_words)
wrong_button.grid(row=1,column=0)
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1,column=1)







window.mainloop()