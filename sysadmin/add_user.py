import os

def new_user():
    confirm = "N"
    # continues while the user does not enter Y
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser " + username)

new_user()