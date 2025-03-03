import json

filename = "file-handling/users.json"
data = {}

try:
    with open(filename, 'r') as f:
        data = json.load(f)
        # print(data)

except IOError:
    print("error! Cannot read the file...")


def check_user():
    name = input("Enter the name of the user to check:  ")
    if name in data:
        print("User is in the database")
    else:
        print("The user entered is not in the database")


def add_user():
    name = input("Enter the user name to add: ")
    if name in data:
        print("The user already exists")
    else:
        num = input("Enter Phone: ")
        user = {name : num}
        data.update(user)
        with open(filename, 'w') as fi:
            json.dump(data, fi)
        
        print("User added successfully")

def remove_user():
    name = input("Enter the name of the user to remove: ")
    if name not in data:
        print("The user does not exist")
    else:
        keyToRemove = name
        if keyToRemove in data:
            del data[keyToRemove]
        with open(filename, 'w') as fil:
            json.dump(data, fil)
        print("User removed successfully")

def edit_user():
    name = input("Enter the name of the user you want to edit: ")
    if name not in data:
        print("The user does not exist")
    else:
        phoneOrName = input("Do you want to edit name or phone? (Name/Phone): ")
        if phoneOrName == "Name":
            oldName = name
            newName = input("Enter new Name: ")
            data[newName] = data.pop(oldName)

            with open(filename, 'w') as fin:
                json.dump(data, fin)
            print("User name editted successfully!")
        elif phoneOrName == "Phone":
            keyToEdit = name
            newPhone = input("Enter new Phone Number: ")
            data[keyToEdit] = newPhone
            with open(filename, 'w') as fin:
                json.dump(data, fin)
            print("Phone number editted successfully")
        else:
            print("Invalid input!")


inp = input("Do you want to add, check, edit, or remove a user? (Add, Check, Remove): ")

if inp == "Add":
    add_user()
elif inp == "Check":
    check_user()
elif inp == "Remove":
    remove_user()
elif inp == "Edit":
    edit_user()
else:
    print("Invalid Input!!")





