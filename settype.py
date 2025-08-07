st = {1,2,2,3,4,5}
print(st)
print(type(st))

# Duplication, Slicing and index based operation can not be performed and set do not allow(will remove duplicate values) duplicate

# Functions
st.update([6])
print(st)
st.remove(6)
print(st)
st.add(6)
print(st)

# Frozen set
fst = frozenset(st) # it makes set immutable
print(fst)