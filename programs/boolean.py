# <----------------Booleans---------------->
# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

# A condition in an if statement

a=200
b=33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# valuate Values and Variables

print(bool("Hello"))
print(bool(15))

a=15
b="Hello"
print(bool(a))
print(bool(b))

# Most Values are True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
# Functions can Return a Boolean
def myfunction():
    return True
print(myfunction())

def myfun():
    return True
if myfun():
    print("Yes!")
else:
    print("No!")