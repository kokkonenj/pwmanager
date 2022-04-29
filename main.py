import argparse
from getpass import getpass
from pw_generator import pw_generator

print("Welcome to your password manager.")
master_password = getpass("Enter your master password: ")
print("What to do next? Options: "
      "[R,r]etrieve a password, "
      "[L,l]ist all services you have saved passwords for, "
      "[G,g]enerate a new password, "
      "[A,a]dd existing password, "
      "[Q,q]uit.")

while True:
    user_input = input("[r,l,g,a,q]: ")
    if user_input == "Q" or user_input == "q":
        print("Exiting..")
        break
    elif user_input == "R" or user_input == "r":
        print("Retrieve password")
    elif user_input == "L" or user_input == "l":
        print("Listing password")
    elif user_input == "G" or user_input == "g":
        print("Generate password")
    elif user_input == "A" or user_input == "a":
        print("Add password")
    else:
        user_input = input("[r,l,g,a,q]: ")
