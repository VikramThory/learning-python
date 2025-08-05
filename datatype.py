amount = 100
tax = 0.06
total = amount + amount * tax
print(total)

int_total = int(total)
print(int_total)

float_total = float(total)
print(float_total)

name = 'Vikram'
print(name)
name = "Vikram Singh"
print(name)

name = input('What is your name?')
greeting = 'Hello ' + name
print(greeting)

a = 1
b = 1.0
print(type(a))
print(type(b))

c = 'String'
print(type(c))

d = 3 + 4j
print(type(d))

e = True # False
print(type(e))

f = 0B1010 # Binary
print(type(f))

g = 0XAF23 #Hexadecimal
print(type(g))

h = 0O234 #Octal
print(type(h))