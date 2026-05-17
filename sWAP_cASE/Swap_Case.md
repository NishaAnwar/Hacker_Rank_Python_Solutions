**Swap Case Problem**

**Problem Statement**

You are given a string and your task is to swap cases.

In other words:

Convert all lowercase letters to uppercase

Convert all uppercase letters to lowercase

📖 Example

Input:

Www.HackerRank.com

Pythonist 2

Output:

wWW.hACKERrANK.COM

pYTHONIST 2

**⚙️ Function Description**

**Function Name:**

swap_case

**Parameter:**

string s → the input string

**Returns:**
string → the modified string after swapping cases

**Input Format**

A single line containing a string s.

**⚠️ Constraints**
0 < len(s) ≤ 1000
💡 Idea / Logic

For each character in the string:

If it is lowercase → convert it to uppercase

If it is uppercase → convert it to lowercase

If it is not a letter (like space or symbol) → still handled automatically

🧾 Solution (Python Code)

```python
def swap_case(s):
    swaped = ""
    
    for i in range(len(s)):
        if s[i].islower():
            swaped += s[i].upper()
        else:
            swaped += s[i].lower()
    
    return swaped


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)```
    
🚀 Key Takeaway

This problem is solved by checking each character and toggling its case using .islower() and .upper() / .lower() methods.
