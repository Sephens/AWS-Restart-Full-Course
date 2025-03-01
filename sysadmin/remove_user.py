import os

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Which user would you like to remove? ")
        print("Are you sure you want to remove '" + username + "'? (Y/N)" )
        confirm = input().upper()

    os.system("sudo userdel -r " + username)

remove_user()