"""
is_prime.py

This script contains a broken function intended to determine whether a number is prime.

Your Task:
- Identify and fix the syntax and logic errors in the `is_prime_number` function.
- Make sure the function returns True for prime numbers and False otherwise.
- Do not use external libraries — just basic Python.
- Run the script via the shell using: python is_prime.py
- Verify the correctness using the sample test cases provided below.

Tip: Read the error messages carefully and fix one issue at a time.
"""

def is_prime_number(n):
    prime = True

    if n <= 1:
        prime = False   # Assignment error — should assign to 'prime'

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:      # Missing colon
            prime = False
            break

    return prime        # Typo: variable not defined


# Sample test cases (expected outputs in comments)
print(is_prime_number(1))   # False
print(is_prime_number(3))   # True
print(is_prime_number(7))   # True
print(is_prime_number(8))   # False
print(is_prime_number(10))  # False
