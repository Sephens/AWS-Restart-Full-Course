## Working with Composite Data Types

A composite data type is any data type that comprises primitive data types
In this lab, you will create a data type that consists of a string that is in a dictionary, which is in a list.

In this lab, you will:

- Use numeric data types
- Use string data types
- Use the dictionary data type
- Use the list data type
- Use a for loop
- Use the print() function
- Use the if statement
- Use the else statement
- Use the import statement

### Creating a car inventory program
#### Defining the dictionary
You will read in the csv file by using a module called csv. 
Additionally, you will make a deep copy of the data to store in memory by using a module called copy.

```
import csv
import copy

```

Next, define a dictionary that will serve as your composite type for reading the tabular data:
```
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

```
You will use a for loop to iterate over the initial keys and values of the dictionary.

```
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

```

Define an empty list to hold the car inventory that you will read:
```
myInventoryList = []

```

#### Copying the CSV file into memory
You will read in the data from disk (hard drive) and make an in-memory (random access memory, or RAM) copy. 
In a computer, a hard drive stores data long term, including when the power is turned off. RAM refers to temporary memory that is faster, but it is erased when the computer's power is turned off.

The `with open` syntax statement, keeps a file open while you read data. It will automatically close the CSV file when the code inside the with block is finished running.

`csv.reader()` is a function that you are using from the csv library that you imported with the import csv statement.

```
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
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

```

#### Printing the car inventory

```
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")

```

