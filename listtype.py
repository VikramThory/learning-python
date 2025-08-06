lst = [10, 20, "Vikram", -30, 87.5]
print(type(lst))
print(lst)

# Indexing
print(lst[0])

# Slicing
print(lst[1:4]) # Work same as String for example check stringtype.py

# Duplication
print(lst*3)

# Length same as String
print(len(lst))

# List function
lst.append(40) # add element in last
lst.remove("Vikram") # remove mentioned element if not found gives error
lst.insert(2, 50) # add element to a specific index
print(lst)

# lst.clear()

lst.sort() # sort in asc order
print(lst)
lst.sort(reverse=True)
print(lst) # sort in reverse order

# More list functions
min(lst)
max(lst)
del(lst[0])
print(lst)

