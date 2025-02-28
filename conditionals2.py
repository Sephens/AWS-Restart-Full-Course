# As the user to input his or her age

age =  int(input("Please enter your Age: "))

if age > 18:
    print("You are an adult")
elif age >= 13 < 18:
    print("You are a teen")
else:
    print("You are a child")

hasBadge = False

ask = input("Do you have a badge? (Enter Y/N) ")

if ask == "Y":
    hasBadge = True
    print("You can enter the building")
elif ask == "N":
    hasBadge = False
    print("The door is locked")