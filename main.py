import string
from random import *
from tkinter import *
import tkinter as tk

window = Tk()
window.title("Strong Password Generator")
window.geometry("500x400")

def new_rand():
    while True:
        try:
            pw_length = int(num_box.get())
            break
        except ValueError:
            pw_box.delete(0, END)
            pw_box.insert(0, "Please enter a valid choice")
            return

    pw_box.delete(0, END)
    pw = ''

    while True:
        try:
            if upper.get() == 1 and numbs.get() == 0 and symbs.get() == 0:
                for x in range(pw_length):
                    pw += ''.join(choice(string.ascii_uppercase))
                break
            elif upper.get() == 1 and numbs.get() == 1 and symbs.get() == 0:
                pw += ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(pw_length))
                break
            elif upper.get() == 1 and numbs.get() == 1 and symbs.get() == 1:
                pw += ''.join(choice(string.ascii_uppercase + string.digits + string.punctuation) for _ in range(pw_length))
                break
            elif upper.get() == 0 and numbs.get() == 1 and symbs.get() == 0:
                pw += ''.join(choice(string.digits) for _ in range(pw_length))
                break
            elif upper.get() == 0 and numbs.get() == 1 and symbs.get() == 1:
                pw += ''.join(choice(string.digits + string.punctuation) for _ in range(pw_length))
                break
            elif upper.get() == 0 and numbs.get() == 0 and symbs.get() == 1:
                pw += ''.join(choice(string.punctuation) for _ in range(pw_length))
                break
            elif upper.get() == 1 and numbs.get() == 0 and symbs.get() == 1:
                pw += ''.join(choice(string.ascii_uppercase + string.punctuation) for _ in range(pw_length))
                break
            elif upper.get() == 0 and numbs.get() == 0 and symbs.get() == 0:
                pw += ''.join(choice(string.ascii_letters) for _ in range(pw_length))
                break
            else:
                pw_box.insert(0, "Please enter a valid choice")
        except ValueError:
            pw_box.insert(0, "Please enter a valid choice")

    pw_box.insert(0, pw)

def copy_clip():
    window.clipboard_clear()
    window.clipboard_append(pw_box.get())

lf = LabelFrame(window, text="Enter the length of the password: ")
lf.pack(pady=20)

num_box = Entry(lf, font=("Poppins, 16"), width=25, justify=CENTER)
num_box.pack(padx=30, pady=20)

upper = tk.IntVar()
numbs = tk.IntVar()
symbs = tk.IntVar()

c1 = Checkbutton(window, text="Uppercase", variable=upper, onvalue=1, offvalue=0, command=new_rand)
c1.pack()

c2 = Checkbutton(window, text="Numbers", variable=numbs, onvalue=1, offvalue=0, command=new_rand)
c2.pack()

c3 = Checkbutton(window, text="Symbols", variable=symbs, onvalue=1, offvalue=0, command=new_rand)
c3.pack()

button_frame = Frame(window)
button_frame.pack(pady=20)

gen_button = Button(button_frame, text="Generate Password", command=new_rand)
gen_button.grid(row=0, column=0, padx=10)

clip_button = Button(button_frame, text="Copy to Clipboard", command=copy_clip)
clip_button.grid(row=0, column=1, padx=10)

pw_box = Entry(window, text='', font=("Poppins, 16"), bd=0, bg="systembuttonface", width=60, justify=CENTER)
pw_box.pack(pady=20, padx=50)

window.mainloop()