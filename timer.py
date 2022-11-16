import time
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
            
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
        
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        timer_root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
        
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


# creating Tk window
timer_root = tk.Tk()

# setting geometry of tk window
timer_root.minsize(width=250,height=120)
timer_root.maxsize(width=250,height=120)

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
timer_root.title("Time Counter")

# Declaration of variables
hour=tk.StringVar()
minute=tk.StringVar()
second=tk.StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

f1=Frame(timer_root)
f1.pack()

# Use of Entry class to take input from the user
hourEntry= Entry(f1, width=3, font=("Arial",18,""),
                textvariable=hour)
# hourEntry.place(x=80,y=20)
hourEntry.pack(side=tk.LEFT)

minuteEntry= Entry(f1, width=3, font=("Arial",18,""),
                textvariable=minute)
# minuteEntry.place(x=130,y=20)
minuteEntry.pack(side=tk.LEFT)

secondEntry= Entry(f1, width=3, font=("Arial",18,""),
                textvariable=second)
secondEntry.pack(side=tk.LEFT)

Label(timer_root, text="Hour   Minute   Second").pack()
#Label(timer_root, text="Minute").pack(side=LEFT)
#Label(timer_root, text="Second").pack(side=LEFT)

# button widget
btn = Button(timer_root, text='Set Time Countdown',command= submit)
# btn = Button(timer_root, text='Set Time Countdown', bd='5',command= submit)
btn.pack(ipadx=20,pady=8)
# btn.place(x = 70,y = 120)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
timer_root.mainloop()