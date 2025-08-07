a=10
b=10
print(a is b) # if true means using same memory location just referencing to it and it will be true

# Check memory location
# id function provides the memory location
print(id(a)==id(b)) # True in this case
print(id(a))
print(id(b))

b = 5
# Check memory location
print(id(a)==id(b)) # False in this case
print(id(a))
print(id(b))