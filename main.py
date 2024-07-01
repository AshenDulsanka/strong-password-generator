import string
import random

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
