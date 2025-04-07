# Python Basics - Comprehensive Guide

## Table of Contents
- [Python Basics - Comprehensive Guide](#python-basics---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Python Basics](#introduction-to-python-basics)
  - [What You Will Learn](#what-you-will-learn)
  - [Installing Python](#installing-python)
    - [Installation on Linux (CentOS)](#installation-on-linux-centos)
  - [Python Syntax Fundamentals](#python-syntax-fundamentals)
  - [Identifiers and Naming Conventions](#identifiers-and-naming-conventions)
    - [Rules:](#rules)
  - [Python Files and Execution](#python-files-and-execution)
    - [Creating and Running a Script:](#creating-and-running-a-script)
  - [Functions in Python](#functions-in-python)
    - [Basic Function Structure:](#basic-function-structure)
  - [Working with Vim Editor](#working-with-vim-editor)
    - [Basic Vim Commands:](#basic-vim-commands)
  - [Comments in Python](#comments-in-python)
    - [Comment Types:](#comment-types)
  - [Python Data Types](#python-data-types)
    - [Basic Types:](#basic-types)
    - [Type Conversion:](#type-conversion)
    - [Mutable vs Immutable:](#mutable-vs-immutable)
  - [Variables in Python](#variables-in-python)
    - [Variable Assignment:](#variable-assignment)
    - [Naming Conventions:](#naming-conventions)
  - [Python Operators](#python-operators)
    - [Operator Categories:](#operator-categories)
    - [Operator Precedence:](#operator-precedence)
  - [Statements and Program Flow](#statements-and-program-flow)
    - [Common Statements:](#common-statements)
  - [Exception Handling](#exception-handling)
    - [Common Exceptions:](#common-exceptions)
    - [Handling Exceptions:](#handling-exceptions)
  - [Checkpoint Questions and Answers](#checkpoint-questions-and-answers)
  - [Key Takeaways](#key-takeaways)
  - [Additional Notes and Examples](#additional-notes-and-examples)
    - [Comprehensive Variable Example:](#comprehensive-variable-example)
    - [Advanced String Operations:](#advanced-string-operations)
    - [Practical Math Operations:](#practical-math-operations)
    - [Comprehensive Function Example:](#comprehensive-function-example)

---

## Introduction to Python Basics
Python is a high-level, interpreted programming language known for its simplicity and readability. This guide covers fundamental Python concepts from installation to basic programming constructs.

**Python Characteristics:**
- Easy-to-learn syntax
- Cross-platform compatibility
- Extensive standard library
- Supports multiple programming paradigms

---

## What You Will Learn
By the end of this guide, you'll be able to:
- Install Python on different operating systems
- Understand Python syntax rules
- Work with variables and data types
- Use functions and handle exceptions
- Write and execute Python scripts
- Apply basic operators and statements

---

## Installing Python

### Installation on Linux (CentOS)
```bash
# Check existing Python version
python --version

# Install dependencies
yum install gcc openssl-devel bzip2-devel libffi-devel

# Download Python 3.7.2
cd /usr/src
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz

# Extract and install
tar xzf Python-3.7.2.tgz
cd Python-3.7.2
./configure --enable-optimizations
make altinstall

# Verify installation
python3.7 -V
```

**Note:** Similar installation processes exist for Windows (installer) and macOS (Homebrew).

---

## Python Syntax Fundamentals
Python has distinctive syntax rules:

1. **Indentation**: Uses whitespace (4 spaces recommended) for code blocks
   ```python
   if True:
       print("This is indented")
   ```

2. **Case Sensitivity**: `variable` and `Variable` are different

3. **Line Structure**: Generally one statement per line

4. **Punctuation**: 
   - Colon (`:`) starts code blocks
   - Parentheses (`()`) for function calls
   - Square brackets (`[]`) for lists
   - Curly braces (`{}`) for dictionaries

---

## Identifiers and Naming Conventions
Identifiers are names given to variables, functions, classes, etc.

### Rules:
1. Can contain letters, numbers, underscores
2. Cannot start with a number
3. Cannot be Python keywords (`if`, `while`, etc.)
4. Case sensitive
5. No special characters (`@`, `#`, `$`, etc.)

**Examples:**
```python
valid_name = "John"  # Valid
2invalid = 10       # Invalid (starts with number)
class = "Math"      # Invalid (keyword)
```

---

## Python Files and Execution
Python scripts use `.py` extension and require a Python interpreter to run.

### Creating and Running a Script:
1. Create file `script.py`
2. Add code: `print("Hello Python")`
3. Execute: `python3 script.py`

**File Naming Best Practices:**
- Use lowercase with underscores (`my_script.py`)
- Avoid spaces or special characters
- Make names descriptive

---

## Functions in Python
Functions are reusable blocks of code that perform specific tasks.

### Basic Function Structure:
```python
def function_name(parameters):
    """Docstring (optional)"""
    # Function body
    return value
```

**Example:**
```python
def greet(name):
    """Returns a greeting message"""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

**Built-in Functions:**
- `print()`: Output to console
- `len()`: Get length of object
- `type()`: Check object type

---

## Working with Vim Editor
Vim is a powerful text editor for coding.

### Basic Vim Commands:
| Command | Action |
|---------|--------|
| `vim filename` | Open/create file |
| `i` | Enter insert mode |
| `ESC` | Return to normal mode |
| `:w` | Save file |
| `:q` | Quit Vim |
| `:wq` | Save and quit |

**Example Workflow:**
1. `vim hello.py`
2. Press `i`
3. Type `print("Hello")`
4. Press `ESC`
5. Type `:wq`
6. Run `python3 hello.py`

---

## Comments in Python
Comments explain code and are ignored by the interpreter.

### Comment Types:
1. Single-line: `# This is a comment`
2. Inline: `x = 5  # Initialize counter`
3. Multi-line (using triple quotes):
   ```python
   """
   This is a 
   multi-line comment
   """
   ```

**Best Practices:**
- Explain why, not what
- Keep comments up-to-date
- Avoid obvious comments

---

## Python Data Types
Python has several built-in data types:

### Basic Types:
| Type | Example | Description |
|------|---------|-------------|
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `bool` | `True` | Boolean values |
| `str` | `"text"` | Text data |

### Type Conversion:
```python
x = 10
float_x = float(x)  # 10.0
str_x = str(x)      # "10"
int("42")           # 42
```

### Mutable vs Immutable:
- **Mutable**: Can change after creation (lists, dicts)
- **Immutable**: Cannot change (ints, strings, tuples)

---

## Variables in Python
Variables store data values in memory.

### Variable Assignment:
```python
x = 10              # Integer
name = "Alice"      # String
is_active = True    # Boolean
```

### Naming Conventions:
- Use descriptive names
- Snake_case for variables
- UPPER_CASE for constants
- Avoid single letters (except in loops)

**Example:**
```python
user_count = 42
MAX_USERS = 100

for i in range(5):
    print(i)
```

---

## Python Operators
Operators perform operations on variables and values.

### Operator Categories:
| Type | Operators | Example |
|------|-----------|---------|
| Arithmetic | `+`, `-`, `*`, `/`, `%` | `5 + 3` |
| Comparison | `==`, `!=`, `>`, `<` | `x == y` |
| Assignment | `=`, `+=`, `-=` | `x += 5` |
| Logical | `and`, `or`, `not` | `x > 0 and x < 10` |
| Membership | `in`, `not in` | `"a" in "apple"` |

### Operator Precedence:
1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication `*`, Division `/`
4. Addition `+`, Subtraction `-`
5. Comparison operators
6. Logical operators

---

## Statements and Program Flow
Statements are individual instructions in Python.

### Common Statements:
1. **Assignment**: `x = 5`
2. **Conditional**:
   ```python
   if x > 0:
       print("Positive")
   elif x < 0:
       print("Negative")
   else:
       print("Zero")
   ```
3. **Loop**:
   ```python
   for i in range(3):
       print(i)
   
   while x > 0:
       print(x)
       x -= 1
   ```

---

## Exception Handling
Exceptions are errors detected during execution.

### Common Exceptions:
- `NameError`: Undefined variable
- `TypeError`: Wrong type operation
- `ValueError`: Invalid value
- `ZeroDivisionError`: Division by zero

### Handling Exceptions:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error occurred: {e}")
```

---

## Checkpoint Questions and Answers

1. **Does Python limit you from using specific characters when you declare a variable?**
   - Yes, you cannot use symbols like `!`, `@`, `#`, `$`, `%` in variable names. Only letters, numbers, and underscores are allowed, and names cannot start with numbers.

2. **How are functions called in Python?**
   - Functions are called by their name followed by parentheses, which may contain arguments: `function_name(arguments)`

3. **Which data type do you use to store the value 1.7—an integer or a float?**
   - A float, since it contains a decimal point. Integers are for whole numbers only.

4. **What is the += operator used for?**
   - The `+=` operator is a compound assignment operator that adds the right operand to the left operand and assigns the result to the left operand. Example: `x += 3` is equivalent to `x = x + 3`

---

## Key Takeaways
1. **Installation**: Python runs on all major OSes and is easy to install
2. **Syntax**: Python uses indentation for code blocks and is case-sensitive
3. **Variables**: Store data with meaningful names following naming rules
4. **Data Types**: Understand different types and their appropriate uses
5. **Operators**: Perform calculations and comparisons efficiently
6. **Functions**: Create reusable code blocks for better organization
7. **Error Handling**: Manage exceptions gracefully for robust programs

---

## Additional Notes and Examples

### Comprehensive Variable Example:
```python
# Valid variable assignments
user_name = "Alice"
user_age = 30
is_active = True
average_score = 92.5

# Multiple assignment
x, y, z = 1, 2, 3

# Type checking
print(type(user_name))  # <class 'str'>
print(type(user_age))   # <class 'int'>

# Type conversion
age_string = str(user_age)  # "30"
```

### Advanced String Operations:
```python
# String concatenation
first = "Hello"
second = "World"
message = first + " " + second  # "Hello World"

# String methods
text = " Python is awesome! "
print(text.strip())          # "Python is awesome!"
print(text.lower())          # " python is awesome! "
print(text.upper())          # " PYTHON IS AWESOME! "
print(text.replace(" ", "_")) # "_Python_is_awesome!_"
print("awesome" in text)     # True
```

### Practical Math Operations:
```python
# Basic arithmetic
sum = 5 + 3       # 8
difference = 5 - 3 # 2
product = 5 * 3    # 15
quotient = 5 / 3   # 1.666...
remainder = 5 % 3  # 2
power = 5 ** 3     # 125
floor_div = 5 // 3 # 1

# Compound assignment
counter = 0
counter += 1  # Equivalent to counter = counter + 1

# Operator precedence
result = 5 + 3 * 2  # 11 (not 16)
```

### Comprehensive Function Example:
```python
def calculate_tax(income, deductions=0, tax_rate=0.2):
    """
    Calculate tax based on income and deductions
    
    Args:
        income (float): Total income
        deductions (float): Tax deductions
        tax_rate (float): Tax rate (default 20%)
    
    Returns:
        float: Calculated tax amount
    """
    taxable_income = income - deductions
    tax = taxable_income * tax_rate
    return max(0, tax)  # Ensure non-negative result

# Function usage
tax = calculate_tax(50000, 10000)
print(f"Tax owed: ${tax:,.2f}")
```

This comprehensive guide covers all Python basics from the provided materials, with expanded explanations, practical examples, and best practices. The markdown format ensures clear organization and easy reference.