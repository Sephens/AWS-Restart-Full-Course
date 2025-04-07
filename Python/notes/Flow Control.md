# AWS re/Start - Flow Control in Python

Below is a comprehensive markdown document covering all content from the Flow Control module, with detailed explanations, practical examples, and additional insights.

---

## Module Overview
**Title**: Flow Control  
**Subtitle**: Python Fundamentals  
**Presenter**: [Name]  
**Date**: [Date]  
**Copyright**: © 2020, Amazon Web Services, Inc. or its affiliates. All rights reserved.

---

## Learning Objectives
By the end of this module, you will learn how to:
1. Understand and implement flow control in Python programs
2. Use conditional statements (`if`, `elif`, `else`) effectively
3. Implement different types of loops (`while`, `for`)
4. Work with Python data structures (lists, dictionaries)
5. Capture user input using the `input()` function

---

## Flow Control Fundamentals

### Definition
Flow control determines the **execution order** of statements in a program. Python provides several constructs to control program flow:

1. **Conditional Statements**: Make decisions
2. **Loops**: Repeat actions
3. **Functions**: Organize code into reusable blocks

**Key Concepts**:
- **Sequential Execution**: Default top-to-bottom execution
- **Branching**: Conditional execution paths
- **Iteration**: Repeated execution

---

## Conditional Statements

### Syntax Structure
```python
if condition1:
    # code block
elif condition2:
    # code block
else:
    # default code block
```

### Real-World Analogies
| Scenario | Python Equivalent |
|----------|-------------------|
| If store is open → enter | `if store_open: enter()` |
| If gas low → warn | `if fuel < 0.1: warn_driver()` |
| Age-based classification | `if age>18: "adult" elif age>13: "teen" else: "child"` |

### Practical Example
```python
# Age classification
age = 21
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# Output: Adult
```

**Key Notes**:
- Colon (`:`) terminates condition
- Indentation (4 spaces) defines code blocks
- Conditions evaluate to `True` or `False`

---

## Loops

### While Loops
**Purpose**: Repeat while condition is true  
**Risk**: Infinite loops if exit condition never met  

**Basic Structure**:
```python
while condition:
    # loop body
    # update condition
```

**Example**:
```python
# Countdown timer
count = 5
while count > 0:
    print(count)
    count -= 1  # Critical: Update condition
print("Liftoff!")
```

**Output**:
```
5
4
3
2
1
Liftoff!
```

### For Loops
**Purpose**: Iterate over sequences  
**Common Uses**: Lists, strings, ranges  

**Basic Structure**:
```python
for item in sequence:
    # process item
```

**Example**:
```python
# Print list elements
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}s")

# Output:
# I love apples
# I love bananas
# I love cherries
```

---

## Data Structures

### Lists
**Characteristics**:
- Ordered, mutable collections
- Can contain mixed data types
- Zero-indexed

**Operations**:
```python
# Create
numbers = [1, 2, 3]
mixed = [1, "two", 3.0]

# Access
first = numbers[0]  # 1

# Modify
numbers[1] = 99  # [1, 99, 3]

# Iterate
for num in numbers:
    print(num * 2)
```

### Dictionaries
**Characteristics**:
- Key-value pairs
- Unordered, mutable
- Keys must be immutable (strings, numbers)

**Operations**:
```python
# Create
person = {"name": "Alice", "age": 25}

# Access
name = person["name"]  # "Alice"

# Modify
person["age"] = 26

# Iterate
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## User Input

### `input()` Function
- Pauses execution to collect user input
- Always returns a string (convert if needed)
- Optional prompt parameter

**Examples**:
```python
# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Numeric input
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult status confirmed")
```

**Type Conversion Table**:
| Input | Conversion | Example |
|-------|------------|---------|
| "42" | `int()` | `int("42") → 42` |
| "3.14" | `float()` | `float("3.14") → 3.14` |
| "True" | `bool()` | `bool("True") → True` |

---

## Practical Demonstrations

### Conditional Statement Demo
```python
# bananas.py
bananas = 3

if bananas >= 5:
    print("Large bunch")
elif bananas >= 1:
    print("Small bunch")
else:
    print("No bananas")

# Output: Small bunch
```

### While Loop Demo
```python
# while.py
counter = 0
while counter < 3:
    print(f"Loop iteration {counter}")
    counter += 1

# Output:
# Loop iteration 0
# Loop iteration 1
# Loop iteration 2
```

### For Loop with Lists
```python
# lists.py
grades = [85, 92, 78]

for grade in grades:
    if grade >= 90:
        print(f"{grade}: A")
    elif grade >= 80:
        print(f"{grade}: B")

# Output:
# 85: B
# 92: A
# 78:
```

### Dictionary Demo
```python
# dictionary.py
student = {
    "name": "Kwaku",
    "courses": ["Math", "CS"],
    "gpa": 3.5
}

print(student["name"])  # Kwaku
for course in student["courses"]:
    print(course)

# Output:
# Kwaku
# Math
# CS
```

---

## Checkpoint Questions & Answers

1. **Name two kinds of loops in Python**  
   - `for` loops (iterate over sequences)  
   - `while` loops (repeat while condition is true)  

2. **How do you select a specific element from a list?**  
   Use index notation: `list[index]` (e.g., `my_list[0]` for first element)  

3. **What does `elif` stand for?**  
   "Else if" - provides alternative conditions after initial `if`  

---

## Key Takeaways

1. **Conditional Logic**:
   - `if`/`elif`/`else` enable decision-making
   - Conditions evaluate to boolean (`True`/`False`)
   - Example:
     ```python
     if score >= 90:
         grade = "A"
     elif score >= 80:
         grade = "B"
     ```

2. **Loop Structures**:
   | Loop Type | Use Case | Example |
   |-----------|----------|---------|
   | `while` | Unknown iterations | `while user_wants_to_continue:` |
   | `for` | Known sequences | `for item in collection:` |

3. **Data Structures**:
   - **Lists**: Ordered, mutable collections
     ```python
     colors = ["red", "green", "blue"]
     ```
   - **Dictionaries**: Key-value pairs
     ```python
     person = {"name": "Alice", "age": 30}
     ```

4. **User Interaction**:
   - `input()` captures user data
   - Always returns string (requires conversion)
   - Example:
     ```python
     age = int(input("Enter age: "))
     ```

---

This enhanced guide combines original content with:
- Expanded code examples
- Real-world analogies
- Practical demonstrations
- Type conversion guidance
- Structured comparison tables

The additional explanations and examples provide concrete context for applying flow control concepts in Python programming.