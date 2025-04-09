# Working with Loops - Comprehensive Lab Guide

## Lab Overview
This lab introduces two fundamental loop structures in Python:
1. **While loops** - Repeat code while a condition is true
2. **For loops** - Iterate through sequences or ranges

## Exercise 1: While Loop (Number Guessing Game)

### Initial Setup
```python
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
```

**Key Points:**
- Uses `print()` to display game instructions
- Clear communication of game rules to user

### Importing Required Modules
```python
import random
```
- `random` module provides random number generation
- Always place imports at the top of your script

### Game Initialization
```python
number = random.randint(1,10)
isGuessRight = False
```
- `randint(1,10)` generates random integer between 1-10
- Boolean flag `isGuessRight` controls loop execution

### Core Game Loop
```python
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
```

**Detailed Breakdown:**
1. **While Condition**: Loop continues until correct guess
2. **User Input**: `input()` collects guess as string
3. **Type Conversion**: `int(guess)` converts to integer
4. **Comparison**: Checks if guess matches random number
5. **Feedback**: Provides success/failure messages
6. **Loop Control**: Sets flag to exit on correct guess

**Pseudocode Translation:**
```
WHILE guess is not correct:
    GET user guess
    IF guess equals secret number:
        PRINT success message
        SET flag to exit loop
    ELSE:
        PRINT try again message
```

### Enhanced Version (With Improvements)
```python
import random

print("Welcome to Guess the Number!")
print("Guess a number between 1 and 10. You have 5 attempts.")

number = random.randint(1, 10)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}/{max_attempts}. Your guess: ")
    
    try:
        guess = int(guess)
        if guess == number:
            print(f"Congratulations! You guessed {number} correctly!")
            break
        elif guess < number:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")
        attempts += 1
    except ValueError:
        print("Please enter a valid number!")

if attempts == max_attempts:
    print(f"Game over! The number was {number}.")
```

**Improvements:**
- Limited attempts
- Input validation
- Hints (too high/low)
- Progress tracking
- Cleaner output formatting

## Exercise 2: For Loop (Counting)

### Basic Counting Example
```python
print("Count to 10!")

for x in range(0, 11):
    print(x)
```

**Key Components:**
1. `range(0, 11)` generates numbers 0-10
   - Start (inclusive): 0
   - Stop (exclusive): 11
   - Step (default): 1
2. `x` is the loop variable (updates each iteration)
3. Indented block executes for each value

### Understanding Range
```python
range(stop)             # 0 to stop-1
range(start, stop)      # start to stop-1  
range(start, stop, step) # start to stop-1 by step
```

### Practical For Loop Applications

**1. Iterating Through Collections**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}!")
```

**2. Custom Step Values**
```python
for even in range(0, 11, 2):
    print(even)  # Prints 0, 2, 4, 6, 8, 10
```

**3. Enumerated Loops**
```python
for index, fruit in enumerate(fruits):
    print(f"Fruit #{index + 1}: {fruit}")
```

**4. Dictionary Iteration**
```python
inventory = {"apples": 5, "oranges": 3}
for item, quantity in inventory.items():
    print(f"We have {quantity} {item}")
```

## Loop Control Statements

1. **break**: Exit loop immediately
   ```python
   for num in range(100):
       if num == 5:
           break
       print(num)
   ```

2. **continue**: Skip to next iteration
   ```python
   for num in range(10):
       if num % 2 == 0:
           continue
       print(num)  # Prints only odds
   ```

3. **else**: Execute after normal loop completion
   ```python
   for n in range(2, 10):
       for x in range(2, n):
           if n % x == 0:
               break
       else:
           print(f"{n} is prime")
   ```

## Common Loop Patterns

**1. Accumulator Pattern**
```python
total = 0
for number in [1, 2, 3, 4]:
    total += number
print(total)  # Sums to 10
```

**2. Search Pattern**
```python
found = False
for item in inventory:
    if item == "apple":
        found = True
        break
```

**3. Nested Loops**
```python
for x in range(3):      # Outer loop
    for y in range(2):  # Inner loop
        print(f"({x},{y})")
```

## Performance Considerations

1. **Preallocate lists** when building large collections
   ```python
   results = [None] * 1000  # Better than appending in loop
   ```

2. **Use built-in functions** like `map()`, `filter()` when appropriate

3. **Avoid unnecessary computations** inside loops

4. **Consider list comprehensions** for simple transformations:
   ```python
   squares = [x**2 for x in range(10)]
   ```

## Debugging Tips

1. **Add print statements** to check loop variables
   ```python
   for i in range(5):
       print(f"Loop iteration {i}")  # Debug output
   ```

2. **Use a debugger** to step through loop execution

3. **Check edge cases** (empty sequences, boundary values)

4. **Validate loop conditions** to prevent infinite loops

## Real-World Applications

1. **Data Processing**: Batch operations on datasets
2. **User Interfaces**: Event loops in GUI applications  
3. **Games**: Main game loops
4. **Web Servers**: Handling multiple requests
5. **Automation**: Repetitive task execution

## Final Thoughts

Mastering loops is essential for:
- Writing efficient, non-repetitive code
- Processing collections of data
- Implementing complex algorithms
- Creating interactive programs

Practice variations of both while and for loops to develop intuition for when each is most appropriate. Remember that many problems can be solved with either type, but one is often more elegant than the other for a given situation.