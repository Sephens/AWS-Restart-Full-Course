# Working with Composite Data Types - Lab Explanation

## Lab Overview
This lab demonstrates how to work with nested data structures in Python, specifically focusing on:
- Combining dictionaries within lists
- Reading and processing CSV files
- Using deep copies for data integrity
- Working with multiple data types in a structured format

## Exercise 1: Creating Car Inventory Data

### Understanding Composite Data Types
Composite data types combine primitive types (integers, strings, etc.) into more complex structures. In this lab, we're creating:
1. A dictionary to represent vehicle properties
2. A list to hold multiple vehicle dictionaries
3. Reading data from a CSV file into this structure

### Setting Up the CSV File
**File: car_fleet.csv**
```csv
vin,make,model,year,range,topSpeed,zeroSixty,mileage
TMX20122,AnyCompany Motors,Coupe,2012,335,155,4.1,50000
TM320163,AnyCompany Motors,Sedan,2016,240,140,5.2,20000
TMX20121,AnyCompany Motors,SUV,2012,295,155,4.7,100000
TMX20204,AnyCompany Motors,Truck,2020,300,155,3.5,0
```

**Key Points:**
- First row contains headers/column names
- Subsequent rows contain vehicle data
- Data includes both strings and numeric values

## Exercise 2: Creating the Car Inventory Program

### Importing Required Modules
```python
import csv
import copy
```
- `csv` module provides functionality to read/write CSV files
- `copy` module is used to create deep copies of dictionaries

### Defining the Vehicle Template
```python
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}
```
**Structure Explanation:**
- Dictionary keys match CSV column headers
- Initialized with default values
- Mixed data types (strings, integers, float)

### Printing the Template Structure
```python
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
```
**Output:**
```
vin : <empty>
make : <empty>
model : <empty>
year : 0
range : 0
topSpeed : 0
zeroSixty : 0.0
mileage : 0
```

### Reading and Processing the CSV File
```python
myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = int(row[3])  # Convert to integer
            currentVehicle["range"] = int(row[4])
            currentVehicle["topSpeed"] = int(row[5])
            currentVehicle["zeroSixty"] = float(row[6])
            currentVehicle["mileage"] = int(row[7])
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')
```

**Key Concepts:**
1. **Context Manager (`with` statement):**
   - Ensures proper file handling (automatically closes file)
   - Creates a file object `csvFile`

2. **CSV Reader:**
   - `csv.reader()` parses the CSV file
   - `delimiter=','` specifies how columns are separated

3. **Line Processing:**
   - First line (header) is handled separately
   - Subsequent lines contain vehicle data

4. **Deep Copy Importance:**
   - `copy.deepcopy()` creates independent copies
   - Without this, all entries would reference the same dictionary

5. **Type Conversion:**
   - Explicitly converting strings to appropriate numeric types
   - Ensures proper data type for numerical operations

### Printing the Inventory
```python
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
    print("-----")
```

**Sample Output:**
```
vin : TMX20122
make : AnyCompany Motors
model : Coupe
year : 2012
range : 335
topSpeed : 155
zeroSixty : 4.1
mileage : 50000
-----
vin : TM320163
make : AnyCompany Motors
model : Sedan
year : 2016
range : 240
topSpeed : 140
zeroSixty : 5.2
mileage : 20000
-----
[Additional vehicles...]
```

## Deep Dive: Important Concepts

### Shallow vs. Deep Copy
```python
# Shallow copy (problematic for nested structures)
currentVehicle = myVehicle  # All entries would reference same dictionary

# Deep copy (correct approach)
currentVehicle = copy.deepcopy(myVehicle)  # Creates independent copy
```

### CSV Processing Best Practices
1. Always check for header rows
2. Handle type conversion explicitly
3. Validate data (missing values, incorrect formats)
4. Consider using `csv.DictReader` for header-based access

### Composite Data Structure Benefits
1. **Organization:** Keeps related data together
2. **Flexibility:** Can represent complex real-world entities
3. **Extensibility:** Easy to add new properties
4. **Processing:** Enables batch operations on collections

## Common Questions

**Q: Why not use pandas for CSV processing?**
A: While pandas is excellent for data analysis, this lab focuses on core Python concepts. Understanding these fundamentals is essential before using higher-level libraries.

**Q: How would I handle missing data?**
A: You could add validation:
```python
currentVehicle["year"] = int(row[3]) if row[3] else 0
```

**Q: What if my CSV has different columns?**
A: You would need to:
1. Update the `myVehicle` template
2. Adjust the column indices
3. Consider using `csv.DictReader` for more robust handling

## Practical Applications

1. **Data Import/Export:** Reading from databases or external sources
2. **Configuration Management:** Storing complex application settings
3. **Object Modeling:** Representing real-world entities before OOP
4. **Data Transformation:** Preparing data for analysis or visualization

## Enhanced Example: Adding Data Validation

```python
def validate_vehicle(vehicle):
    """Validate vehicle data meets certain criteria"""
    if not vehicle["vin"] or len(vehicle["vin"]) < 5:
        return False
    if vehicle["year"] < 1900 or vehicle["year"] > 2023:
        return False
    return True

# During processing:
valid_vehicles = []
for vehicle in myInventoryList:
    if validate_vehicle(vehicle):
        valid_vehicles.append(vehicle)
```

## Conclusion

This lab covered essential skills for working with composite data types:
1. Creating nested data structures (dictionaries in lists)
2. Properly reading and parsing CSV files
3. Maintaining data integrity with deep copies
4. Processing and displaying structured data

These concepts form the foundation for more advanced data handling in Python, including working with databases, APIs, and data analysis libraries.