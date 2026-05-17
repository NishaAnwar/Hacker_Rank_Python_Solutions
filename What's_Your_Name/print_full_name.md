# Print Full Name Problem

## Problem Description

You are given the firstname and lastname of a person on two different lines.  
Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

---

## Function Description

Complete the `print_full_name` function in the editor below.

### Function Name:
`print_full_name`

### Parameters:
- `string first`: the first name  
- `string last`: the last name  

### Output:
Print a single string in the format:

Hello firstname lastname! You just delved into python.

---

## Input Format

- The first line contains the first name  
- The second line contains the last name  

---

## Constraints

- Length of first and last names is ≤ 10

---

## Sample Input
Ross
Taylor


---

## Sample Output
Hello Ross Taylor! You just delved into python.



---

## Explanation

The input values are stored as strings and then formatted into the required output string using string formatting.

---

## Python Code

```python
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
