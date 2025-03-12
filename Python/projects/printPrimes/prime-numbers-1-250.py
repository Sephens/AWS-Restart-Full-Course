def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Other even numbers are not prime

    # Check for factors from 3 to the square root of n (only odd numbers)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime


with open("printPrimes/prime-numbers.txt", "w") as file:
    file.write("Prime numbers between 1-250: \n")
    for x in range(1, 251):  # Loop through numbers 1 to 250
        if is_prime(x):  # Check if the number is prime
            file.write(f"{x} ")  # Write the prime number to the file
            print(x, end=" ")

print("\n Prime numbers have been written to 'prime-numbers.txt'.")
