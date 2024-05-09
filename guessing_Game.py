from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Guessing Game!!!")
root.minsize(500, 500)
root.maxsize(500, 500)
root.config(bg="gray")


rand_num = random.randint(1, 10)
attempt_left = 3


def show():
    global attempt_left
    no = int(en.get())
    en.delete(0, END)

    if no==rand_num:
        lbl2.config(text="Congrats! You Win!!")
        btn.config(state=DISABLED)
    else:
        attempt_left -=1
        if attempt_left==0:
            lbl2.config(text=f"Game over! The number was {rand_num}")
            btn.config(state=DISABLED)
        else:
            lbl2.config(text=f"Wrong guess. {attempt_left} attempts left.")


lbl1 = Label(root, text="Guessing Game", font="comicsansms 19 bold", fg="red", bd=4, relief=RAISED, bg="yellow")
lbl1.place(x=140, y=20)

lbl2 = Label(root, text="", fg="white", font="comicsansms 15 bold", bg="gray")
lbl2.place(x=115, y=120)

en = Entry(root, fg="red", font="arial 10 bold")
en.place(x=170, y=270, height=25)

btn = Button(root, text="Submit Guess", font="comicsansms 10 bold", command=show)
btn.place(x=190, y=310)

root.mainloop()