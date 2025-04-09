# Working with Insulin Data Using JSON and Python Modules

## Lab Overview
This lab demonstrates how to:
- Structure biological data in JSON format
- Create Python modules for file handling
- Calculate molecular weights from JSON data
- Implement error handling for file operations

## Exercise 1: Creating the JSON Data File

### insulin.json Structure
```json
{
   "molecules": {
      "lsInsulin": "malwmrllpllallalwgpdpaaa",
      "bInsulin": "fvnqhlcgshlvealylvcgergffytpkt",
      "aInsulin": "giveqcctsicslyqlenycn",
      "cInsulin": "rreaedlqvgqvelgggpgagslqplalegslqkr"
   },
   "weights": {
      "A": 89.09, "C": 121.16, "D": 133.10, "E": 147.13,
      "F": 165.19, "G": 75.07, "H": 155.16, "I": 131.17,
      "K": 146.19, "L": 131.17, "M": 149.21, "N": 132.12,
      "P": 115.13, "Q": 146.15, "R": 174.20, "S": 105.09,
      "T": 119.12, "V": 117.15, "W": 204.23, "Y": 181.19
   },
   "molecularWeightInsulinActual": 5807.63
}
```

**Key Features:**
- Organized structure with clear sections
- All insulin sequence components included
- Amino acid weights for calculations
- Actual molecular weight for validation

## Exercise 2: Creating the JSON File Handler Module

### jsonFileHandler.py
```python
import json

def readJsonFile(fileName):
    """Reads and parses a JSON file
    
    Args:
        fileName (str): Path to JSON file
        
    Returns:
        dict: Parsed JSON data or empty string if error occurs
    """
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: File {fileName} not found")
    except json.JSONDecodeError:
        print(f"Error: File {fileName} contains invalid JSON")
    except Exception as e:
        print(f"Unexpected error reading {fileName}: {str(e)}")
    return data
```

**Improvements:**
- Specific exception handling for different error cases
- Descriptive error messages
- Docstring explaining function purpose
- Returns consistent data type (empty string on error)

## Exercise 3: Main Program for Molecular Weight Calculation

### calc_weight_json.py
```python
import jsonFileHandler

def calculate_molecular_weight(sequence, weights):
    """Calculate molecular weight from sequence and weights"""
    aa_counts = {
        aa: float(sequence.upper().count(aa)) 
        for aa in weights.keys()
    }
    return sum(count * weights[aa] for aa, count in aa_counts.items())

def main():
    # Load data
    data = jsonFileHandler.readJsonFile('files/insulin.json')
    
    if not data:
        print("Error: Unable to process data")
        return
    
    # Extract sequences and weights
    b_insulin = data['molecules']['bInsulin']
    a_insulin = data['molecules']['aInsulin']
    insulin = b_insulin + a_insulin
    aa_weights = data['weights']
    actual_weight = data['molecularWeightInsulinActual']
    
    # Calculate and display results
    print(f"bInsulin: {b_insulin}")
    print(f"aInsulin: {a_insulin}")
    print(f"Actual molecular weight: {actual_weight:.2f}")
    
    calculated_weight = calculate_molecular_weight(insulin, aa_weights)
    error_percent = ((calculated_weight - actual_weight) / actual_weight) * 100
    
    print(f"\nCalculated molecular weight: {calculated_weight:.2f}")
    print(f"Percent error: {error_percent:.2f}%")

if __name__ == "__main__":
    main()
```

**Key Components:**
1. **Data Loading**: Uses our jsonFileHandler module
2. **Weight Calculation**: Modular function for reuse
3. **Error Handling**: Checks for valid data before processing
4. **Output Formatting**: Clear presentation of results

## Enhanced Solution with Additional Features

### Enhanced jsonFileHandler.py
```python
import json
from pathlib import Path

def read_json_file(file_path):
    """Enhanced JSON file reader with path validation"""
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Path does not exist: {file_path}")
    
    if not Path(file_path).is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file {file_path}: {str(e)}")

def write_json_file(data, file_path, indent=2):
    """Write data to JSON file with pretty printing"""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=indent)
```

### Enhanced Calculation Module (insulin_calculations.py)
```python
def calculate_molecular_weight(sequence, weights):
    """Calculate molecular weight with validation"""
    if not sequence or not weights:
        raise ValueError("Sequence and weights must be provided")
    
    sequence = sequence.upper()
    invalid_aas = set(sequence) - set(weights.keys()) - {' ', '\n', '\t'}
    
    if invalid_aas:
        raise ValueError(f"Sequence contains unknown amino acids: {invalid_aas}")
    
    return sum(sequence.count(aa) * weight for aa, weight in weights.items())

def calculate_error(calculated, actual):
    """Calculate percentage error with validation"""
    if actual == 0:
        raise ZeroDivisionError("Actual weight cannot be zero")
    return ((calculated - actual) / actual) * 100
```

### Enhanced Main Program
```python
import jsonFileHandler
import insulin_calculations as ic
import sys

def main():
    try:
        # Load and validate data
        data = jsonFileHandler.read_json_file('files/insulin.json')
        
        # Extract components
        molecules = data['molecules']
        insulin = molecules['bInsulin'] + molecules['aInsulin']
        weights = data['weights']
        actual_weight = data['molecularWeightInsulinActual']
        
        # Perform calculations
        calc_weight = ic.calculate_molecular_weight(insulin, weights)
        error = ic.calculate_error(calc_weight, actual_weight)
        
        # Display results
        print("\nInsulin Analysis Results")
        print("=" * 40)
        print(f"Combined sequence length: {len(insulin)} aa")
        print(f"Calculated weight: {calc_weight:.2f} Da")
        print(f"Actual weight: {actual_weight:.2f} Da")
        print(f"Error: {error:.2f}%")
        
        # Explain error sources
        if error > 5:
            print("\nNote: The error >5% occurs because this calculation:")
            print("- Doesn't account for disulfide bond formation")
            print("- Ignores post-translational modifications")
            print("- Uses average amino acid weights")
    
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **JSON for Structured Data**:
   - Ideal for hierarchical biological data
   - Human-readable format
   - Easy to parse in Python

2. **Modular Design**:
   - Separate file handling from business logic
   - Reusable calculation functions
   - Clear separation of concerns

3. **Error Handling**:
   - Anticipate and handle file issues
   - Validate data before processing
   - Provide meaningful error messages

4. **Scientific Calculations**:
   - Understand limitations of simple models
   - Document assumptions
   - Explain discrepancies

## Further Improvements

1. **Unit Testing**:
   ```python
   import unittest
   class TestInsulinCalculations(unittest.TestCase):
       def test_weight_calculation(self):
           test_seq = "ACDE"
           test_weights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13}
           expected = sum(test_weights.values())
           self.assertAlmostEqual(ic.calculate_molecular_weight(test_seq, test_weights), expected)
   ```

2. **Command Line Interface**:
   ```python
   import argparse
   parser = argparse.ArgumentParser(description='Insulin molecular weight calculator')
   parser.add_argument('json_file', help='Path to insulin.json')
   args = parser.parse_args()
   ```

3. **Visualization**:
   ```python
   import matplotlib.pyplot as plt
   def plot_amino_acid_distribution(sequence, weights):
       counts = {aa: sequence.count(aa) for aa in weights}
       plt.bar(counts.keys(), counts.values())
       plt.title("Amino Acid Distribution")
       plt.show()
   ```

This lab demonstrates professional Python practices for working with scientific data, including proper project structure, error handling, and clear separation between data access and business logic.