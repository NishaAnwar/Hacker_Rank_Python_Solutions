# **Split and Join Problem**

## **Problem Description**

You are given a string `line`. Your task is to:

- Split the string into words  
- Join the words using a hyphen (`-`)  
- Return the resulting string  

---

## **Function Description**

### **Function Name:**
`split_and_join`

### **Parameter:**
- `line` (string): Input string containing words separated by spaces

### **Returns:**
- A single string where words are joined using `-`

---

## **Solution Approach**

The approach used here is:

- Split the string into a list of words using `split()`
- Manually iterate over the list
- Build a new string by adding `-` between words

---

## **Python Code**

```python
def split_and_join(line):
    splited_line=line.split()
    joined_string=""
    for i in range(len(splited_line)):
        joined_string+=splited_line[i]
        if i<len(splited_line)-1:
            joined_string+='-'
    return joined_string
