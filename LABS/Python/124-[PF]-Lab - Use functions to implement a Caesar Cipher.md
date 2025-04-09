# Implementing a Caesar Cipher with Python Functions

## Lab Overview
This lab teaches how to create and use user-defined functions in Python by building a Caesar cipher - a classic encryption technique that shifts letters by a fixed number down the alphabet. You'll learn to:
- Create modular functions for specific tasks
- Encrypt and decrypt messages
- Implement program control flow
- Reuse functions for different purposes

## Exercise 1: Creating the Double Alphabet Function

```python
def getDoubleAlphabet(alphabet):
    """Doubles the alphabet string to handle large shifts"""
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
```

**Purpose**: Creates an extended alphabet (e.g., "ABC" → "ABCABC") to simplify shifting letters past 'Z'

**Key Concepts**:
- Function definition with `def`
- String concatenation with `+`
- Return statement

## Exercise 2: Getting User Message

```python
def getMessage():
    """Prompts user for message to encrypt"""
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
```

**Features**:
- Uses `input()` for user interaction
- Returns the raw message string
- No parameters needed

## Exercise 3: Getting Cipher Key

```python
def getCipherKey():
    """Gets encryption key from user (1-25)"""
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount
```

**Validation Note**: In a production app, you'd add validation:
```python
while True:
    try:
        shift = int(input("Enter key (1-25): "))
        if 1 <= shift <= 25:
            return shift
    except ValueError:
        print("Invalid input - please enter a number")
```

## Exercise 4: Message Encryption

```python
def encryptMessage(message, cipherKey, alphabet):
    """Encrypts message using Caesar cipher"""
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        if position >= 0:  # Character found in alphabet
            newPosition = position + int(cipherKey)
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter  # Keep non-alphabet chars
    
    return encryptedMessage
```

**Algorithm**:
1. Convert message to uppercase
2. For each character:
   - Find its position in the alphabet
   - Calculate new position with cipher key
   - Handle wrap-around using double alphabet
3. Preserve non-alphabetic characters

## Exercise 5: Message Decryption

```python
def decryptMessage(message, cipherKey, alphabet):
    """Decrypts message by reversing the cipher"""
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
```

**Clever Reuse**: Instead of rewriting the logic, we reuse `encryptMessage` with a negative key

## Exercise 6: Main Program Function

```python
def runCaesarCipherProgram():
    """Main function controlling cipher workflow"""
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    
    print("\n=== Caesar Cipher ===")
    myMessage = getMessage()
    myCipherKey = getCipherKey()
    
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f"\nEncrypted Message: {myEncryptedMessage}")
    
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f"Decrypted Message: {myDecryptedMessage}\n")

# Execute the program
runCaesarCipherProgram()
```

**Program Flow**:
1. Define alphabet
2. Get user inputs
3. Encrypt message
4. Decrypt message
5. Display results

## Enhanced Version with Improvements

```python
import string

def caesar_cipher(text, shift, direction='encrypt'):
    """
    Enhanced Caesar cipher that handles both encryption and decryption
    Args:
        text: str - message to process
        shift: int - number of positions to shift (1-25)
        direction: str - 'encrypt' or 'decrypt'
    Returns:
        str - processed message
    """
    if direction == 'decrypt':
        shift = -shift
    
    # Create translation table
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.lower(), 
                                    shifted_alphabet + shifted_alphabet.lower())
    
    return text.translate(translation_table)

def main():
    """Enhanced main function with input validation"""
    print("\n=== Enhanced Caesar Cipher ===")
    
    # Get user input with validation
    while True:
        try:
            message = input("Enter message: ")
            key = int(input("Enter shift key (1-25): "))
            if not 1 <= key <= 25:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please try again.")
    
    # Process and display
    encrypted = caesar_cipher(message, key, 'encrypt')
    decrypted = caesar_cipher(encrypted, key, 'decrypt')
    
    print(f"\nOriginal: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()
```

**Improvements**:
1. Single function handles both encryption/decryption
2. Uses Python's `str.maketrans()` for efficient translation
3. Preserves case (uppercase and lowercase)
4. Better input validation
5. Cleaner output formatting
6. Standard Python module (`string`) for alphabet
7. Pythonic `if __name__ == "__main__"` guard

## How the Cipher Works

For shift = 3:
```
Original:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Encrypted: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

**Example**:
- "HELLO" → "KHOOR" (encrypt with shift 3)
- "KHOOR" → "HELLO" (decrypt with shift 3)

## Security Considerations

While Caesar ciphers are:
- Great for learning programming concepts
- Simple to implement
- Useful for basic obfuscation

They are NOT secure for real encryption because:
1. Only 25 possible keys (easy to brute force)
2. Preserves letter frequency patterns
3. Vulnerable to known-plaintext attacks

For real security, use Python's built-in cryptographic libraries like `cryptography`.

## Further Enhancements

1. **File Encryption**:
```python
def encrypt_file(input_file, output_file, key):
    with open(input_file) as f:
        message = f.read()
    encrypted = caesar_cipher(message, key)
    with open(output_file, 'w') as f:
        f.write(encrypted)
```

2. **Frequency Analysis Defense**:
- Implement padding
- Add random characters
- Combine with other ciphers

3. **Command Line Interface**:
```python
import argparse

parser = argparse.ArgumentParser(description='Caesar Cipher')
parser.add_argument('message', help='Text to process')
parser.add_argument('key', type=int, help='Shift amount (1-25)')
parser.add_argument('--decrypt', action='store_true', help='Decrypt instead')
args = parser.parse_args()
```

This lab provides a solid foundation in function creation and string manipulation while introducing basic cryptographic concepts.