from tkinter import *
import pandas
import random

BACKGROUND_COLOR="#B1DDC6"
current_word={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_word
    global flip_timer
    window.after_cancel((flip_timer))
    current_word=random.choice(to_learn)
    canvas.itemconfig(title_text,text="French",fill="black")
    canvas.itemconfig(word_text,text=current_word["French"],fill="black")
    canvas.itemconfig(photo_background,image=photo_front_image)
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text,text="English",fill="white")
    canvas.itemconfig(word_text,text=current_word["English"],fill="white")
    canvas.itemconfig(photo_background,image=photo_back_image)

def is_known():
    to_learn.remove(current_word)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)




canvas=Canvas(width=800,height=526,highlightthickness=0)
photo_front_image=PhotoImage(file="images/card_front.png")
photo_back_image=PhotoImage(file="images/card_back.png")
photo_background=canvas.create_image(400,263,image=photo_front_image)
canvas.config(bg=BACKGROUND_COLOR)
title_text=canvas.create_text(400,123,text="Title",font=("Ariel",40,"italic"))
word_text=canvas.create_text(400,300,text="Word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

photo_right_image=PhotoImage(file="images/right.png")
right_button=Button(image=photo_right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=0)


photo_wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=photo_wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=1)



next_card()


window.mainloop()


