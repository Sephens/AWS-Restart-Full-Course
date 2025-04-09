# Working with Insulin Sequences and Molecular Weights in Python

## Lab Overview
This lab demonstrates how to process biological sequence data in Python by:
- Storing insulin sequences in string variables
- Performing sequence manipulations
- Calculating molecular weights
- Analyzing calculation accuracy
- Following Python coding best practices

## Exercise 1: Variable Assignment and Sequence Storage

### File Header and Initial Setup
```python
#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# Store the human preproinsulin sequence in a variable called preproInsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Combine B and A chains to form human insulin
insulin = bInsulin + aInsulin
```

**Key Points:**
- Follows PEP 8 style guide (79 char max per line)
- Uses backslash `\` for line continuation
- Descriptive variable names (camelCase convention)
- Clear comments explaining each section

## Exercise 3: Printing Sequences

### Sequence Output Methods
```python
# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

# Alternative method using multiple arguments
print("The sequence of human insulin, chain a:", aInsulin)
```

**Output Options Compared:**
1. **Simple print()**: Direct string output
2. **Concatenation**: Combines strings with `+`
3. **Multiple arguments**: Cleaner, auto-spaced output

## Exercise 4: Molecular Weight Calculation

### Weight Calculation Implementation
```python
# Calculating the molecular weight of insulin
# Creating a list of the amino acid (AA) weights
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13,
    'F': 165.19, 'G': 75.07, 'H': 155.16, 'I': 131.17,
    'K': 146.19, 'L': 131.17, 'M': 149.21, 'N': 132.12,
    'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09,
    'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Count the number of each amino acids
aaCountInsulin = {
    x: float(insulin.upper().count(x)) 
    for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 
              'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
}

# Multiply the count by the weights and sum
molecularWeightInsulin = sum(
    aaCountInsulin[x] * aaWeights[x] 
    for x in aaCountInsulin.keys()
)

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

# Compare with actual molecular weight
molecularWeightInsulinActual = 5807.63
errorPercentage = ((molecularWeightInsulin - molecularWeightInsulinActual) / 
                  molecularWeightInsulinActual) * 100
print("Error percentage: " + str(errorPercentage))
```

### Key Concepts Explained

1. **Dictionary Comprehension**:
   ```python
   aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaList}
   ```
   - Counts occurrences of each amino acid
   - Converts counts to floats for precise math

2. **Molecular Weight Calculation**:
   - Multiplies count by weight for each amino acid
   - Sums all individual weights

3. **Error Analysis**:
   - Compares calculated vs actual weight
   - Calculates percentage difference

### Understanding the Error
The calculated weight (6696.42) differs from actual (5807.63) because:
- Disulfide bonds between cysteines aren't accounted for
- Post-translational modifications are ignored
- Water molecules lost during peptide formation aren't subtracted

## Enhanced Solution with Improvements

```python
def calculate_molecular_weight(sequence, aa_weights):
    """Calculate molecular weight of a protein sequence"""
    sequence = sequence.upper()
    return sum(aa_weights.get(aa, 0) for aa in sequence)

def calculate_error(calculated, actual):
    """Calculate percentage error"""
    return ((calculated - actual) / actual) * 100

# Improved amino acid weights (monoisotopic)
aaWeightsImproved = {
    'A': 89.04768, 'C': 121.01975, 'D': 133.03751, 'E': 147.05316,
    'F': 165.07898, 'G': 75.03203, 'H': 155.06948, 'I': 131.09463,
    'K': 146.10553, 'L': 131.09463, 'M': 149.05105, 'N': 132.05352,
    'P': 115.06333, 'Q': 146.06914, 'R': 174.11168, 'S': 105.04260,
    'T': 119.05824, 'V': 117.07898, 'W': 204.08988, 'Y': 181.07390
}

# Calculate and compare weights
mw_calculated = calculate_molecular_weight(insulin, aaWeights)
mw_improved = calculate_molecular_weight(insulin, aaWeightsImproved)
mw_actual = 5807.63

print(f"Basic calculation: {mw_calculated:.2f} Da")
print(f"Improved weights: {mw_improved:.2f} Da")
print(f"Actual weight: {mw_actual:.2f} Da")
print(f"Basic error: {calculate_error(mw_calculated, mw_actual):.2f}%")
print(f"Improved error: {calculate_error(mw_improved, mw_actual):.2f}%")
```

**Improvements:**
- Modular functions for reuse
- More precise monoisotopic weights
- Better output formatting with f-strings
- Comparative error analysis

## Best Practices Demonstrated

1. **Code Organization**:
   - Logical section separation
   - Clear variable naming
   - Consistent indentation

2. **Documentation**:
   - Explanatory comments
   - Function docstrings
   - Header information

3. **Error Handling**:
   - Type casting with `str()`
   - Floating-point precision
   - Error analysis

4. **Performance**:
   - Dictionary lookups for fast weight access
   - Generator expressions for memory efficiency

## Practical Applications

This approach can be extended to:
1. **Protein Engineering**: Design novel insulin analogs
2. **Drug Development**: Calculate weights of therapeutic peptides
3. **Bioinformatics Tools**: Build sequence analysis pipelines
4. **Educational Resources**: Teach protein chemistry concepts

## Further Exploration

1. **Account for Disulfide Bonds**:
   ```python
   # Subtract weight of hydrogen atoms lost in bond formation
   ss_bond_correction = 2 * 1.008  # Per disulfide bond
   ```

2. **Post-Translational Modifications**:
   - Add weights for glycosylation
   - Account for phosphorylation

3. **3D Structure Analysis**:
   - Incorporate solvent accessibility
   - Calculate surface area to volume ratios

This lab provides a foundation for computational biology work in Python, combining string manipulation, mathematical operations, and scientific analysis in a real-world biological context.