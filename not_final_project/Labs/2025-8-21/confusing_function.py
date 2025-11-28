"""
confusing_function.py

This script contains a broken function intended to produce the output 42
when called with input 0 — but due to a series of logic errors and syntactic mistakes,
it does not work as intended.

Your Task:
- Read and understand the current implementation.
- Fix the syntax and logic errors.
- Ensure that the function returns 42 when input is 0.
- Run the script via the shell using: python confusing_function.py

Remember: Do NOT change the expected input/output behavior — just fix what's broken.
"""

def confusing_function(input_value):
    output_value = input_value  # Invalid syntax
    output_value += 1
    output_value += 2
    output_value += 1             # Likely meant: output_value = -1
    output_value += 4
    output_value -= 5              # Overwrites all previous steps
    output_value += 8 # I want this number to be 11
    output_value *= 3
    output_value += 9             # Comparison operator used instead of assignment
    return output_value


print(confusing_function(0))      # Expected output: 42
