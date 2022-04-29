from getpass import getpass
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
          "[Q,q]uit.")

    while True:
        user_input = input("[r,l,g,a,q]: ")
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
            service_name = input("Enter title for the password: ")
            pw_handler.generate_new_password(service_name, master_password)

        elif user_input == "A" or user_input == "a":
            print("Add password")

        else:
            user_input = input("[r,l,g,a,q]: ")
