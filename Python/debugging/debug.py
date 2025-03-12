import logging # import the library to be able perform logging/log monitoring
logging.basicConfig(filename="debugging/app.log", level=logging.DEBUG)

var  = "Double value"
num = 10
sumValue = var + "4"

def do_something():
    if len(sumValue) >= 4:
        print("Bad indent")


# Debugging can be done statically or dynamically
# Dynamic analysis uses assertion statements during runtime to raise errors when conditions certain
# conditions occur.

logging.debug("This is a debug message")

# an example of assertion statement
def log_age():
    age = int(input("How old are you: "))
    assert age >= 1, "Age must be positive"
    print(f'You are {age} years old')

log_age()