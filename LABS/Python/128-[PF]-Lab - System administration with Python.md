# System Administration with Python - Comprehensive Guide

## Lab Overview
This lab demonstrates how to execute system commands from Python using:
- `os.system()` - Simple command execution
- `subprocess.run()` - More powerful and flexible command execution

## Exercise 1: Using os.system()

### Basic Command Execution
```python
import os

# Simple command execution
os.system("ls")  # Lists directory contents
```

**Key Points:**
- Returns exit status (0 for success)
- Output goes directly to stdout
- Limited control over the process
- Security risk with shell=True (avoid with untrusted input)

**Example Output:**
```
file1.txt  file2.py  README.md
0  # Exit status
```

## Exercise 2: Using subprocess.run()

### Basic Usage
```python
import subprocess

# Recommended approach for command execution
subprocess.run(["ls"])  # Note: command as list of arguments
```

**Advantages over os.system():**
- More control over process execution
- Better handling of input/output
- Access to process return code
- Safer by default (no shell interpretation)

## Exercise 3: Adding Command Arguments

### Long Listing Format
```python
subprocess.run(["ls", "-l"])  # Detailed directory listing
```

**Example Output:**
```
total 16
-rw-r--r-- 1 user group  123 Apr 10 10:00 file1.txt
-rwxr-xr-x 1 user group 4096 Apr  9 14:30 script.py
```

## Exercise 4: Targeting Specific Files

### Listing Specific File
```python
subprocess.run(["ls", "-l", "README.md"])  # Info about specific file
```

## Exercise 5: Retrieving System Information

### Using uname Command
```python
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])
```

**Example Output:**
```
Gathering system information with command: uname -a
Linux hostname 5.4.0-1045-aws #47-Ubuntu SMP x86_64 GNU/Linux
```

## Exercise 6: Checking Process Information

### Using ps Command
```python
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])
```

## Enhanced Implementation

### Complete System Admin Script
```python
#!/usr/bin/env python3
"""
System Administration Toolkit
Execute common system commands safely from Python
"""

import subprocess
from typing import List, Optional

def run_command(cmd: List[str], capture: bool = False) -> Optional[str]:
    """Execute a system command safely
    
    Args:
        cmd: List of command and arguments
        capture: Whether to capture output
        
    Returns:
        Command output if capture=True, None otherwise
    """
    try:
        if capture:
            result = subprocess.run(
                cmd,
                check=True,
                text=True,
                capture_output=True
            )
            return result.stdout
        else:
            subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(cmd)}")
        print(f"Error: {e.stderr}")
        raise
    except FileNotFoundError:
        print(f"Command not found: {cmd[0]}")
        raise

def get_system_info() -> dict:
    """Collect key system information"""
    info = {
        'system': run_command(["uname", "-a"], capture=True),
        'disk': run_command(["df", "-h"], capture=True),
        'memory': run_command(["free", "-h"], capture=True),
        'processes': run_command(["ps", "aux"], capture=True)
    }
    return info

def main():
    """Main execution function"""
    print("=== System Administration Toolkit ===")
    
    try:
        # Example usage
        print("\nCurrent directory contents:")
        run_command(["ls", "-lha"])
        
        print("\nSystem information:")
        info = get_system_info()
        for key, value in info.items():
            print(f"\n{key.upper()}:\n{value}")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
```

## Key Features of the Enhanced Solution

1. **Type Hints**: Better code documentation and IDE support
2. **Error Handling**: Proper exception handling for robust execution
3. **Output Capture**: Option to capture command output
4. **Modular Design**: Reusable functions for common tasks
5. **Safety**: Avoids shell=True to prevent injection vulnerabilities

## Security Best Practices

1. **Avoid shell=True**:
   ```python
   # UNSAFE - vulnerable to injection
   subprocess.run(f"ls {user_input}", shell=True)
   
   # SAFE alternative
   subprocess.run(["ls", user_input])
   ```

2. **Validate Inputs**:
   ```python
   def safe_command(cmd: str):
       allowed = ['ls', 'ps', 'df']
       if cmd not in allowed:
           raise ValueError(f"Command {cmd} not permitted")
   ```

3. **Use Absolute Paths** for critical commands

## Advanced Usage Examples

### 1. Running with Timeout
```python
try:
    subprocess.run(["ping", "google.com"], timeout=5)
except subprocess.TimeoutExpired:
    print("Command timed out")
```

### 2. Environment Variables
```python
subprocess.run(["printenv"], env={"CUSTOM_VAR": "value"})
```

### 3. Working Directory
```python
subprocess.run(["ls"], cwd="/path/to/directory")
```

### 4. Piping Commands
```python
p1 = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", ".py"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
```

## Common Use Cases

1. **Automating System Maintenance**:
   ```python
   # Update packages
   subprocess.run(["apt", "update"])
   subprocess.run(["apt", "upgrade", "-y"])
   ```

2. **Log Monitoring**:
   ```python
   # Check auth logs
   logs = subprocess.run(
       ["grep", "Failed", "/var/log/auth.log"],
       capture_output=True,
       text=True
   )
   ```

3. **Backup Operations**:
   ```python
   # Create compressed backup
   subprocess.run(["tar", "-czvf", "backup.tar.gz", "/important/data"])
   ```

## Performance Considerations

1. **For frequent commands**, consider:
   ```python
   # Reuse executable path
   from shutil import which
   ls_path = which("ls")
   subprocess.run([ls_path, "-l"])
   ```

2. **For many commands**, use `subprocess.Popen` for better control

3. **For CPU-intensive tasks**, consider native Python implementations

This lab provides a foundation for integrating Python with system administration tasks, combining Python's flexibility with the power of system commands while maintaining security and robustness.