from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

to_learn = {}

def next_card():
    
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= current_card['French'], fill= "black")
    canvas.itemconfig(card_background, image =card_front)

    flip_timer = window.after(3000, func=flip_card)

    

def flip_card():
    
    canvas.itemconfig(card_background, image =card_back)

    
    canvas.itemconfig(card_title, text= "English", fill="white")
    canvas.itemconfig(card_word, text= current_card['English'] , fill="white")




def is_known():
    to_learn.remove(current_card)

    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv",index=False)
    next_card()



window= Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
window.title("Flash Cards")

flip_timer = window.after(3000, func=flip_card)

try:
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:

    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")








    
    
    


#creating the canvas
card_back = PhotoImage(file="./images/card_back.png")

card_front = PhotoImage(file="./images/card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400,263, image = card_front)
canvas.grid(column=0, row=0, columnspan= 2)

card_title = canvas.create_text(400,150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("Arial", 60, "bold"))



#buttons

right_button_img = PhotoImage(file="./images/right.png")
unknown_button_img = PhotoImage(file="./images/wrong.png")

right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(column=1,row=1)

unknown_button = Button(image=unknown_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0,row=1)


next_card()





window.mainloop()

