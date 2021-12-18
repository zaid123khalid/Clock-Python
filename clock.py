from tkinter import Label, Tk
from time import strftime


def update():
    time_string = strftime("%I:%M:%S %p")
    l1.config(text=time_string)

    day_string = strftime("%A")
    l2.config(text=day_string)

    date_string = strftime("%d-%b-%Y")
    l3.config(text=date_string)

    l1.after(1000, update)


clock = Tk()
clock.resizable(False, False)
clock.config(bg="Black")
clock.title('CLOCK')

l1 = Label(clock, font=("Free style", 50, "italic"), fg="#00FF00", bg="black")
l1.pack()

l2 = Label(clock, font=("Free style", 50, "italic"), fg="#00FF00", bg="black")
l2.pack()

l3 = Label(clock, font=("Free style", 50, "italic"), fg="#00FF00", bg="Black")
l3.pack()

update()

clock.mainloop()
