import tkinter as tk
from tkinter.ttk import *
from datetime import datetime

counter = 66600
running = False
count = 1

def lap():
    global count 
    lbx1.insert(tk.END,datetime.fromtimestamp(counter-1).strftime("%H:%M:%S"))
    lbx2.insert(tk.END,str(count) + ". ")
    stpwtch_root.update()
    count = count + 1

def multiple_yview(*args):
    lbx2.yview(*args)
    lbx1.yview(*args)

def counter_label(label):
    def count():
        if running:
            global counter
    # To manage the initial delay.
            if counter == 66600:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string
            label['text'] = display
            label.after(1000, count)
            counter += 1
    # Triggering the start of the counter.
    count()
# start function of the stopwatch
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
# Stop function of the stopwatch
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False
# Reset function of the stopwatch
def Reset(label):
    global counter, count
    counter = 66600
    count = 1
    lbx1.delete(0, tk.END)
    lbx2.delete(0, tk.END)
    # If rest is pressed after pressing stop.
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Welcome!'
    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = 'Starting...'

stpwtch_root = tk.Tk()
stpwtch_root.title("Stopwatch")
scrollbar = Scrollbar(stpwtch_root)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

# stpwtch_root.iconbitmap("stopwatch.ico")
stpwtch_root.configure()
# Fixing the window size.
stpwtch_root.minsize(width=250, height=400)
stpwtch_root.maxsize(width=250, height=400)
#label = Label(stpwtch_root, text="Welcome!")
label = Label(stpwtch_root, text="Welcome!", font=("Arial", 25)) #fg="#4B8BBE", bg="#FFE873", font="Verdana 30 bold")
label.pack()
f = Frame(stpwtch_root)
start = Button(f, text='Start', width=6, command=lambda: Start(label))
stop = Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Button(f, text='Reset', width=6,
                    state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(fill = tk.BOTH , side="left")
stop.pack(fill = tk.BOTH , side="left")
reset.pack(fill = tk.BOTH ,side="left")

Button(stpwtch_root, text="Lap", command=lap, width=16).pack(ipadx=20)  # , bd='5').place(x=85, y=112)
f1=Frame(stpwtch_root)
f1.pack(pady=5)
lbx2 = tk.Listbox(f1,width=2, height=14, yscrollcommand=scrollbar.set)
lbx1 = tk.Listbox(f1,width=18, height=8,yscrollcommand= scrollbar.set)
scrollbar.config(command=multiple_yview)
lbx2.pack(side=tk.LEFT)
lbx1.pack(ipadx=20, ipady=50, pady=6, side=tk.LEFT)

stpwtch_root.mainloop()