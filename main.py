from getpass import getpass

import file_handler
import pw_handler
import utils


if __name__ == '__main__':
    print("Welcome to your password manager.")
    master_password = getpass("Enter your master password: ")
    print("What to do next? Options: \n"
          "[R,r]etrieve a password, \n"
          "[L,l]ist all password titles you have saved, \n"
          "[G,g]enerate a new password, \n"
          "[A,a]dd existing password, \n"
          "[U,u]pdate existing password, \n"
          "[D,d]elete a password, \n"
          "[Q,q]uit.")

    while True:
        user_input = input("[r,l,g,a,u,d,q]: ")
        if user_input == "Q" or user_input == "q":
            print("Exiting..")
            break

        elif user_input == "R" or user_input == "r":
            title = input("Enter title of the password: ")
            pw = pw_handler.retrieve_password(title, master_password)
            print("Retrieved: " + pw)

        elif user_input == "L" or user_input == "l":
            utils.list_services()

        elif user_input == "G" or user_input == "g":
            title = input("Enter title for the password: ")
            pw_handler.generate_new_password(title, master_password)

        elif user_input == "A" or user_input == "a":
            title = input("Enter title for the password: ")
            if utils.file_exists(title+".pw"):
                print("Password for that title already exists")
            else:
                pw = getpass("Enter the password: ")
                check = getpass("Enter the password again: ")
                if pw != check:
                    print("The passwords do not match.")
                else:
                    pw_handler.add_password(title, pw, master_password)

        elif user_input == "U" or user_input == "u":
            title = input("Enter title for the password to be updated: ")
            pw_handler.update_password(title, master_password)

        elif user_input == "D" or user_input == "d":
            title = input("Enter title for the password to be deleted: ")
            pw_handler.delete_password(title)

        else:
            user_input = input("[r,l,g,a,u,d,q]: ")
