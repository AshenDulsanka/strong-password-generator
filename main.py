import string
from random import *
from tkinter import *

root = Tk()
root.title("Strong Password Generator")
root.geometry("500x400")

def new_rand():
    pw_box.delete(0, END)
    pw_length = int(num_box.get())
    pw = ''

    for x in range(pw_length):
        pw += chr(randint(33, 126))

    pw_box.insert(0, pw)

def copy_clip():
    root.clipboard_clear()
    root.clipboard_append(pw_box.get())

lf = LabelFrame(root, text="Enter the length of the password: ")
lf.pack(pady=20)

num_box = Entry(lf, font=("Poppins, 16"))
num_box.pack(padx=30, pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

gen_button = Button(button_frame, text="Generate Password", command=new_rand)
gen_button.grid(row=0, column=0, padx=10)

clip_button = Button(button_frame, text="Copy to Clipboard", command=copy_clip)
clip_button.grid(row=0, column=1, padx=10)

pw_box = Entry(root, text='', font=("Poppins, 16"), bd=0, bg="systembuttonface")
pw_box.pack(pady=20)


while True:
    try:
        length = int(input("Enter the length of the password: "))
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    try:
        choice = int(input("\n1. Letters only \n2. Letters and Numbers \n3. Letters, Numbers and Special Characters \n\nEnter your choice: "))

        if choice == 1:
            password = ''.join(random.choice(string.ascii_letters) for _ in range(length))
            break
        elif choice == 2:
            password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
            break
        elif choice == 3:
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
            break
        else:
            print("\n\nPlease enter a valid choice")
        
    except ValueError:
        print("\n\nPlease enter a valid choice\n")
    
print("\nYour password is: ", password)
