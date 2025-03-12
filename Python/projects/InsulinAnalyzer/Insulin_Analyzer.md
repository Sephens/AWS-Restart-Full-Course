Python is especially preferred in scientific computing applications such as physics, chemistry, and biology.
In this project, we will perform simple sequence manipulations and calculations on human insulin, which is a well-known hormone in the human body that is responsible for regulating sugars.

We will Retrieve the protein sequence of human insulin from human preproinsulin

# Insulin Sequence Analysis Project

This project involves the analysis of the human preproinsulin sequence, its breakdown into smaller components, and the calculation of its molecular weight. Below is a detailed explanation of the steps involved in this project.

---

## Table of Contents
- [Insulin Sequence Analysis Project](#insulin-sequence-analysis-project)
  - [Table of Contents](#table-of-contents)
  - [1. Storing the Human Preproinsulin Sequence](#1-storing-the-human-preproinsulin-sequence)
  - [2. Breaking Down the Preproinsulin Sequence](#2-breaking-down-the-preproinsulin-sequence)
  - [3. Merging Insulin Chains](#3-merging-insulin-chains)
  - [4. Printing Sequences](#4-printing-sequences)
  - [5. Calculating the Molecular Weight of Insulin](#5-calculating-the-molecular-weight-of-insulin)
    - [5.1 Amino Acid Weights](#51-amino-acid-weights)
    - [5.2 Counting Amino Acids](#52-counting-amino-acids)
    - [5.3 Calculating Molecular Weight](#53-calculating-molecular-weight)
    - [5.4 Printing the Molecular Weight](#54-printing-the-molecular-weight)
    - [5.5 Calculating Error Percentage](#55-calculating-error-percentage)
  - [6. Conclusion](#6-conclusion)
    - [Key Takeaways:](#key-takeaways)

---

## 1. Storing the Human Preproinsulin Sequence

The human preproinsulin sequence is stored in a variable called `preproInsulin`. This sequence includes the signal peptide and the insulin chains.

```python
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
```

---

## 2. Breaking Down the Preproinsulin Sequence

The preproinsulin sequence is broken down into smaller components:

- **lsInsulin**: The signal peptide.
- **bInsulin**: The B-chain of insulin.
- **aInsulin**: The A-chain of insulin.
- **cInsulin**: The C-peptide.

```python
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
```

---

## 3. Merging Insulin Chains

The B-chain and A-chain of insulin are merged into a single variable called `insulin`.

```python
insulin = bInsulin + aInsulin
```

---

## 4. Printing Sequences

The sequences are printed to the console for verification.

```python
print("The sequence of human preproinsulin:")
print(preproInsulin)

print("The sequence of human insulin, chain a: " + aInsulin)
```

---

## 5. Calculating the Molecular Weight of Insulin

The molecular weight of insulin is calculated using the amino acid weights and their counts in the insulin sequence.

### 5.1 Amino Acid Weights

A dictionary of amino acid weights is created.

```python
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}
```

### 5.2 Counting Amino Acids

The count of each amino acid in the insulin sequence is calculated.

```python
aaCountInsulin = {
    x: float(insulin.upper().count(x)) for x in [
        'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 
        'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'
    ]
}
```

### 5.3 Calculating Molecular Weight

The molecular weight is calculated by multiplying the count of each amino acid by its weight and summing the results.

```python
molecularWeightInsulin = sum({
    x: (aaCountInsulin[x] * aaWeights[x]) for x in [
        'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 
        'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'
    ]
}.values())
```

### 5.4 Printing the Molecular Weight

The calculated molecular weight is printed to the console.

```python
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
```

### 5.5 Calculating Error Percentage

The error percentage is calculated by comparing the calculated molecular weight with the actual molecular weight of insulin.

```python
molecularWeightInsulinActual = 5807.63
errorPercentage = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
print("Error percentage: " + str(errorPercentage))
```

---

## 6. Conclusion

This project demonstrates the process of analyzing the human preproinsulin sequence, breaking it down into its constituent parts, and calculating its molecular weight. The calculated molecular weight is then compared to the actual molecular weight to determine the error percentage. This type of analysis is crucial in bioinformatics and molecular biology for understanding protein structure and function.

---

### Key Takeaways:
- The preproinsulin sequence is processed to extract the A-chain, B-chain, and C-peptide.
- The molecular weight of insulin is calculated using amino acid weights and their counts.
- The error percentage provides insight into the accuracy of the calculation compared to the known molecular weight.

This project serves as a foundational example of sequence analysis and molecular weight calculation in bioinformatics.

