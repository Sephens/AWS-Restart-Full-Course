# Mastering Python Debugging with pdb and Cloud9

## Lab Overview
This lab introduces debugging techniques in Python using:
- AWS Cloud9's built-in debugger
- Breakpoints and watch expressions
- Step-by-step code execution
- Variable inspection

## Exercise 1: Basic Debugging Workflow

### Sample Code for Debugging
```python
# debug_demo.py
name = "John"
print("Hello " + name + ".")
age = 40
print(name + " is " + str(age) + " years old.")
```

### Debugging Steps in Cloud9

1. **Setting Breakpoints**:
   - Click the gutter (left margin) next to line numbers 1 and 4
   - Breakpoints appear as red circles

2. **Adding Watch Expressions**:
   - In Debugger tab, add variables `name` and `age` to watch

3. **Running in Debug Mode**:
   - Click the "Run" button
   - Select "Run in Debug Mode"
   - Execution pauses at first breakpoint (line 1)

4. **Debugging Controls**:
   - **Step Over**: Execute current line (F10)
   - **Step Into**: Enter function calls (F11)
   - **Step Out**: Complete current function (Shift+F11)
   - **Continue**: Run to next breakpoint (F8)

5. **Inspecting Variables**:
   - Watch expressions update automatically
   - Hover over variables to see current values
   - View full call stack in Debugger tab

## Exercise 2: Advanced Debugging Techniques

### Debugging Complex Programs
```python
# insulin_calculator.py
def calculate_molecular_weight(sequence, weights):
    total = 0
    for aa in sequence.upper():  # Set breakpoint here
        if aa in weights:
            total += weights[aa]
    return total

if __name__ == "__main__":
    insulin_sequence = "GIVEQCCTSICSLYQLENYCN"
    aa_weights = {
        'A': 89.09, 'C': 121.16, 'D': 133.10, 
        'E': 147.13, 'F': 165.19, 'G': 75.07,
        # ... other amino acids ...
    }
    
    result = calculate_molecular_weight(insulin_sequence, aa_weights)
    print(f"Molecular weight: {result:.2f}")
```

### Debugging Strategies

1. **Conditional Breakpoints**:
   - Right-click breakpoint → "Edit Breakpoint"
   - Set condition like `aa == 'C'` to pause on cysteine residues

2. **Exception Breakpoints**:
   - Configure to break on uncaught exceptions
   - Helps identify where errors originate

3. **Debug Console**:
   - Evaluate expressions mid-execution
   - Test fixes without restarting

4. **Call Stack Inspection**:
   - View complete execution path
   - Navigate between stack frames

## Command Line Debugging with pdb

For environments without GUI debuggers:

```python
import pdb

def problematic_function(x):
    result = x * 2
    pdb.set_trace()  # Manual breakpoint
    return result + 5

problematic_function(10)
```

### Essential pdb Commands:
| Command | Description |
|---------|-------------|
| `l` | List source code around current line |
| `n` | Next line (step over) |
| `s` | Step into function |
| `c` | Continue execution |
| `p expr` | Print expression value |
| `q` | Quit debugger |

## Debugging Best Practices

1. **Reproduce the Issue**:
   - Identify exact inputs causing the problem
   - Create minimal reproducible example

2. **Incremental Checking**:
   - Verify assumptions at each step
   - Check function pre/post conditions

3. **Logging Alternative**:
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   logger = logging.getLogger(__name__)
   
   def calculate_weight(sequence):
       logger.debug(f"Processing sequence: {sequence}")
       # ... calculations ...
   ```

4. **Debugger Types**:
   - **Post-mortem**: `python -m pdb script.py`
   - **Remote**: Debugging across machines
   - **Web-based**: For Django/Flask apps

## Cloud9-Specific Features

1. **Visual Debugging**:
   - Variable inspection panels
   - Interactive watch expressions
   - Breakpoint management

2. **Integration**:
   - Works with Django/Flask
   - Supports remote debugging
   - Configurable launch.json

3. **Keyboard Shortcuts**:
   - Toggle breakpoint: F9
   - Step over: F10
   - Continue: F5

## Real-World Debugging Scenario

Debugging a scientific calculation:

1. **Symptoms**: Wrong molecular weight calculation
2. **Approach**:
   - Set breakpoint at start of calculation
   - Step through each amino acid
   - Verify weight lookup values
   - Check sequence uppercase conversion
3. **Discovery**: Missing amino acid in weights table
4. **Fix**: Add missing amino acid weights

## Advanced Topics

1. **Time-Travel Debugging**:
   - Record execution for backward stepping
   - Tools like `rr` or `pdb++`

2. **Performance Debugging**:
   ```python
   import cProfile
   cProfile.run('calculate_molecular_weight("GIVEQCCTSICSLYQLENYCN", aa_weights)')
   ```

3. **Memory Debugging**:
   ```python
   from tracemalloc import start, take_snapshot, compare_to
   start()
   # ... code ...
   snapshot = take_snapshot()
   top_stats = snapshot.statistics('lineno')
   ```

This lab provides essential skills for identifying and fixing bugs in Python code, using both graphical debuggers and command-line tools. Mastering these techniques will significantly improve your troubleshooting efficiency.