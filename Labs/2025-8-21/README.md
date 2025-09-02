# 🧪 Week 1: Shell + Python Workflow Recap Assignment

## 📦 Provided Files

You will receive a `.zip` file containing the following three files:

```
20250821_lab/
├── confusing_function.py
├── is_prime.py
└── generate_files.sh
```

---

## 🎯 Objectives

This assignment helps you:

- Practice basic Unix shell commands
- Execute Python scripts using the terminal
- Modify existing Python and shell scripts
- Develop confidence in organizing code and output files
- Begin reasoning about code correctness and functionality
- Practice explaining your work in plain English

---

## 🛠️ What You Must Do

### ✅ 1. Fix `is_prime.py`

- This script contains **syntax and logic errors**.
- Your task is to **debug and correct** the function so it properly checks whether a number is prime.
- Run the script using:

```bash
python is_prime.py
```

- Ensure the output matches the expected results in the comments.
- **Do NOT use any external libraries**. Only basic Python is allowed.

---

### ✅ 2. Modify `generate_files.sh`

Currently, this script:

- Creates files with different extensions (`.txt`, `.md`, `.csv`, `.tsv`, `.rtf`)
- Uses numbers `0` to `9` as filename indices

Your tasks:

- Modify the script so it creates two subdirectories:
  - `even_files/` → for files with even index numbers (0, 2, 4, 6, 8)
  - `odd_files/` → for files with odd index numbers (1, 3, 5, 7, 9)
- When the script is run:
  - All generated files should be **moved** into the correct subdirectory based on their number

Run it using:

```bash
bash generate_files.sh
```

Example:
```
even_files/file_0.txt
odd_files/file_1.md
```

---

### ✅ 3. Understand and Explain

You will meet with a TA during lab to:

- **Show the output of your scripts**
- **Explain in plain English what your code does** (both Python and shell)
- **Walk through your changes and reasoning**

This will help you practice **code communication** and **clarity of understanding**, which are essential to scientific programming.

---

## 📊 Rubric: Based on Student Learning Outcomes (SLOs)

| **SLO Component** | **Criteria** | **Max Points** |
|------------------|--------------|----------------|
| **1.1 Problem-Solving Approach** | Effective use of shell commands to automate, navigate, and structure work | 4 |
| **1.2 Code/Pseudocode Quality** | Code and script structure is logical, modular, and easy to follow | 4 |
| **2.1 Correctness / Functionality** | Files behave as expected; outputs are correct; edge cases handled | 4 |
| **2.2 Efficiency / Optimization** | Uses concise shell and Python constructs; no unnecessary repetition | 4 |
| **3.1 Documentation / Clarity** | Code is commented or self-explanatory; student provides a clear verbal explanation | 4 |
| **3.2 Error Handling / Debugging** | Syntax and logic errors are fixed correctly; uses appropriate testing | 4 |

**Total: 24 points**

**Grading Scale:**

- 20–24 points: ✅ Exemplary
- 15–19 points: ✅ Proficient
- 10–14 points: ⚠️ Needs Improvement
- 6–9 points: ❌ Unsatisfactory
- 0-6: Fail to complete any objective or could not explain the programming in plain English

---

## 📅 Submission & Evaluation

You will demonstrate your work **during class**. The TA will take notes and grade you **after class** using the rubric above.

---

If you have questions, reach out via email or ask in class. This exercise sets the foundation for everything we’ll build going forward!
