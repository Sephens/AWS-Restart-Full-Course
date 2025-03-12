# **Caesar Cipher Encryption and Decryption Project**

---

This project demonstrates the implementation of the Caesar Cipher, a classic encryption technique used to secure messages by shifting letters in the alphabet by a fixed number of positions. The project includes functions to double the alphabet, request user input for the message and cipher key, encrypt the message, and decrypt the message. This implementation is designed to handle uppercase letters and non-alphabet characters gracefully.

---

## **Table of Contents**
- [**Caesar Cipher Encryption and Decryption Project**](#caesar-cipher-encryption-and-decryption-project)
  - [**Table of Contents**](#table-of-contents)
  - [**1. Introduction**](#1-introduction)
  - [**2. Functions Overview**](#2-functions-overview)
    - [**2.1 getDoubleAlphabet**](#21-getdoublealphabet)
    - [**2.2 getMessage**](#22-getmessage)
    - [**2.3 getCipherKey**](#23-getcipherkey)
    - [**2.4 encryptMessage**](#24-encryptmessage)
    - [**2.5 decryptMessage**](#25-decryptmessage)
    - [**2.6 runCaesarCipherProgram**](#26-runcaesarcipherprogram)
  - [**3. How the Caesar Cipher Works**](#3-how-the-caesar-cipher-works)
  - [**4. Code Implementation**](#4-code-implementation)
  - [**5. Conclusion**](#5-conclusion)
    - [**Key Takeaways:**](#key-takeaways)

---

## **1. Introduction**

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down or up the alphabet. For example, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on. This project provides a Python implementation of the Caesar Cipher, including functions for encryption, decryption, and user interaction.

---

## **2. Functions Overview**

### **2.1 getDoubleAlphabet**

This function takes a string (the alphabet) and concatenates it with itself to create a doubled alphabet. This is useful for handling shifts that go beyond the end of the alphabet.

```python
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
```

### **2.2 getMessage**

This function prompts the user to enter a message to encrypt.

```python
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
```

### **2.3 getCipherKey**

This function prompts the user to enter a cipher key (a whole number between 1 and 25).

```python
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount
```

### **2.4 encryptMessage**

This function encrypts the message using the Caesar Cipher technique. It shifts each letter in the message by the cipher key and handles non-alphabet characters by leaving them unchanged.

```python
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
```

### **2.5 decryptMessage**

This function decrypts the message by reversing the encryption process. It uses the negative of the cipher key to shift the letters back to their original positions.

```python
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
```

### **2.6 runCaesarCipherProgram**

This function orchestrates the entire program. It defines the alphabet, doubles it, gets the message and cipher key from the user, encrypts the message, and then decrypts it.

```python
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')
```

---

## **3. How the Caesar Cipher Works**

The Caesar Cipher works by shifting each letter in the plaintext by a fixed number of positions down or up the alphabet. For example:

- With a shift of 3:
  - `A` → `D`
  - `B` → `E`
  - `C` → `F`
  - ...
  - `Z` → `C`

The doubled alphabet is used to handle shifts that go beyond `Z`. For example, if the shift is 3 and the letter is `X`, the new position will wrap around to the beginning of the alphabet.

---

## **4. Code Implementation**

Below is the complete implementation of the Caesar Cipher program:

```python
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()
```

---

## **5. Conclusion**

This project provides a complete implementation of the Caesar Cipher in Python. It includes functions for doubling the alphabet, encrypting and decrypting messages, and interacting with the user. The Caesar Cipher is a foundational concept in cryptography, and this project serves as a practical introduction to encryption techniques.

---

### **Key Takeaways:**
- The Caesar Cipher is a simple encryption technique that shifts letters by a fixed number of positions.
- The doubled alphabet ensures that shifts beyond `Z` wrap around to the beginning of the alphabet.
- Non-alphabet characters (e.g., spaces, punctuation) are left unchanged during encryption and decryption.
- This project demonstrates how to implement a basic encryption algorithm and interact with user input in Python.

---

This detailed markdown file provides a comprehensive explanation of the project, making it easy to understand and replicate.