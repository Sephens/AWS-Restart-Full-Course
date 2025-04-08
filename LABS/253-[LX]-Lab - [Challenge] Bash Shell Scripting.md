# Challenge Lab: Bash Shell Scripting Exercise - Comprehensive Solution

## Introduction
This challenge lab tests your ability to create an advanced Bash script that generates numbered files in batches while maintaining state between executions. The solution requires careful file system inspection and arithmetic operations in Bash.

## Step-by-Step Solution

### Step 1: Create the Script File
1. Open a text editor to create the script:
   ```bash
   nano file_generator.sh
   ```

### Step 2: Add the Shebang Line
1. First line of the script:
   ```bash
   #!/bin/bash
   ```
   - This specifies Bash as the interpreter

### Step 3: Define Your Name Variable
1. Set your name as a variable:
   ```bash
   YOUR_NAME="steve" 
   ```

### Step 4: Create Target Directory (If Needed)
1. Add directory creation logic:
   ```bash
   TARGET_DIR="numbered_files"
   mkdir -p "$TARGET_DIR"
   ```
   - `-p` flag prevents errors if directory exists

### Step 5: Find the Highest Existing Number
1. Add logic to find highest existing file number:
   ```bash
   MAX_NUM=$(ls "$TARGET_DIR" | grep "^${YOUR_NAME}[0-9]\+$" | sed "s/${YOUR_NAME}//" | sort -n | tail -1)
   ```
   **Breakdown:**
   - `ls "$TARGET_DIR"`: Lists directory contents
   - `grep "^${YOUR_NAME}[0-9]\+$"`: Matches your filename pattern
   - `sed "s/${YOUR_NAME}//"`: Removes name prefix
   - `sort -n`: Sorts numerically
   - `tail -1`: Gets highest number

2. Handle case when no files exist:
   ```bash
   if [ -z "$MAX_NUM" ]; then
       MAX_NUM=0
   fi
   ```

### Step 6: Generate New Files
1. Create the next 25 files:
   ```bash
   for ((i=1; i<=25; i++)); do
       NEXT_NUM=$((MAX_NUM + i))
       touch "${TARGET_DIR}/${YOUR_NAME}${NEXT_NUM}"
   done
   ```

### Step 7: Verify Creation
1. Add verification output:
   ```bash
   echo "Created 25 new files from ${YOUR_NAME}$((MAX_NUM + 1)) to ${YOUR_NAME}$((MAX_NUM + 25))"
   ls -l "$TARGET_DIR" | tail -25
   ```

### Complete Script
```bash
#!/bin/bash

# Configuration
YOUR_NAME="john"  # Replace with your name
TARGET_DIR="numbered_files"

# Create target directory if needed
mkdir -p "$TARGET_DIR"

# Find highest existing number
MAX_NUM=$(ls "$TARGET_DIR" | grep "^${YOUR_NAME}[0-9]\+$" | sed "s/${YOUR_NAME}//" | sort -n | tail -1)

# Handle case when no files exist
if [ -z "$MAX_NUM" ]; then
    MAX_NUM=0
fi

# Create new files
for ((i=1; i<=25; i++)); do
    NEXT_NUM=$((MAX_NUM + i))
    touch "${TARGET_DIR}/${YOUR_NAME}${NEXT_NUM}"
done

# Verification output
echo "Created 25 new files from ${YOUR_NAME}$((MAX_NUM + 1)) to ${YOUR_NAME}$((MAX_NUM + 25))"
ls -l "$TARGET_DIR" | tail -25
```

## Execution and Testing

### Step 1: Make Script Executable
```bash
chmod +x file_generator.sh
```

### Step 2: First Execution
```bash
./file_generator.sh
```
**Expected Output:**
```
Created 25 new files from john1 to john25
-rw-rw-r-- 1 user user 0 Aug 25 14:30 john1
-rw-rw-r-- 1 user user 0 Aug 25 14:30 john2
...
-rw-rw-r-- 1 user user 0 Aug 25 14:30 john25
```

### Step 3: Second Execution
```bash
./file_generator.sh
```
**Expected Output:**
```
Created 25 new files from john26 to john50
-rw-rw-r-- 1 user user 0 Aug 25 14:30 john26
...
-rw-rw-r-- 1 user user 0 Aug 25 14:31 john50
```

## Advanced Enhancements

### 1. Adding Parameterization
Modify script to accept parameters:
```bash
#!/bin/bash

# Default values
YOUR_NAME=${1:-"john"}
BATCH_SIZE=${2:-25}
TARGET_DIR=${3:-"numbered_files"}
```

### 2. Error Handling
Add validation:
```bash
if ! [[ "$BATCH_SIZE" =~ ^[0-9]+$ ]]; then
    echo "Error: Batch size must be a number" >&2
    exit 1
fi
```

### 3. Dry Run Option
Add testing mode:
```bash
DRY_RUN=false
if [ "$4" == "--dry-run" ]; then
    DRY_RUN=true
fi

if [ "$DRY_RUN" = false ]; then
    touch "${TARGET_DIR}/${YOUR_NAME}${NEXT_NUM}"
fi
```

## Common Questions

**Q: What if files get deleted in the middle?**
A: The script always looks for the highest existing number, so gaps won't affect it.

**Q: How to handle very large numbers?**
A: Bash supports numbers up to 2^63-1 (9,223,372,036,854,775,807), which should be sufficient.

**Q: Can I use leading zeros in numbering?**
A: Yes, modify the touch command:
```bash
printf -v PADDED_NUM "%04d" "$NEXT_NUM"
touch "${TARGET_DIR}/${YOUR_NAME}${PADDED_NUM}"
```

## Alternative Approach Using find

For more robust existing file detection:
```bash
MAX_NUM=$(find "$TARGET_DIR" -name "${YOUR_NAME}*" -printf '%f\n' | sed "s/${YOUR_NAME}//" | sort -n | tail -1)
```

This solution provides a complete, robust implementation that meets all challenge requirements while including additional enhancements for real-world use.