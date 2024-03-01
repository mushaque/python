# <---------------Data Types------------->

# Getting the Data Type------type()
x=5
print(type(x))
x = "Hello World"
print(type(x))
x = 20.5
print(type(x))
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))
x = True
print(type(x))


# <-----------------------Numbers---------------------->
# Int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion---convert from one type to another
x = 1   
y = 2.8  
z = 1j   

x=float(1)
y=int(2.8)
z=complex(1)

print(x)
print(y)
print(z)


print(type(x))
print(type(y))
print(type(z))

#Random Number
import random
print(random.randrange(1, 10))

# ----------- Casting------------
# Integers:
x = int(1)
y = int(2.8)
z = int("3")

print(x)
print(y)
print(z)
# Floats:
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

print(x)
print(y)
print(z)
print(w)
# Strings:
x = str("s1")
y = str(2)
z = str(3.0)

print(x)
print(y)
print(z)
