# AWS re/Start - Debugging and Testing in Python

Below is a comprehensive markdown document covering all content from the Debugging and Testing module, with detailed explanations, practical examples, and additional insights.

---

## Module Overview
**Title**: Debugging and Testing  
**Subtitle**: Python Fundamentals  
**Presenter**: [Name]  
**Date**: [Date]  
**Copyright**: © 2020, Amazon Web Services, Inc. or its affiliates. All rights reserved.

---

## Learning Objectives
By the end of this module, you will learn how to:
1. Explain the purpose of debugging and testing code
2. Use debuggers to find bugs in Python code
3. Perform static analysis on Python code
4. Implement dynamic analysis techniques
5. Understand different types of software testing

---

## Debugging Fundamentals

### What is Debugging?
Debugging is the process of:
1. **Identifying defects** in code
2. **Fixing those defects**

**Example Scenario**:
```python
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # Potential ZeroDivisionError
```

### Python Debugger (PDB)
The built-in Python debugger allows line-by-line execution and inspection.

**Basic Commands**:
| Command | Action |
|---------|--------|
| `n` | Next line |
| `s` | Step into function |
| `c` | Continue until breakpoint |
| `p <var>` | Print variable value |
| `q` | Quit debugger |

**Example Usage**:
```bash
python -m pdb my_script.py
```

---

## Static Analysis

### Definition
Analysis performed **without executing code**:
- Syntax checking
- Code style validation
- Complexity analysis

**Tools**:
1. **Python Interpreter**: Basic syntax checking
   ```bash
   python -m py_compile script.py
   ```
2. **IDEs**: Real-time error detection (PyCharm, VS Code)
3. **Linters**: `pylint`, `flake8`, `mypy`

**Example Pylint Output**:
```
************* Module example
C:  5, 0: Missing function docstring (missing-docstring)
C:  5, 4: Argument name "x" doesn't conform to snake_case (invalid-name)
```

### Advantages vs Disadvantages
| Advantages | Disadvantages |
|------------|---------------|
| Early bug detection | False positives |
| Consistent code style | Time-consuming manual review |
| Catches syntax errors | Limited to visible code |

---

## Dynamic Analysis

### Definition
Analysis performed **during code execution**:
- Runtime error detection
- Performance monitoring
- Memory usage tracking

**Techniques**:
1. **Debugging Mode**: Step-through execution
2. **Assertions**: Runtime condition checks
   ```python
   def process_age(age):
       assert age > 0, "Age must be positive"
       return age * 2
   ```
3. **Logging**: Runtime event recording

**Logging Example**:
```python
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error(f"Division by zero: {e}")
        raise
    return result
```

### Advantages vs Disadvantages
| Advantages | Disadvantages |
|------------|---------------|
| Real-world behavior | Resource intensive |
| Catches runtime errors | Difficult to reproduce issues |
| Works with compiled code | Incomplete coverage |

---

## Software Testing Hierarchy

### Testing Pyramid
1. **Unit Tests** (70%)
   - Test individual components
   - Fast execution
   - Example: `unittest`, `pytest`
   
   ```python
   # test_calculator.py
   def test_addition():
       assert add(2, 3) == 5
   ```

2. **Integration Tests** (20%)
   - Test component interactions
   - Medium execution speed
   - Example: Database + API tests

3. **System Tests** (8%)
   - Full system validation
   - Slow execution
   - Example: End-to-end UI tests

4. **Acceptance Tests** (2%)
   - Business requirement validation
   - Very slow
   - Example: User acceptance testing (UAT)

---

## Practical Demonstrations

### Static Debugging Exercise
1. Create `debug.py`:
   ```python
   # Contains two errors
   var = "Double Value"
   sumvalue = var + 4  # TypeError

   def dosomething(valuetocheck):
       if valuetocheck > 4:
       print("Bad indent")  # IndentationError
   ```

2. Run and analyze errors:
   ```bash
   python debug.py
   ```

### Dynamic Debugging Exercise
1. Modify `debug.py`:
   ```python
   def checkvalue(valuetocheck):
       assert type(valuetocheck) is int, "Must enter a number"
       assert valuetocheck > 0, "Value must be > 0"
       if valuetocheck > 4:
           print("Value > 4")

   var = int(input("Enter number > 0: "))
   checkvalue(var)
   ```

2. Test with various inputs:
   ```bash
   python debug.py
   ```

---

## Logging Best Practices

### What to Log
| Category | Examples |
|----------|---------|
| Errors | Exceptions, stack traces |
| Events | User logins, transactions |
| Performance | Execution times, memory usage |
| System | Startup/shutdown events |

### Python Logging Levels
| Level | When to Use |
|-------|------------|
| DEBUG | Diagnostic information |
| INFO | Confirmation messages |
| WARNING | Potential issues |
| ERROR | Serious problems |
| CRITICAL | Application failure |

**Configuration Example**:
```python
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

---

## Checkpoint Questions & Answers

1. **What is the purpose of debugging?**  
   Debugging enables developers to identify and fix logic errors in code, ensuring correct program behavior.

2. **Why learn PDB?**  
   PDB provides granular control over code execution, allowing inspection of variables and program state at specific points.

3. **Static vs dynamic for small programs?**  
   Static analysis is typically more effective for small programs as the entire codebase can be easily reviewed for errors.

4. **Unit vs integration tests?**  
   - Unit tests verify individual components in isolation  
   - Integration tests verify interactions between components  

---

## Key Takeaways

1. **Debugging Techniques**:
   - Use PDB for step-by-step execution
   - Combine static and dynamic analysis
   - Implement comprehensive logging

2. **Testing Strategy**:
   - Follow the testing pyramid (70/20/8/2 rule)
   - Automate where possible (CI/CD pipelines)
   - Validate at all levels (unit to acceptance)

3. **Best Practices**:
   - Log meaningful events with proper context
   - Use assertions for critical conditions
   - Maintain consistent coding standards

4. **Tool Ecosystem**:
   ```mermaid
   graph LR
   A[Debugging] --> B(PDB)
   A --> C(IDE Debuggers)
   D[Testing] --> E(pytest)
   D --> F(unittest)
   E --> G(Unit Tests)
   E --> H(Integration Tests)
   ```

---

This document provides both the core content from the module and substantial additional explanations, examples, and practical applications to deepen understanding of debugging and testing in Python projects.