## Working with a while loop
A while loop makes a section of code repeat until a certain condition is met. 
In this exercise, you will create a Python script that asks the user to correctly guess a number.

Use the print() function to inform the user about your game:

```
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

```

Next, enter a statement that will generate a random number between 1 and 10 by using the randint() function of the random module.
Remember to import random module at the top of the file

```
import random

```

```
number = random.randint(1,10)

```
Track whether the user guessed your number by creating a variable called isGuessRight:

```
isGuessRight = False

```

To handle the game logic, create a while loop:

```
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


```
**Note**: The while loop will repeat the code inside the loop until the number is guessed correctly, which is represented by the condition isGuessRight != True in the code. 

---

## Working with for loop

