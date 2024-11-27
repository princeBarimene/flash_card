from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

window= Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
window.title("Flash Cards")


#creating the canvas
card_back = PhotoImage(file="./images/card_back.png")

card_front = PhotoImage(file="./images/card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400,263, image = card_front)
canvas.grid(column=0, row=0, columnspan= 2)

canvas.create_text(400,150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400,263, text="word", font=("Arial", 60, "bold"))



#buttons

right_button_img = PhotoImage(file="./images/right.png")
unknown_button_img = PhotoImage(file="./images/wrong.png")

right_button = Button(image=right_button_img, highlightthickness=0)
right_button.grid(column=1,row=1)

unknown_button = Button(image=unknown_button_img, highlightthickness=0)
unknown_button.grid(column=0,row=1)








window.mainloop()

