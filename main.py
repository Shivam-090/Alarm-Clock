from tkinter import *
import datetime as dt
from time import strftime
# from stopwatch import *
# from alarm import *
# from timer import *

root = Tk()
root.title("Digital Clock Project")
root.geometry("850x550")

heading = Label(root, text="Digital Clock", font=(
    "Helvetica 25 bold"), fg="red").pack(pady=30)

date = dt.datetime.now()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
leftframe = Frame(root)
leftframe.pack(side=LEFT)
rightframe = Frame(root)
rightframe.pack(side=RIGHT)


def timing():
    string = strftime('%H:%M:%S %p')
    real_time1.config(text=string)
    real_time1.after(1000, timing)


button_dict = {}
option = ["Alarm", "Stopwatch", "Timer"]

for i in option:
    def test(x = i):
        if x == "Alarm":
            alarm_clock()
        elif x == "Stopwatch":
            stopwatch()
        elif x == "Timer":
            timer()

    button_dict[i] = Button(root, text=i, background="white", activebackground="light cyan", padx=70, pady=10, width=5,command=test).pack(pady=25, ipadx=25)
    
# alarm_btn = Button(leftframe, text="Alarm", background="white", activebackground="light cyan", padx=70, pady=10, width=5, command= alarm_clock).pack()
# stopwatch_btn = Button(leftframe, text="Stopwatch", background="white", activebackground="light cyan", padx=70, pady=10, width=5, command= stopwatch).pack()
# timer_btn = Button(leftframe, text="Timer", background="white", activebackground="light cyan", padx=70, pady=10, width=5, command= timer).pack()  
real_time = Label(
    rightframe, text=f"{date:%A, %B %d, %Y}", font="Calibri, 20").pack(padx=40)
real_time1 = Label(rightframe, font=("Calibri 20"))
real_time1.pack()
timing()
btn = Button(bottomframe, text='Exit!', command=root.destroy,
             width=10, activebackground="#ff033e", anchor="n").pack(pady=60)
root.mainloop()