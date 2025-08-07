lst = [1,2,3,4,5]
print(lst)
print(type(lst))

# Bytes can not be modified
bt = bytes(lst)
print(bt)
print(type(bt))

# In bytes array values can be added
bta = bytearray(bt)
print(bta)
print(type(bta))
bta[3] = 40
print(bta)
print(type(bta))