s = "You are awesome"
print(s)

s1 = """Yor
are
awesome"""
print(s1)

#Indexing - Index start from Zero
print(s[0])
print(s[2])

# Length function to calculate string length
print(len(s)) # Find length of string

# Duplicate string
print(s * 3) # Multiply the string by itself in resulting the duplication

# Sting Slicing
print(s[1:11]) #It excludes the mention end index [Start Index: End Index]
print(s[0:]) # Excluding end index will cover the string till end
print(s[:8]) # Excluding start index will strat from Zero index till mentioned end index
print(s[-3:-1]) # Will cover the string -3 to -1 last index is -1

# String Step Slicing
print(s[0:8:2]) # Will pick every second element
print(s[15::-1]) # Start index(Which is end index in linear format) to not mention end index with -1 skip will print string in reverse
print(s[::-1]) # Will print the string in reverse as no end and start index mention only the skip order mention which is -1 means cover every element in reverse

# String strip for space
s = " You are awesome "
print(s.strip()) # Will remove leading and trailing spaces
print(s.lstrip()) # Will remove spaces from left side of string
print(s.rstrip()) # Will remove spaces from right side of string

# String casing
s = "You are awesome"
print(s.upper()) # All uppercase
print(s.lower()) # All lowercase
print(s.capitalize()) # First letter capital of every word