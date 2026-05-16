"""For the below problem use python2 because the built-in hash() function in Python 3 uses a random 
salt by default for security, meaning it produces a different value every time the program runs.HackerRank’s 
expected outputs for this specific challenge were generated using Python 2's deterministic hashing. """

# 013 - Tuples
## Problem

### Task

Given an integer, `n`, and `n` space-separated integers as input, create a tuple, `t`, of those `n` integers. Then compute and print the result of `hash(t)`.

**Note**: `hash()` is one of the functions in the `__builtins__` module, so it need not be imported.


### Input Format

The first line contains as integer, `n`, denoting the number of elements in the tuple.

The second line contains `n` space-separated integers describing the elements in tuple `t`.


### Output Format

Print the result of `hash(t)`.


**Sample Input 0**

```
2
1 2
```

**Sample Output 0**

```
3713081631934410656
```


<br>

## Solution


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple((integer_list))))
