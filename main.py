s = "Hello, Python!"

# Slice string from index 0 to index 5 (exclusive)
s2 = s[0:5]

print(s2)

# Get the entire string
s3 = s[:]
s4 = s[::]

print(s3)
print(s4)

# Characters from index 7 to the end
print(s[7:])

# Characters from the start up to index 5 (exclusive)
print(s[:5])

# Characters from index 1 to index 5 (excluding 5)
print(s[1:5]) 

# Overwrite value stored in variable s
s = "abcdefghi"

# Every second character
print(s[::2])

# Every third character from index 1 to 8 (exclusive)
print(s[1:8:3]) 

# Overwrite value stored in variable s
s = "abcdefghijklmno"

# Characters from index -4 to the end
print(s[-4:])

# Characters from the start up to index -3 (excluding -3)
print(s[:-3])

# Characters from index -5 to -2 (excluding -2)
print(s[-5:-2])

# Get every 2nd elements from index -8 to -1 (excluding index -1)
print(s[-8:-1:2])

# Overwrite value stored in variable s
s = "Python"

# Reverse the string
print(s[::-1])