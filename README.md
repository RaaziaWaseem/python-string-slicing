# Python String Slicing Examples

This project demonstrates various string slicing techniques in Python. String slicing allows you to extract parts of a string using specific patterns of indices. 

## Features
- Slicing strings using index ranges and steps.
- Extracting substrings from the beginning, middle, and end of strings.
- Reversing strings using slicing.

## Code Overview

The code demonstrates the following types of string slicing:
1. **Basic Slicing**: Extract a portion of the string from a start index to an end index.
2. **Full String Extraction**: Extract the entire string using slicing.
3. **From Specific Index to End**: Extract characters starting from a specific index up to the end.
4. **From Start to Specific Index**: Extract characters from the start up to a specific index.
5. **Using Step**: Extract every nth character from a string.
6. **Negative Indexing**: Using negative indices to slice from the end of the string.
7. **Reversing a String**: Reverse a string using slicing.

## Example Code

```python
s = "Hello, Python!"

# Slice string from index 0 to index 5 (exclusive)
s2 = s[0:5]
print(s2)  # Output: Hello

# Get the entire string
s3 = s[:]
s4 = s[::]
print(s3)  # Output: Hello, Python!
print(s4)  # Output: Hello, Python!

# Characters from index 7 to the end
print(s[7:])  # Output: Python!

# Characters from the start up to index 5 (exclusive)
print(s[:5])  # Output: Hello

# Characters from index 1 to index 5 (excluding 5)
print(s[1:5])  # Output: ello

# Overwrite value stored in variable s
s = "abcdefghi"

# Every second character
print(s[::2])  # Output: acegi

# Every third character from index 1 to 8 (exclusive)
print(s[1:8:3])  # Output: bdf

# Overwrite value stored in variable s
s = "abcdefghijklmno"

# Characters from index -4 to the end
print(s[-4:])  # Output: lmn

# Characters from the start up to index -3 (excluding -3)
print(s[:-3])  # Output:abcdefghijk

# Characters from index -5 to -2 (excluding -2)
print(s[-5:-2])  # Output: lmn

# Get every 2nd elements from index -8 to -1 (excluding index -1)
print(s[-8:-1:2])  # Output: hln

# Overwrite value stored in variable s
s = "Python"

# Reverse the string
print(s[::-1])  # Output: nohtyP