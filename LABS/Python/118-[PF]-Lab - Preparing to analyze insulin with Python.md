# Preparing to Analyze Insulin with Python - Comprehensive Guide

## Lab Overview
This lab introduces bioinformatics data processing by working with human insulin sequences. You'll learn to:
- Retrieve protein sequences from NCBI
- Clean and process biological data
- Extract specific protein segments
- Balance automation vs manual processing

## Exercise 1: Retrieving Human Preproinsulin Sequence

### NCBI Data Retrieval Steps
1. Visit [NCBI Protein Database](https://ncbi.nlm.nih.gov)
2. Select "Protein" from search dropdown
3. Search for "human insulin"
4. Locate the correct record: "insulin [Homo sapiens]"
5. Copy the sequence including ORIGIN and // markers

### File Creation
```python
# Save as preproinsulin-seq.txt
ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
```

### Programmatic Cleaning (Bonus)
```python
import re

with open('preproinsulin-seq.txt', 'r') as file:
    content = file.read()

# Remove ORIGIN, numbers, //, spaces, and newlines
clean_seq = re.sub(r'ORIGIN|\d+|//|\s+', '', content)

# Verify length is 110 characters
assert len(clean_seq) == 110, f"Sequence length is {len(clean_seq)}, expected 110"

with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(clean_seq)
```

**Key Regex Components:**
- `ORIGIN` - Matches literal text
- `\d+` - Matches one or more digits
- `//` - Matches sequence terminator
- `\s+` - Matches whitespace and newlines

## Exercise 2: Extracting Insulin Components

### Understanding Preproinsulin Structure
- **Signal peptide**: aa 1-24 (removed during processing)
- **B chain**: aa 25-54 (30 aa)
- **C peptide**: aa 55-89 (35 aa) - removed in mature insulin
- **A chain**: aa 90-110 (21 aa)

### Manual Extraction Process
1. Clean sequence (remove non-amino acid characters)
2. Create separate files for each component:
   - `lsinsulin-seq-clean.txt`: aa 1-24 (signal peptide)
   - `binsulin-seq-clean.txt`: aa 25-54 (B chain)
   - `cinsulin-seq-clean.txt`: aa 55-89 (C peptide)
   - `ainsulin-seq-clean.txt`: aa 90-110 (A chain)

### Automated Extraction Solution
```python
def extract_sequence(input_file, output_file, start, end):
    with open(input_file, 'r') as f:
        content = f.read().replace('\n', '').replace(' ', '')
    
    # Remove non-sequence content
    seq = re.sub(r'ORIGIN|\d+|//', '', content)
    
    # Extract specified range (1-based to 0-based conversion)
    extracted = seq[start-1:end]
    
    with open(output_file, 'w') as f:
        f.write(extracted)
    
    print(f"Saved {output_file} with {len(extracted)} amino acids")

# Process all components
extract_sequence('preproinsulin-seq.txt', 'lsinsulin-seq-clean.txt', 1, 24)
extract_sequence('preproinsulin-seq.txt', 'binsulin-seq-clean.txt', 25, 54)
extract_sequence('preproinsulin-seq.txt', 'cinsulin-seq-clean.txt', 55, 89)
extract_sequence('preproinsulin-seq.txt', 'ainsulin-seq-clean.txt', 90, 110)
```

### Verification Code
```python
def verify_files():
    files = {
        'lsinsulin': 24,
        'binsulin': 30,
        'cinsulin': 35,
        'ainsulin': 21
    }
    
    for name, expected in files.items():
        with open(f'{name}-seq-clean.txt', 'r') as f:
            content = f.read().strip()
            assert len(content) == expected, \
                f"{name} has {len(content)} aa, expected {expected}"
    
    print("All files verified successfully")

verify_files()
```

## Automation vs Manual Processing

### Decision Factors
| Factor | Manual | Automated |
|--------|--------|-----------|
| Time for one-time task | Faster | Slower |
| Consistency | Prone to errors | Perfect consistency |
| Scalability | Doesn't scale | Handles any volume |
| Maintenance | No code to maintain | Code requires updates |
| Documentation | Process may be unclear | Code documents process |

### When to Automate
1. Repetitive tasks (>5 repetitions)
2. Large datasets (>100 records)
3. Processes requiring precision
4. Tasks that may need re-running

### When to Work Manually
1. One-time exploratory analysis
2. Small datasets (<10 records)
3. Processes requiring human judgment
4. Time-sensitive prototypes

## Advanced Sequence Analysis

### Calculating Molecular Weight
```python
# Approximate molecular weights (Da)
aa_weights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13,
    'F': 165.19, 'G': 75.07, 'H': 155.16, 'I': 131.17,
    'K': 146.19, 'L': 131.17, 'M': 149.21, 'N': 132.12,
    'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09,
    'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

def calculate_weight(sequence):
    return sum(aa_weights.get(aa, 0) for aa in sequence.upper())

# Example usage
b_chain = open('binsulin-seq-clean.txt').read().strip()
print(f"B chain molecular weight: {calculate_weight(b_chain):.2f} Da")
```

### Finding Cysteine Residues
```python
def find_cysteines(sequence):
    return [i+1 for i, aa in enumerate(sequence) if aa.upper() == 'C']

a_chain = open('ainsulin-seq-clean.txt').read().strip()
print(f"Cysteine positions in A chain: {find_cysteines(a_chain)}")
```

## Best Practices for Bioinformatics Code

1. **Document Assumptions**: Clearly state sequence numbering (0-based vs 1-based)
2. **Validate Inputs**: Check for unexpected characters
3. **Use Biological Standards**: Follow FASTA format conventions
4. **Include Unit Tests**: Verify expected behavior with test cases
5. **Handle Edge Cases**: Empty sequences, unknown amino acids

## Next Steps in Insulin Analysis

1. **Sequence Alignment**: Compare with other species
2. **Structure Prediction**: Predict 3D conformation
3. **Post-Translational Modifications**: Identify modification sites
4. **Functional Analysis**: Study binding domains

## Conclusion

This lab provides fundamental skills for:
- Retrieving biological data from authoritative sources
- Processing and cleaning sequence data
- Making informed automation decisions
- Preparing data for advanced bioinformatics analysis

The techniques learned can be applied to any protein or DNA sequence analysis task, forming the foundation for more complex computational biology projects.