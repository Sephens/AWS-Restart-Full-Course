# Comprehensive Lab Guide: Working with Linux Commands

## Introduction
This lab provides hands-on experience with essential Linux commands for text processing and output redirection. You'll learn to manipulate file contents, redirect output, and chain commands together using powerful Unix utilities.

## Task 2: Using the tee Command

### Step 1: Verify Working Directory
1. Check current directory:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user
   ```

### Step 2: Execute tee Command
1. Run hostname and tee output to file:
   ```bash
   hostname | tee file1.txt
   ```

**Command Breakdown:**
- `hostname`: Outputs system's hostname
- `|`: Pipe redirects output to next command
- `tee`: Copies input to both file and standard output

**Example Output:**
```
ip-10-0-10-81.us-west-2.compute.internal
```

### Step 3: Verify File Creation
1. List directory contents:
   ```bash
   ls
   ```
   **Expected Output:**
   ```
   companyA  file1.txt
   ```

**Key Concepts:**
- `tee` is useful for:
  - Saving command output while viewing it
  - Creating log files of terminal sessions
  - Splitting output streams

**Common Questions:**
Q: How to append to file instead of overwriting?
A: Use `tee -a filename` (the `-a` flag appends)

## Task 3: Using sort and Pipe Operator

### Step 1: Create Test CSV
1. Create new file with cat:
   ```bash
   cat > test.csv
   ```
2. Enter data (press Enter after each line):
   ```
   Factory, 1, Paris
   Store, 2, Dubai
   Factory, 3, Brasilia
   Store, 4, Algiers
   Factory, 5, Tokyo
   ```
3. Press CTRL+D to save

### Step 2: Sort File Contents
1. Sort file alphabetically:
   ```bash
   sort test.csv
   ```

**Expected Output:**
```
Factory, 1, Paris
Factory, 3, Brasilia
Factory, 5, Tokyo
Store, 2, Dubai
Store, 4, Algiers
```

**Sort Options:**
- `-n`: Sort numerically
- `-r`: Reverse sort order
- `-k`: Sort by specific column

### Step 3: Search with grep
1. Find Paris entry:
   ```bash
   grep Paris test.csv
   ```

**Improved Command:**
```bash
cat test.csv | grep Paris
```

**Pipe Operator Concepts:**
- Connects command output to input of next command
- Enables powerful command chaining
- Alternative to temporary files

## Task 4: Using cut and sed Commands

### Step 1: Create Cities CSV
1. Create new file:
   ```bash
   cat > cities.csv
   ```
2. Enter data:
   ```
   Dallas, Texas
   Seattle, Washington
   Los Angeles, California
   Atlanta, Georgia
   New York, New York
   ```
3. Press CTRL+D to save

### Step 2: Extract Fields with cut
1. Get first column:
   ```bash
   cut -d ',' -f 1 cities.csv
   ```

**Command Breakdown:**
- `-d ','`: Sets comma as delimiter
- `-f 1`: Selects first field

**Expected Output:**
```
Dallas
Seattle
Los Angeles
Atlanta
New York
```

### Step 3: Text Replacement with sed
1. Replace commas with periods:
   ```bash
   sed 's/,/./' cities.csv
   ```

**Advanced sed Usage:**
1. In-place editing (with backup):
   ```bash
   sed -i.bak 's/,/./' cities.csv
   ```
2. Global replacement (all occurrences):
   ```bash
   sed 's/,/./g' cities.csv
   ```

**Expected Output:**
```
Dallas. Texas
Seattle. Washington
Los Angeles. California
Atlanta. Georgia
New York. New York
```

## Additional Challenge: Command Chaining

### Solution 1: Process Multiple Files
```bash
sed 's/,/./' cities.csv > temp && sed 's/,/./' test.csv >> temp
```

### Solution 2: Using xargs
```bash
echo "cities.csv test.csv" | xargs -n 1 sed 's/,/./'
```

### Solution 3: Using tee with Process Substitution
```bash
sed 's/,/./' cities.csv | tee >(sed 's/,/./' test.csv)
```

## Comprehensive Command Reference

| Command | Description | Common Options |
|---------|-------------|----------------|
| `tee`   | Split output | `-a` (append) |
| `sort`  | Sort lines | `-n` (numeric), `-r` (reverse) |
| `grep`  | Pattern search | `-i` (ignore case), `-v` (invert) |
| `cut`   | Extract columns | `-d` (delimiter), `-f` (fields) |
| `sed`   | Stream editor | `-i` (in-place), `s/old/new/` (substitute) |

## Real-World Applications

1. **Log Processing**: Extract specific fields from server logs
2. **Data Cleaning**: Format CSV files for analysis
3. **System Administration**: Parse command output for monitoring
4. **Automation**: Create scripts for repetitive text tasks

## Best Practices

1. **Backup Files**: Always make copies before bulk edits
2. **Test Commands**: Try on small samples first
3. **Use Quotes**: Protect special characters in patterns
4. **Document Pipelines**: Comment complex command chains
5. **Check Exit Codes**: Verify success of each command

This lab provides fundamental skills for efficient text processing in Linux environments, forming the basis for more advanced system administration and data processing tasks.