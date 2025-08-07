dic = {1:"John", 2:"Smith"}
print(dic)

# Indexing
print(dic[1])

# Adding element
dic.update({3:"Bob"})
print(dic)

# Deleting element
del(dic[3]) # If the key doesn't exists it will give error
print(dic)

# Function
print(dic.keys()) # Get all keys
print(dic.values()) # Get all the values
print(dic.items()) # Print all the items

