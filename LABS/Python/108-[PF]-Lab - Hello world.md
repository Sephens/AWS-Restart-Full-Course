
# AWS Cloud9 Python Lab: Hello World and Environment Setup

## **Lab Overview**
This lab guides you through setting up a Python environment in **AWS Cloud9** and writing your first Python program (`Hello, World`).  
We will cover:
1. Accessing AWS Cloud9 IDE  
2. Creating a Python file  
3. Checking Python versions  
4. Writing and running a Python script  

---

## **Step 1: Accessing AWS Cloud9**
### **Actions:**
1. Log in to the **AWS Management Console**.
2. Navigate to **Services > Cloud9**.
3. Locate the `reStart-python-cloud9` environment and click **Open IDE**.

### **Notes:**
- If prompted with `.c9/project.settings have been changed on disk`, select **Discard**.
- If asked to **Show third-party content**, choose **No** for security.

### **Why This Matters:**
- AWS Cloud9 is a cloud-based **Integrated Development Environment (IDE)**.  
- It comes preconfigured with Python, eliminating manual setup.  

---

## **Step 2: Creating a Python File**
### **Actions:**
1. In the Cloud9 menu bar, go to **File > New From Template > Python File**.
   - A new untitled file opens with sample code (if any).
2. **Delete the template code** (we’ll write our own).
3. Save the file:  
   - **File > Save As...**  
   - Name: `hello-world.py`  
   - Location: `/home/ec2-user/environment`  

### **Notes:**
- The `/home/ec2-user/environment` directory is the **default workspace** in Cloud9.  
- `.py` extension tells the system this is a **Python script**.  

---

## **Step 3: Understanding Python Versions**
### **Actions:**
Run these commands in the **Cloud9 terminal** (bottom pane):  
```bash
python --version    # Checks default Python version
python2 --version   # Checks Python 2.x (if installed)
python3 --version   # Checks Python 3.x
```
**Example Output:**  
```
Python 3.6.12   # Default (Python 3)
Python 2.7.18   # Legacy Python 2
Python 3.6.12   # Explicit Python 3
```

### **Key Concepts:**
- **Python 2 vs. Python 3**:  
  - Python 2 is **legacy** (no longer supported since 2020).  
  - Python 3 is **modern** (used in this lab).  
- **Backward Compatibility**:  
  - Code written for Python 3 may **not** work in Python 2 (e.g., `print` syntax differs).  

---

## **Step 4: Writing the "Hello, World" Program**
### **Actions:**
1. Open `hello-world.py` in the editor.  
2. Type:  
   ```python
   print("Hello, World")
   ```
3. Save the file (**Ctrl+S** or **File > Save**).  

### **Running the Program:**
1. Click the **Run button (▶)** in the top menu.  
2. Output appears in the terminal:  
   ```
   Hello, World
   ```

### **Explanation:**
- `print()` is a **built-in function** that displays text.  
- Strings (text) must be enclosed in **quotes** (`" "` or `' '`).  

---

## **Step 5: Debugging Common Issues**
### **Problem 1: Syntax Error**
- **Example Mistake:**  
  ```python
  print(Hello, World)  # Missing quotes!
  ```
- **Error:**  
  ```
  NameError: name 'Hello' is not defined
  ```
- **Fix:**  
  ```python
  print("Hello, World")  # Correct
  ```

### **Problem 2: Wrong Python Version**
- If `python --version` shows **Python 2.x**, force Python 3 by running:  
  ```bash
  python3 hello-world.py
  ```

---

## **Additional Notes**
### **Q: Why Use Cloud9 Instead of Local Python?**
- **Preconfigured Environment**: No need to install Python/packages.  
- **Accessible Anywhere**: Work from any device with a browser.  

### **Q: How to Exit Cloud9?**
- Simply close the browser tab. Your work is **auto-saved**.  

---

## **Conclusion**
You’ve successfully:  
✅ Set up AWS Cloud9  
✅ Created a Python file  
✅ Verified Python versions  
✅ Written and executed a `Hello, World` program  

Next: Explore more Python basics like variables, loops, and functions!  


---

### **Key Features of This Guide:**
1. **Step-by-Step Instructions**: No steps skipped.  
2. **Troubleshooting**: Common errors and fixes.  
3. **Theoretical Explanations**: Why each step matters.  
4. **Q&A**: Anticipates learner questions.  
