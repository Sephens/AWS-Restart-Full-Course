# Working with Lists, Tuples, and Dictionaries - Lab Explanation

## Lab Overview
This lab focuses on three fundamental Python collection data types:
1. **Lists** - Mutable, ordered collections
2. **Tuples** - Immutable, ordered collections
3. **Dictionaries** - Mutable, unordered key-value pairs

## Exercise 1: Working with Lists

### Defining a List
Lists are created using square brackets `[]` and can contain mixed data types.

**Code:**
```python
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
```

**Explanation:**
- Creates a list containing three string elements
- `print(myFruitList)` outputs the entire list: `['apple', 'banana', 'cherry']`
- `type(myFruitList)` confirms it's a list: `<class 'list'>`

**Example Output:**
```
['apple', 'banana', 'cherry']
<class 'list'>
```

### Accessing List Elements by Position
Python uses zero-based indexing to access list elements.

**Code:**
```python
print(myFruitList[0])  # First element
print(myFruitList[1])  # Second element
print(myFruitList[2])  # Third element
```

**Explanation:**
- Index `0` accesses the first element ("apple")
- Index `1` accesses the second element ("banana")
- Index `2` accesses the third element ("cherry")

**Example Output:**
```
apple
banana
cherry
```

### Modifying List Elements
Lists are mutable, meaning their elements can be changed after creation.

**Code:**
```python
myFruitList[2] = "orange"  # Change third element
print(myFruitList)
```

**Explanation:**
- Changes the element at index 2 from "cherry" to "orange"
- Prints the modified list

**Example Output:**
```
['apple', 'banana', 'orange']
```

**Common Question:**  
*What happens if I try to access an index that doesn't exist?*  
Answer: Python raises an `IndexError`. For example, `myFruitList[3]` would fail because our list only has indices 0-2.

## Exercise 2: Working with Tuples

### Defining a Tuple
Tuples are immutable collections defined with parentheses `()`.

**Code:**
```python
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
```

**Explanation:**
- Creates a tuple with three elements
- Tuples cannot be modified after creation (immutable)
- `type()` confirms it's a tuple

**Example Output:**
```
('apple', 'banana', 'pineapple')
<class 'tuple'>
```

### Accessing Tuple Elements
Like lists, tuples use zero-based indexing.

**Code:**
```python
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
```

**Example Output:**
```
apple
banana
pineapple
```

**Important Note:**  
Attempting to modify a tuple like `myFinalAnswerTuple[0] = "pear"` would raise a `TypeError` because tuples are immutable.

**Common Question:**  
*When should I use a tuple instead of a list?*  
Answer: Use tuples when:
- You need to ensure data integrity (can't be changed)
- Working with constant data
- Using as dictionary keys (lists can't be dictionary keys)
- Generally faster than lists for iteration

## Exercise 3: Working with Dictionaries

### Defining a Dictionary
Dictionaries store key-value pairs in curly braces `{}`.

**Code:**
```python
myFavoriteFruitDictionary = {
  "Akua": "apple",
  "Saanvi": "banana",
  "Paulo": "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
```

**Explanation:**
- Creates a dictionary mapping names to favorite fruits
- Each entry consists of a key (name) and value (fruit)
- Keys must be unique and immutable (strings, numbers, or tuples)
- Values can be any data type

**Example Output:**
```
{'Akua': 'apple', 'Saanvi': 'banana', 'Paulo': 'pineapple'}
<class 'dict'>
```

### Accessing Dictionary Values
Values are accessed using their keys in square brackets.

**Code:**
```python
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
```

**Explanation:**
- Retrieves the value associated with each key
- Much more readable than numeric indices when data has natural labels

**Example Output:**
```
apple
banana
pineapple
```

**Common Question:**  
*What happens if I try to access a key that doesn't exist?*  
Answer: Python raises a `KeyError`. You can use `.get()` method to avoid this:
```python
print(myFavoriteFruitDictionary.get("Maria", "No favorite fruit recorded"))
```

### Modifying Dictionaries
Unlike tuples, dictionaries are mutable.

**Example of Modification:**
```python
myFavoriteFruitDictionary["Maria"] = "mango"  # Add new entry
myFavoriteFruitDictionary["Akua"] = "pear"    # Modify existing entry
```

## Summary of Key Differences

| Feature        | List            | Tuple           | Dictionary          |
|---------------|----------------|----------------|--------------------|
| Syntax        | `[]`           | `()`           | `{}` with key:value |
| Mutable       | Yes            | No             | Yes (values only)   |
| Ordered       | Yes            | Yes            | No (Python 3.7+: insertion order preserved) |
| Indexing      | Numeric        | Numeric        | Key-based          |
| Use Case      | Mutable sequences | Immutable sequences | Key-value mappings |

## Additional Notes

### List Methods to Explore:
- `.append()` - Add item to end
- `.insert()` - Insert at specific position
- `.remove()` - Remove first matching value
- `.pop()` - Remove item at index

### Dictionary Methods to Explore:
- `.keys()` - Get all keys
- `.values()` - Get all values
- `.items()` - Get key-value pairs
- `.update()` - Merge dictionaries

### Real-world Applications:
- **Lists**: Shopping items, to-do tasks, sequence of operations
- **Tuples**: GPS coordinates, database records (where immutability is desired)
- **Dictionaries**: User profiles, configuration settings, word counters

This comprehensive explanation covers all steps in the lab while providing additional context and examples to enhance understanding of Python's collection data types.