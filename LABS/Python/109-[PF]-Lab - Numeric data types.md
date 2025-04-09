
# Python Lab: Working with Numeric Data Types

## Introduction
This lab explores Python's numeric data types (`int`, `float`, `complex`) and Boolean (`bool`) values. You'll practice working with these types in both interactive Python shell and script modes, while learning essential programming concepts.

## Lab Components
The lab environment provides:

1. **AWS Cloud9 IDE**
   - Pre-configured Python 3.6+ environment
   - Integrated terminal and code editor

2. **Key Python Features**:
   - Interactive shell for immediate feedback
   - Script execution capability
   - Built-in functions for type checking

## Task 1: Using the Python Shell

### Step 1: Launching the Python Shell
1. Open the terminal in Cloud9
2. Enter:
```bash
python3
```

**Expected Output**:
```
Python 3.6.12 (default, Aug 31 2020, 18:56:18)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Step 2: Performing Basic Arithmetic
Try these operations in the shell:

| Operation | Command      | Output | Notes                          |
|-----------|--------------|--------|--------------------------------|
| Addition  | `2 + 2`      | `4`    | Uses `+` operator             |
| Subtraction | `4 - 2`    | `2`    | Uses `-` operator             |
| Multiplication | `2 * 3` | `6`    | Uses `*` operator             |
| Division  | `4 / 2`      | `2.0`  | Returns float even if whole number |

**Note**: To exit the shell, type:
```python
quit()
```

## Task 2: Working with Numeric Data Types

### Step 1: Create a Python Script
1. Create new file `numeric_types.py`
2. Add initial code:
```python
print("Python has three numeric types: int, float, and complex")
```

### Step 2: Using Integer Type (`int`)
Add to your script:
```python
myValue = 1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of type " + str(type(myValue)))
```

**Expected Output**:
```
1
<class 'int'>
1 is of type <class 'int'>
```

### Step 3: Using Float Type (`float`)
Add to your script:
```python
myValue = 3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of type " + str(type(myValue)))
```

**Expected Output**:
```
3.14
<class 'float'>
3.14 is of type <class 'float'>
```

### Step 4: Using Complex Type (`complex`)
Add to your script:
```python
myValue = 5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of type " + str(type(myValue)))
```

**Expected Output**:
```
5j
<class 'complex'>
5j is of type <class 'complex'>
```

### Step 5: Using Boolean Type (`bool`)
Add to your script:
```python
myValue = True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of type " + str(type(myValue)))

myValue = False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of type " + str(type(myValue)))
```

**Expected Output**:
```
True
<class 'bool'>
True is of type <class 'bool'>
False
<class 'bool'>
False is of type <class 'bool'>
```

## Task 3: Practical Exercises

### Exercise 1: Type Conversion
```python
# Convert between types
num_int = 10
num_float = float(num_int)
num_str = str(num_int)

print(f"Integer: {num_int}, Float: {num_float}, String: {num_str}")
```

### Exercise 2: Arithmetic Operations
```python
# Mixed-type arithmetic
result = 3 + 4.5
print(result)  # What type is this?
print(type(result))
```

### Exercise 3: Boolean Evaluation
```python
# Boolean from comparison
is_greater = 5 > 3
print(is_greater)
print(type(is_greater))
```

## Common Questions and Troubleshooting

**Q: Why does division return a float?**
A: Python 3 always returns float from division. Use `//` for integer division:
```python
print(4 // 2)  # Returns 2 (int)
```

**Q: How to format float precision?**
A: Use f-strings or format():
```python
pi = 3.14159265
print(f"{pi:.2f}")  # Prints 3.14
```

**Q: What's the difference between 5 and 5.0?**
A: The first is `int`, second is `float`. They're stored differently in memory.

**Q: Why use complex numbers?**
A: Essential for advanced math, engineering, and physics calculations.

## Advanced Concepts

### Type Checking
```python
import numbers

x = 5
print(isinstance(x, numbers.Number))  # True for all numeric types
```

### Numeric Limits
```python
import sys
print(sys.maxsize)  # Maximum integer size
```

### Math Module
```python
import math
print(math.sqrt(4))  # Square root function
```

## Best Practices

1. **Choose appropriate types**:
   - Use `int` for counting/whole numbers
   - Use `float` for measurements/continuous values
   - Use `complex` for specialized math

2. **Be aware of type conversion**:
   - Operations between types follow coercion rules
   - Explicit conversion is clearer than implicit

3. **Use parentheses** for complex expressions:
```python
result = (2 + 3) * 4  # Clear precedence
```

## Conclusion

This lab covered:
1. Python's numeric data types (`int`, `float`, `complex`)
2. Boolean values and their numeric nature
3. Type conversion and checking
4. Best practices for numeric operations

These fundamentals are essential for all Python programming, especially in data analysis and scientific computing.
