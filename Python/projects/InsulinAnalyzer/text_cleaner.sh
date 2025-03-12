#!/bin/bash

# Define input and output files
INPUT_FILE="preproinsulin-seq.txt"
OUTPUT_FILE="cleaned_preproinsulin-seq.txt"

# Process the file to remove unwanted characters
CLEANED_DATA=$(sed -E 's/ORIGIN//g; s/[0-9]//g; s/\/\///g; s/\s+//g' "$INPUT_FILE" | tr -d '\r\n')

# Save the cleaned data to the output file
echo -n "$CLEANED_DATA" > "$OUTPUT_FILE"

# Check the character count
CHAR_COUNT=$(wc -c < "$OUTPUT_FILE")

echo "File cleaned and saved as $OUTPUT_FILE"
echo "Character count: $CHAR_COUNT"

# Confirm if the file has exactly 110 characters
if [[ $CHAR_COUNT -eq 110 ]]; then
  echo "✅ The cleaned sequence has exactly 110 characters."
else
  echo "❌ Warning: The cleaned sequence does not have 110 characters."
fi

