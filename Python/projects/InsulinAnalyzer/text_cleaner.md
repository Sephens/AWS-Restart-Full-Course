# Cleaning Script Documentation

## Overview
This Bash script processes a text file containing a preproinsulin sequence, removes unnecessary characters, and ensures the cleaned output has exactly 110 characters.

---

## How It Works
1. **Reads the input file (`preproinsulin-seq.txt`).**
2. **Removes unwanted elements** using `sed` and `tr`:
   - Removes `ORIGIN`
   - Removes all numbers (`0-9`)
   - Removes `//` symbols (slashes)
   - Removes spaces, tabs, and newlines
3. **Saves the cleaned data** into an output file (`cleaned_preproinsulin-seq.txt`).
4. **Counts the number of characters** in the cleaned file.
5. **Checks if the file contains exactly 110 characters** and outputs a success or warning message.

---

## Script Breakdown

### **1. Define Input and Output Files**
```bash
INPUT_FILE="preproinsulin-seq.txt"
OUTPUT_FILE="cleaned_preproinsulin-seq.txt"
```
- `INPUT_FILE`: The file containing the original sequence.
- `OUTPUT_FILE`: The file where the cleaned sequence will be saved.

### **2. Clean the File Using `sed` and `tr`**
```bash
CLEANED_DATA=$(sed -E 's/ORIGIN//g; s/[0-9]//g; s/\/\///g; s/\s+//g' "$INPUT_FILE" | tr -d '\r\n')
```
#### **Explanation:**
- **`sed -E`**: Enables extended regular expressions.
- **`s/ORIGIN//g`**: Removes the word "ORIGIN".
- **`s/[0-9]//g`**: Removes all digits (0-9).
- **`s/\/\///g`**: Removes `//` (double slashes).
- **`s/\s+//g`**: Removes all whitespace (spaces, tabs, newlines).
- **`tr -d '\r\n'`**: Deletes carriage returns (`\r`) and newlines (`\n`), ensuring the output is a single continuous string.

### **3. Save the Cleaned Data to a File**
```bash
echo -n "$CLEANED_DATA" > "$OUTPUT_FILE"
```
- `echo -n`: Prints the cleaned data without adding an extra newline.
- `> "$OUTPUT_FILE"` Overwrites the file with the cleaned content.

### **4. Count Characters in the Cleaned File**
```bash
CHAR_COUNT=$(wc -c < "$OUTPUT_FILE")
```
- **`wc -c`**: Counts characters in the file.
- `< "$OUTPUT_FILE"`: Reads the file’s content.
- The result is stored in `CHAR_COUNT`.

### **5. Display Results and Validate Character Count**
```bash
echo "File cleaned and saved as $OUTPUT_FILE"
echo "Character count: $CHAR_COUNT"

if [[ $CHAR_COUNT -eq 110 ]]; then
  echo "✅ The cleaned sequence has exactly 110 characters."
else
  echo "❌ Warning: The cleaned sequence does not have 110 characters."
fi
```
#### **Explanation:**
- Prints the filename and character count.
- Checks if the file has exactly **110 characters**.
- Displays a ✅ success message if true, or ❌ a warning if false.

---

## Running the Script
1. **Make the script executable:**
   ```bash
   chmod +x clean_sequence.sh
   ```
2. **Run the script:**
   ```bash
   ./clean_sequence.sh
   ```

---

## Expected Output
```
File cleaned and saved as cleaned_preproinsulin-seq.txt
Character count: 110
✅ The cleaned sequence has exactly 110 characters.
```

If the character count is not 110, the script will warn you:
```
❌ Warning: The cleaned sequence does not have 110 characters.
```

---

## Summary
| Command | Purpose |
|---------|---------|
| `sed -E` | Uses extended regular expressions to modify text. |
| `s/ORIGIN//g` | Removes the word `ORIGIN`. |
| `s/[0-9]//g` | Removes all numbers. |
| `s/\/\///g` | Removes double slashes `//`. |
| `s/\s+//g` | Removes all whitespace. |
| `tr -d '\r\n'` | Deletes newlines and carriage returns. |
| `wc -c` | Counts characters in the output file. |

🚀 This script ensures **efficient processing** of sequence data while maintaining correctness! 🎯


A carriage return (\r) is a control character used in text files to move the cursor to the beginning of a line. It originates from typewriters, where the carriage (which holds the paper) would physically return to the starting position when a new line was needed.
