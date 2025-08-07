# Tuple is immutable no update, addition and deletion of element

tpl = (10,20,30, 30,40,50,60,70,80,90)
print(tpl)

# Indexing
print(tpl[0])

# Slicing work same as String for examples check stingtype.py

# Duplication
print(tpl * 3)

# Length same as String
print(len(tpl))

# Functions
print(tpl.count(20)) # Count the provided value repetitions
print(tpl.index(30)) # Find the index of provided value first appearance

# More tuple functions
print(min(tpl))
print(max(tpl))