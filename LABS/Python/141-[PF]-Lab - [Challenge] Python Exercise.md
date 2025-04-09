# Python Script to Find and Store Prime Numbers (1-250)

## Solution Code

```python
#!/usr/bin/env python3
"""
Prime Number Generator
Finds all prime numbers between 1 and 250 and stores them in results.txt
"""

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start, end):
    """Generate list of primes in given range"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def save_primes(primes, filename):
    """Save primes to a text file"""
    with open(filename, 'w') as f:
        f.write("\n".join(map(str, primes)))
        f.write("\n")  # Add final newline

def main():
    """Main execution function"""
    primes = find_primes(1, 250)
    save_primes(primes, "results.txt")
    print(f"Found {len(primes)} prime numbers between 1 and 250")
    print("Results saved to results.txt")

if __name__ == "__main__":
    main()
```

## How to Use This Script

1. Save the code as `prime_finder.py`
2. Make it executable:
   ```bash
   chmod +x prime_finder.py
   ```
3. Run the script:
   ```bash
   python3 prime_finder.py
   ```

## Expected Output in results.txt

```
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
211
223
227
229
233
239
241
```

## Key Features

1. **Efficient Prime Checking**: Uses the 6k ± 1 optimization
2. **Modular Design**: Separate functions for prime checking, generation, and file I/O
3. **Proper File Handling**: Ensures file is properly closed after writing
4. **User Feedback**: Prints status messages to console
5. **Shebang Line**: Allows direct execution in Unix-like systems

## Verification Steps

1. Check the output file exists:
   ```bash
   ls -l results.txt
   ```

2. Count the number of primes found (should be 53):
   ```bash
   wc -l results.txt
   ```

3. Verify the last prime is 241:
   ```bash
   tail -1 results.txt
   ```

## Alternative Implementation (More Concise)

For those preferring a more compact solution:

```python
#!/usr/bin/env python3
with open('results.txt', 'w') as f:
    f.write('\n'.join(str(n) for n in range(2,250) if all(n%i for i in range(2,int(n**0.5)+1))))
```

This minimalist version provides the same functionality in fewer lines, though it's less readable and maintainable. The first implementation is recommended for production use.