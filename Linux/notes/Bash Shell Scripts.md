# Bash Shell Scripts - Comprehensive Guide

## Table of Contents
1. [Introduction to Bash Scripting](#introduction-to-bash-scripting)
2. [Creating and Running Scripts](#creating-and-running-scripts)
3. [Script Variables and Arguments](#script-variables-and-arguments)
4. [Conditional Statements](#conditional-statements)
5. [Loop Statements](#loop-statements)
6. [Useful Commands and Operators](#useful-commands-and-operators)
7. [Script Permissions and Execution](#script-permissions-and-execution)
8. [Key Takeaways](#key-takeaways)

---

## Introduction to Bash Scripting

### What is a Script?
A script is a text file containing a series of commands that are executed sequentially when the script is run. Scripts automate repetitive tasks, ensure consistency, and can be scheduled to run at specific times (e.g., using `cron`).

**Common Script Tasks:**
- Creating backup jobs (e.g., `tar -cf backup-home.tar /home/ec2-user`)
- Archiving log files
- Configuring systems and services
- Simplifying repetitive tasks (e.g., batch renaming files)
- Automating deployments (e.g., installing software on EC2 instances at launch)

**Example Backup Script:**
```bash
#!/bin/bash
# Script to backup the home directory
tar -cf backup-home.tar /home/ec2-user
echo "Backup job complete at $(date)"
```
**Output:**
```
tar: Removing leading '/' from member names
Backup job complete at Fri Jun 18 08:13:30 UTC 2021
```

---

## Creating and Running Scripts

### Steps to Create and Run a Script:
1. **Create the Script**: Use a text editor (e.g., `nano`, `vim`) to write the script.
   ```bash
   #!/bin/bash
   echo "Hello $USER"
   echo "Today's date is: $(date)"
   ```
2. **Set Permissions**: Make the script executable.
   ```bash
   chmod +x hello.sh
   ```
3. **Run the Script**: Execute it using `./`.
   ```bash
   ./hello.sh
   ```
   **Output:**
   ```
   Hello ec2-user
   Today's date is: Fri Jun 18 08:22:27 UTC 2021
   ```

### Shebang (`#!/bin/bash`)
- The first line (`#!/bin/bash`) specifies the interpreter (Bash).
- Without it, the system uses the default shell, which may not support all Bash features.

---

## Script Variables and Arguments

### Declaring Variables:
```bash
#!/bin/bash
NAME="Mary Major"
echo $NAME
```
**Output:**
```
Mary Major
```

### Command-Line Arguments:
- `$1`, `$2`, etc., represent arguments passed to the script.
- Example:
  ```bash
  #!/bin/bash
  sum=$(($1 + $2))
  echo "$1 + $2 equals $sum"
  ```
  **Run:**
  ```bash
  ./math.sh 3 8
  ```
  **Output:**
  ```
  3 + 8 equals 11
  ```

### Command Substitution:
- Use backticks or `$()` to embed commands.
  ```bash
  echo "Today's date is: $(date)"
  ```

---

## Conditional Statements

### `if` Statement:
```bash
#!/bin/bash
if [ $? -eq 0 ]; then
  echo "Command succeeded"
else
  echo "Command failed"
fi
```
- `$?` checks the exit status of the last command (`0` = success).

### `if-elif-else`:
```bash
if [ $1 -gt $2 ]; then
  echo "$1 is greater"
elif [ $1 -lt $2 ]; then
  echo "$2 is greater"
else
  echo "Equal"
fi
```

### Test Command:
```bash
test 100 -lt 99 && echo "Yes" || echo "No"
```
**Output:**
```
No
```

---

## Loop Statements

### `for` Loop:
```bash
for x in 1 2 3 a b c; do
  echo "Value: $x"
done
```
**Output:**
```
Value: 1
Value: 2
Value: 3
Value: a
Value: b
Value: c
```

### `while` Loop:
```bash
counter=1
while [ $counter -le 5 ]; do
  echo $counter
  ((counter++))
done
```
**Output:**
```
1
2
3
4
5
```

### `break` and `continue`:
- `break`: Exits the loop.
- `continue`: Skips the current iteration.

---

## Useful Commands and Operators

### Common Commands:
| Command | Description |
|---------|-------------|
| `echo`  | Print text   |
| `read`  | Read user input |
| `mkdir` | Create directory |
| `chmod` | Change permissions |
| `grep`  | Search text |

### String Comparisons:
```bash
if [ "$1" = "hello" ]; then
  echo "Greeting detected"
fi
```

### Arithmetic Operators:
```bash
sum=$((5 + 3))
echo "Sum: $sum"
```

---

## Script Permissions and Execution

### Setting Permissions:
```bash
chmod 744 script.sh  # rwxr--r--
chmod u+x script.sh  # Add execute for user
```

### Running Scripts:
- Use `./` to run scripts not in `$PATH`:
  ```bash
  ./script.sh
  ```
- Full path:
  ```bash
  /home/user/script.sh
  ```

---

## Key Takeaways
1. **Automation**: Scripts save time by automating tasks.
2. **Documentation**: Use templates for consistency.
3. **Testing**: Always test scripts before deployment.
4. **Security**: Limit permissions and validate inputs.
5. **Flexibility**: Use variables and arguments for reusable scripts.

**Example Template:**
```bash
#!/bin/bash
# Author: Jane Doe
# Date: 2023-10-01
# Description: Backup script for /home
tar -czf /backup/home-$(date +%F).tar.gz /home
```

---

## Checkpoint Answers
**Q: What tasks can you automate with scripts?**  
A: Backups, log rotation, system configurations, and repetitive file operations.

**Q: When to use conditional statements?**  
A: When decisions are needed (e.g., check if a file exists before deleting it).

---
