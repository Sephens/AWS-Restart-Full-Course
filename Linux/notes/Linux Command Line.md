# Linux Command Line - Comprehensive Guide

## Table of Contents
1. [Linux Login Workflow](#linux-login-workflow)
2. [Command Syntax](#command-syntax)
3. [Essential Commands](#essential-commands)
4. [Standard Streams](#standard-streams)
5. [Bash Features](#bash-features)
6. [Key Takeaways](#key-takeaways)

---

## Linux Login Workflow

### Authentication Process
1. **Login Prompt**:  
   ```plaintext
   server88 login: username
   Password: ********
   ```
   - Username is checked against `/etc/passwd`.
   - Password is verified via `/etc/shadow`.

2. **Profile Loading**:  
   - User-specific settings are loaded from:
     - `~/.bashrc` (shell configurations)
     - `~/.bash_profile` (login settings)
     - `~/.bash_history` (command history)

3. **Home Directory**:  
   - After login, the user lands in their home directory (`/home/username`).

**Example**:  
```bash
$ pwd
/home/userA
```

---

## Command Syntax

### Structure
| Component | Purpose | Example |
|-----------|---------|---------|
| **Command** | Action to perform | `ls` |
| **Option** | Modifies command behavior | `-l` (long format) |
| **Argument** | Target of the command | `/home` |

**Example**:  
```bash
ls -l /home  # Lists contents of /home in detail
```
- `ls`: Command  
- `-l`: Option (long listing)  
- `/home`: Argument  

**Note**: Linux commands are **case-sensitive**.

---

## Essential Commands

### 1. User Information
| Command | Description | Example Output |
|---------|-------------|----------------|
| `whoami` | Current username | `userA` |
| `id` | User/group IDs | `uid=1003(userA) gid=1003(userA)` |
| `hostname` | System name | `server00` |

### 2. System Status
| Command | Description | Example Output |
|---------|-------------|----------------|
| `uptime` | System uptime | `21:39:05 up 11 min` |
| `date` | Current date/time | `Thu Mar 7 21:37:34 GMT 2019` |
| `cal` | Calendar | Displays current month |

### 3. File Operations
| Command | Description | Example |
|---------|-------------|---------|
| `touch` | Create empty file | `touch file1.txt` |
| `cat` | Display file content | `cat /etc/hosts` |
| `echo` | Print text | `echo "Hello"` → `Hello` |

**Demo**:  
```bash
$ touch notes.txt
$ echo "Linux Notes" > notes.txt
$ cat notes.txt
Linux Notes
```

---

## Standard Streams

### Input/Output Redirection
| Stream | File Descriptor | Syntax | Purpose |
|--------|-----------------|--------|---------|
| **stdin** | 0 | `<` | Read input from file |
| **stdout** | 1 | `>` | Write output to file |
| **stderr** | 2 | `2>` | Redirect errors |

**Examples**:  
1. Redirect output:  
   ```bash
   ls -l > dir_contents.txt  # Saves listing to file
   ```
2. Discard errors:  
   ```bash
   find / -name "*" 2> /dev/null  # Hides errors
   ```
3. Combine streams:  
   ```bash
   command > output.log 2>&1  # Saves both output and errors
   ```

---

## Bash Features

### 1. Tab Completion
- **Purpose**: Auto-completes commands or filenames.  
- **Usage**:  
  ```bash
  $ cat fi<Tab><Tab>  # Shows: file1.txt file2.log
  $ cat file1.txt     # Auto-completes if unique
  ```

### 2. Command History
- **View History**:  
  ```bash
  history  # Lists past commands
  ```
- **Re-run Command**:  
  ```bash
  !143  # Repeats command #143 from history
  ```

**Best Practice**:  
- Use `Ctrl+R` to search history interactively.  
- Clear sensitive commands:  
  ```bash
  history -d 143  # Deletes entry #143
  ```

---

## Key Takeaways

1. **Login Process**: Authentication → Profile Loading → Home Directory.  
2. **Command Structure**: `command [options] [arguments]`.  
3. **Redirection**: Use `>`, `<`, `2>` for I/O control.  
4. **Efficiency**: Leverage tab completion and history.  

**Essential Commands**:  
- `whoami`, `id`, `hostname` (User info)  
- `touch`, `cat`, `echo` (File operations)  

---

## Checkpoint Answers

**Q: What are the three main components of Bash command syntax?**  
A: **Command**, **Option**, **Argument**.  

**Q: How to run a command from history?**  
A: Use `!<number>` (e.g., `!143`).  

**Q: What happens if tab completion isn’t unique?**  
A: Pressing **Tab twice** shows all matching options.  

---
