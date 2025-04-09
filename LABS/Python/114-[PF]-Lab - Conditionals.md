# Working with Conditionals - Lab Explanation

## Lab Overview
This lab introduces Python's conditional statements which allow programs to make decisions based on different conditions. You'll learn to control program flow using:
- `if` statements
- `else` statements
- `elif` (else-if) statements

## Exercise 1: Basic if Statement

### Getting User Input
```python
userReply = input("Do you need to ship a package? (Enter yes or no) ")
```
- `input()` function collects user input
- The prompt message guides the user
- Input is stored in `userReply` variable

### Making a Simple Decision
```python
if userReply == "yes":
    print("We can help you ship that package!")
```
**Key Components:**
- `if` keyword starts the conditional
- `==` comparison operator checks equality
- Colon `:` ends the condition
- Indented block executes if condition is True

**Behavior:**
- If user enters "yes": Prints shipping message
- If user enters anything else: Does nothing

**Important Notes:**
- Python uses indentation (not brackets) to define code blocks
- `==` checks value equality (different from `=` which assigns values)
- Condition is case-sensitive ("Yes" ≠ "yes")

## Exercise 2: Adding an else Clause

### Handling the Negative Case
```python
else:
    print("Please come back when you need to ship a package. Thank you.")
```
**Improvements:**
- Catches all cases where initial condition is False
- Provides polite response instead of silent exit
- Maintains indentation for the code block

**Full Example Now:**
```python
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
```

**Testing Scenarios:**
1. Input "yes" → "We can help you ship that package!"
2. Input "no" → "Please come back when you need..."
3. Input anything else → Same else response

## Exercise 3: Using elif for Multiple Conditions

### Expanded Service Options
```python
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
```

**Key Features:**
1. **Multiple Conditions:** Handles 3 specific options plus catch-all
2. **Nested Input:** For copies, gets additional information
3. **String Formatting:** Uses `.format()` to insert variable
4. **Order Matters:** Evaluates top-to-bottom

**elif Characteristics:**
- Short for "else if"
- Must come after initial `if`
- Can have multiple `elif` clauses
- Only one block executes (first true condition found)

**Testing Scenarios:**
1. "stamps" → Shows stamp designs
2. "envelope" → Shows envelope sizes
3. "copy" → Asks for number, then shows copies
4. Anything else → Thanks user

## Deep Dive: Important Concepts

### Comparison Operators
| Operator | Meaning                  | Example          |
|----------|--------------------------|------------------|
| `==`     | Equal to                 | `if x == 5:`     |
| `!=`     | Not equal to             | `if x != 5:`     |
| `>`      | Greater than             | `if x > 5:`      |
| `<`      | Less than                | `if x < 5:`      |
| `>=`     | Greater than or equal to | `if x >= 5:`     |
| `<=`     | Less than or equal to    | `if x <= 5:`     |

### Truth Value Testing
Python evaluates conditions as Boolean (True/False):
- Empty sequences (strings, lists) are False
- Zero is False
- None is False
- Everything else is generally True

### Input Handling Best Practices
1. **Case Sensitivity:** Consider using `.lower()`:
   ```python
   if userReply.lower() == "yes":
   ```
2. **Input Validation:** Check for unexpected values
3. **Type Conversion:** For numeric input:
   ```python
   copies = int(input("How many copies?"))
   ```

## Practical Applications

1. **Menu Systems:** Drive program navigation
2. **Data Validation:** Ensure proper input formats
3. **Business Rules:** Implement decision logic
4. **Game Development:** Control game flow

## Enhanced Example with Error Handling

```python
while True:
    userReply = input("Would you like to buy stamps, envelope, or make copies? ")
    
    if userReply.lower() == "stamps":
        print("Stamp designs available...")
        break
    elif userReply.lower() == "envelope":
        print("Envelope sizes available...")
        break
    elif userReply.lower() == "copies":
        try:
            copies = int(input("How many copies? "))
            print(f"Preparing {copies} copies...")
            break
        except ValueError:
            print("Please enter a valid number")
    else:
        print("Invalid option. Please try again.")
```

**Improvements:**
- Case-insensitive comparison
- Numeric input validation
- Loop until valid input
- F-strings for formatting

## Common Questions

**Q: How many elif statements can I use?**
A: As many as needed, but consider a dictionary or match-case (Python 3.10+) for many options.

**Q: Can I nest if statements?**
A: Yes, but deep nesting can make code hard to read:
```python
if condition1:
    if condition2:
        # Nested logic
```

**Q: What's the difference between elif and multiple ifs?**
A: `elif` is part of a single decision structure (only one executes), while multiple `if` statements are evaluated independently.

## Conclusion

This lab covered essential conditional programming concepts:
1. Basic `if`/`else` decision making
2. Handling multiple conditions with `elif`
3. Proper Python indentation and syntax
4. Practical input/output patterns

These fundamentals enable you to create programs that can make decisions and respond differently to various inputs, which is crucial for building interactive applications.