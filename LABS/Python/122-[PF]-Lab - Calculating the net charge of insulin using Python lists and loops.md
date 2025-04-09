# Calculating Net Charge of Insulin Using Python

## Lab Overview
This lab demonstrates how to calculate the net charge of insulin across different pH levels using:
- Dictionaries to store pKa values
- List comprehensions to count amino acids
- While loops to iterate through pH values
- Mathematical formulas for charge calculations

## Exercise 1: Setting Up Variables and Dictionaries

### Sequence Variables
```python
# Store insulin sequences
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin
```

### pKa Dictionary
```python
pKR = {
    'y': 10.07,  # Tyrosine
    'c': 8.18,   # Cysteine
    'k': 10.53,  # Lysine
    'h': 6.00,   # Histidine
    'r': 12.48,  # Arginine
    'd': 3.65,   # Aspartic Acid
    'e': 4.25    # Glutamic Acid
}
```

**Key Points:**
- Only these 7 amino acids contribute to net charge
- pKa values indicate pH where 50% of groups are protonated

## Exercise 2: Counting Relevant Amino Acids

### Using List Comprehension
```python
seqCount = {
    x: float(insulin.count(x)) 
    for x in ['y','c','k','h','r','d','e']
}
```

**What This Does:**
- Counts occurrences of each charged amino acid
- Converts counts to floats for precise calculations
- Creates dictionary with amino acid counts like:
  ```python
  {'y': 4.0, 'c': 6.0, 'k': 1.0, ...}
  ```

## Exercise 3: Net Charge Calculation

### pH Loop and Charge Calculation
```python
pH = 0
while pH <= 14:
    # Calculate positive charges (N-terminus, K, H, R)
    positiveCharge = sum(
        (seqCount[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x]))
        for x in ['k','h','r']
    )
    
    # Calculate negative charges (C-terminus, Y, C, D, E)
    negativeCharge = sum(
        (seqCount[x] * (10**pH)) / ((10**pH) + (10**pKR[x]))
        for x in ['y','c','d','e']
    )
    
    # Net charge is positive - negative charges
    netCharge = positiveCharge - negativeCharge
    
    # Print formatted results
    print(f'pH {pH:.2f}: Net Charge {netCharge:+0.2f}')
    
    # Increment pH
    pH += 1
```

### Understanding the Formula
The charge calculation uses the Henderson-Hasselbalch equation:
```
Charge = [A⁻] = [HA]/(1 + 10^(pH-pKa))
```

**Components:**
1. **Positive Charges**:
   - Lysine (K), Histidine (H), Arginine (R)
   - N-terminus (not shown but typically included)

2. **Negative Charges**:
   - Tyrosine (Y), Cysteine (C)
   - Aspartic Acid (D), Glutamic Acid (E)
   - C-terminus (not shown but typically included)

## Enhanced Solution with Improvements

```python
def calculate_net_charge(sequence, pKR_values, pH_range=14):
    """Calculate net charge of protein across pH range"""
    # Count charged amino acids
    charged_aas = ['y','c','k','h','r','d','e']
    counts = {aa: sequence.lower().count(aa) for aa in charged_aas}
    
    # Add terminal charges (NH2 and COOH)
    counts['n_term'] = 1  # N-terminus contributes +1 when protonated
    counts['c_term'] = 1  # C-terminus contributes -1 when deprotonated
    pKR_values['n_term'] = 8.0  # Approximate pKa for N-terminus
    pKR_values['c_term'] = 3.1  # Approximate pKa for C-terminus
    
    results = []
    for pH in range(pH_range + 1):
        # Positive charges
        pos_charged = ['k','h','r','n_term']
        positive = sum(
            (counts[aa] * (10**pKR_values[aa])) / 
            ((10**pH) + (10**pKR_values[aa]))
            for aa in pos_charged
        )
        
        # Negative charges
        neg_charged = ['y','c','d','e','c_term']
        negative = sum(
            (counts[aa] * (10**pH)) / 
            ((10**pH) + (10**pKR_values[aa]))
            for aa in neg_charged
        )
        
        net_charge = positive - negative
        results.append((pH, net_charge))
    
    return results

# Calculate and print results
charge_results = calculate_net_charge(insulin, pKR)
for pH, charge in charge_results:
    print(f"pH {pH:2d}: Net Charge {charge:+0.2f}")
```

**Improvements:**
1. Added terminal charge contributions
2. Created reusable function
3. Better output formatting
4. More complete pKa set
5. Returns all results for further analysis

## Understanding the Output

The output will show how insulin's net charge changes with pH:
- **Low pH (acidic)**: More positive charges (protonated groups)
- **High pH (basic)**: More negative charges (deprotonated groups)
- **Isoelectric point (pI)**: pH where net charge = 0

## Practical Applications

1. **Protein Purification**: Helps determine optimal pH for chromatography
2. **Drug Formulation**: Guides pH selection for stable solutions
3. **Protein Engineering**: Predicts how mutations affect charge
4. **Biological Function**: Relates charge to insulin's activity

## Further Exploration

1. **Plotting Results**:
   ```python
   import matplotlib.pyplot as plt
   pHs = [x[0] for x in charge_results]
   charges = [x[1] for x in charge_results]
   plt.plot(pHs, charges)
   plt.xlabel('pH')
   plt.ylabel('Net Charge')
   plt.title('Insulin Net Charge vs pH')
   plt.show()
   ```

2. **Finding pI Programmatically**:
   ```python
   def find_pI(charge_results):
       for pH, charge in charge_results:
           if abs(charge) < 0.1:  # Close to zero
               return pH
       return None
   ```

3. **Comparing Insulin Variants**:
   - Modify sequence and compare charge profiles
   - Analyze charge differences between species

This lab provides a foundation for understanding protein charge behavior - a crucial concept in biochemistry and pharmaceutical development.