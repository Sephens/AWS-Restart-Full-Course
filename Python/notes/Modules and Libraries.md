# Python Modules and Libraries - Comprehensive Guide

## Table of Contents
- [Python Modules and Libraries - Comprehensive Guide](#python-modules-and-libraries---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Modules and Libraries](#introduction-to-modules-and-libraries)
  - [What You Will Learn](#what-you-will-learn)
  - [Understanding Modules and Libraries](#understanding-modules-and-libraries)
    - [Hierarchy of Code Organization:](#hierarchy-of-code-organization)
    - [Types of Modules:](#types-of-modules)
  - [Python Standard Library](#python-standard-library)
  - [Importing Modules](#importing-modules)
    - [Import Methods:](#import-methods)
  - [Creating Your Own Modules](#creating-your-own-modules)
    - [Steps to Create a Module:](#steps-to-create-a-module)
  - [Working with File Handlers](#working-with-file-handlers)
    - [File Operations:](#file-operations)
    - [File Modes:](#file-modes)
  - [Exception Handling](#exception-handling)
    - [Basic Structure:](#basic-structure)
  - [OS Module](#os-module)
    - [Common OS Operations:](#common-os-operations)
  - [Working with JSON](#working-with-json)
    - [JSON Operations:](#json-operations)
  - [Package Management with pip](#package-management-with-pip)
    - [Common pip Commands:](#common-pip-commands)
  - [Checkpoint Questions and Answers](#checkpoint-questions-and-answers)
  - [Key Takeaways](#key-takeaways)
  - [Additional Notes and Examples](#additional-notes-and-examples)
    - [Advanced Module Techniques](#advanced-module-techniques)
    - [File Handling Best Practices](#file-handling-best-practices)
    - [Extended JSON Example](#extended-json-example)
    - [Comprehensive Exception Handling Example](#comprehensive-exception-handling-example)

---

## Introduction to Modules and Libraries
Modules and libraries are fundamental concepts in Python that enable code organization, reusability, and sharing of functionality across different programs.

**Why use modules and libraries?**
- Promote code reuse (Don't Repeat Yourself principle)
- Better organization of related functionality
- Easier maintenance and updates
- Access to vast ecosystem of pre-built solutions
- Standardization of common operations

---

## What You Will Learn
By the end of this guide, you'll be able to:
- Explain the purpose and structure of Python modules
- Navigate and utilize the Python Standard Library
- Import and use both built-in and third-party modules
- Work with files using file handlers
- Implement exception handling in your code
- Process JSON data effectively
- Manage packages using pip

---

## Understanding Modules and Libraries

### Hierarchy of Code Organization:
1. **Functions**: Blocks of code that perform specific tasks
2. **Modules**: Python files containing related functions and variables
3. **Libraries**: Collections of related modules packaged together

**Example Structure:**
```
my_library/           # Library
├── math_utils.py     # Module (contains calculate_area, calculate_volume)
├── string_utils.py   # Module (contains format_name, clean_string)
└── io_utils.py       # Module (contains read_file, write_file)
```

### Types of Modules:
1. **Standard Library Modules**: Pre-installed with Python (math, os, sys)
2. **Third-party Modules**: Installed via pip (requests, numpy)
3. **Custom Modules**: Created by developers for specific needs

---

## Python Standard Library
The Python Standard Library is a collection of modules that come pre-installed with Python, providing solutions for common programming tasks.

**Key Standard Library Modules:**
| Module | Purpose |
|--------|---------|
| `math` | Mathematical operations |
| `os` | Operating system interactions |
| `sys` | System-specific parameters |
| `json` | JSON data processing |
| `datetime` | Date and time operations |
| `random` | Random number generation |
| `re` | Regular expressions |

**Practical Example:**
```python
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793
```

---

## Importing Modules
Python provides several ways to import modules and their contents.

### Import Methods:
1. **Basic Import**:
   ```python
   import math
   print(math.sqrt(9))
   ```

2. **Import with Alias**:
   ```python
   import math as m
   print(m.sqrt(9))
   ```

3. **Import Specific Items**:
   ```python
   from math import sqrt, pi
   print(sqrt(9))
   print(pi)
   ```

4. **Import All Items** (Not Recommended):
   ```python
   from math import *
   print(sqrt(9))
   ```

**Best Practice**: Prefer explicit imports (methods 1-3) to avoid naming conflicts.

---

## Creating Your Own Modules
Creating custom modules helps organize your code into logical units.

### Steps to Create a Module:
1. Create a Python file (e.g., `mymodule.py`)
2. Add functions/variables to the file
3. Import and use in other files

**Example:**
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def calculate_area(length, width):
    return length * width
```

```python
# main.py
from mymodule import greet, calculate_area

print(greet("Alice"))          # Hello, Alice!
print(calculate_area(5, 3))    # 15
```

---

## Working with File Handlers
File handlers allow Python programs to interact with files on the filesystem.

### File Operations:
1. **Opening Files**:
   ```python
   file = open('example.txt', 'r')  # Read mode
   ```

2. **Reading Files**:
   ```python
   content = file.read()
   ```

3. **Writing Files**:
   ```python
   file = open('example.txt', 'w')  # Write mode
   file.write("New content")
   ```

4. **Closing Files**:
   ```python
   file.close()
   ```

**Best Practice**: Use `with` statement for automatic resource management:
```python
with open('example.txt', 'r') as file:
    content = file.read()
# File automatically closed after block
```

### File Modes:
| Mode | Description |
|------|-------------|
| `r` | Read (default) |
| `w` | Write (truncates) |
| `a` | Append |
| `r+` | Read and write |
| `b` | Binary mode |

---

## Exception Handling
Exception handling allows programs to gracefully handle errors rather than crashing.

### Basic Structure:
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero!")
except Exception as e:
    # Handle any other exception
    print(f"An error occurred: {e}")
else:
    # Runs if no exceptions
    print("Operation successful")
finally:
    # Always runs
    print("Execution complete")
```

**Common Exception Types**:
- `ZeroDivisionError`: Division by zero
- `FileNotFoundError`: Missing file
- `ValueError`: Invalid value
- `TypeError`: Invalid operation for type
- `KeyError`: Missing dictionary key

**Practical Example**:
```python
try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found, using default data")
    data = {}
except json.JSONDecodeError:
    print("Invalid JSON format")
    data = {}
```

---

## OS Module
The `os` module provides a way to interact with the operating system.

### Common OS Operations:
1. **File Operations**:
   ```python
   import os
   os.rename('old.txt', 'new.txt')
   os.remove('file.txt')
   ```

2. **Directory Operations**:
   ```python
   os.mkdir('new_folder')
   os.rmdir('empty_folder')
   print(os.listdir('.'))  # List directory contents
   ```

3. **System Information**:
   ```python
   print(os.getlogin())    # Current user
   print(os.getcwd())      # Current working directory
   print(os.uname())       # System information (Linux)
   ```

4. **Running System Commands**:
   ```python
   os.system('ls -l')      # Execute shell command
   ```

**Practical Example**:
```python
import os

# Create backup directory if it doesn't exist
if not os.path.exists('backups'):
    os.mkdir('backups')

# List Python files in current directory
py_files = [f for f in os.listdir('.') if f.endswith('.py')]
print("Python files:", py_files)
```

---

## Working with JSON
JSON (JavaScript Object Notation) is a lightweight data interchange format.

### JSON Operations:
1. **Serialization (Python → JSON)**:
   ```python
   import json
   data = {'name': 'Alice', 'age': 30}
   json_str = json.dumps(data)  # To string
   json.dump(data, open('data.json', 'w'))  # To file
   ```

2. **Deserialization (JSON → Python)**:
   ```python
   data = json.loads(json_str)  # From string
   data = json.load(open('data.json', 'r'))  # From file
   ```

**Practical Example**:
```python
import json

# Save user preferences
prefs = {'theme': 'dark', 'notifications': True}
with open('prefs.json', 'w') as f:
    json.dump(prefs, f)

# Load preferences
try:
    with open('prefs.json', 'r') as f:
        loaded_prefs = json.load(f)
except FileNotFoundError:
    loaded_prefs = {}
```

---

## Package Management with pip
pip is Python's package installer for managing third-party libraries.

### Common pip Commands:
| Command | Description |
|---------|-------------|
| `pip install package` | Install a package |
| `pip uninstall package` | Remove a package |
| `pip list` | List installed packages |
| `pip show package` | Show package info |
| `pip freeze > requirements.txt` | Save dependencies |
| `pip install -r requirements.txt` | Install from file |

**Example Workflow**:
```bash
# Install requests package
pip install requests

# Verify installation
pip show requests

# Create requirements file
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

---

## Checkpoint Questions and Answers

1. **What is the relationship between a function, a module, and a library?**
   - Functions are blocks of code that perform specific tasks. Multiple related functions can be grouped into a module (a Python file). A library is a collection of related modules packaged together.

2. **What is the purpose of file handlers?**
   - File handlers provide an interface to read from and write to files, manage file operations, and ensure proper resource cleanup.

3. **Can Python be used to run system commands?**
   - Yes, through modules like `os` (e.g., `os.system()`) or `subprocess` for more advanced control.

4. **What are exceptions used for in Python?**
   - Exceptions handle errors gracefully, allowing programs to continue running or fail with meaningful messages rather than crashing.

5. **True or False: When used, the JSON library automatically creates the correct data type for data.**
   - True. The JSON library converts JSON types to equivalent Python types (e.g., JSON object → Python dict, JSON array → Python list).

6. **What is pip?**
   - pip is Python's package manager for installing and managing third-party libraries.

7. **Why use pip?**
   - pip simplifies dependency management, ensures version compatibility, and provides easy access to thousands of Python packages.

---

## Key Takeaways
1. **Modularity**: Python's module system promotes organized, reusable code.
2. **Standard Library**: Comes with batteries included for common tasks.
3. **File Handling**: Essential for persistent data storage and retrieval.
4. **Error Handling**: Critical for robust applications.
5. **System Integration**: The `os` module bridges Python and the operating system.
6. **Data Interchange**: JSON is widely used for data serialization.
7. **Package Management**: pip is indispensable for leveraging Python's ecosystem.

---

## Additional Notes and Examples

### Advanced Module Techniques
**`__init__.py`**: Turns a directory into a package (Python < 3.3)
```python
# mypackage/__init__.py
from .submodule import useful_function
```

**Relative Imports** (within a package):
```python
from . import sibling_module
from ..parent_package import module
```

### File Handling Best Practices
1. Always close files or use `with` statements
2. Handle potential encoding issues:
   ```python
   with open('file.txt', 'r', encoding='utf-8') as f:
       content = f.read()
   ```

### Extended JSON Example
```python
import json

# Complex Python object
data = {
    'name': 'Alice',
    'age': 30,
    'pets': ['dog', 'cat'],
    'active': True,
    'balance': 1250.50,
    'address': {
        'street': '123 Main St',
        'city': 'Boston'
    }
}

# Serialize with formatting
json_str = json.dumps(data, indent=2)
print(json_str)

# Custom serialization for non-standard types
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def user_encoder(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age}
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

user = User("Bob", 25)
print(json.dumps(user, default=user_encoder))
```

### Comprehensive Exception Handling Example
```python
import os
import json

def load_config(config_file):
    """Load application configuration with robust error handling"""
    default_config = {
        'theme': 'light',
        'timeout': 30,
        'plugins': []
    }
    
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            
        # Validate required fields
        if 'theme' not in config:
            raise ValueError("Missing required 'theme' in config")
            
        return {**default_config, **config}  # Merge with defaults
        
    except FileNotFoundError:
        print(f"Config file {config_file} not found, using defaults")
        return default_config
    except json.JSONDecodeError:
        print("Invalid JSON in config file, using defaults")
        return default_config
    except PermissionError:
        print("No permission to read config file, using defaults")
        return default_config
    except Exception as e:
        print(f"Unexpected error loading config: {e}")
        return default_config

# Usage
config = load_config('app_config.json')
print(config)
```

This comprehensive guide covers all aspects of Python modules and libraries from the provided materials, with expanded explanations, practical examples, and best practices. The markdown format ensures clear organization and easy reference.