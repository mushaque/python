# >---------Variables----------<
# Creating Variables

x=5
print(x)
y="Kanna"
print(y)

x=5
x="Khanna"
print(x)

# Casting
x=str(3)
y=int(3)
z=float(3)
print(x)
print(y)
print(z)

# Get the Type----type()
x='kanna'
print(x,type(x))
y=31
print(y,type(y))

# Case-Sensitive
a=90
A="Johnny"
print(a)
print(A)


#<---------Variable Names--------->
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#<------------Many Values to Multiple Variables---------->
x,y,z="Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#<-------------One Value to Multiple Variables------------>
x=y=z="Apple"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits=["apple", "banana", "cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

#<-----------Output Variables------------->
x="Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x=5
y=10
print(x+y)

x=5
y="Kanna"
print(x,y)


# <-----------Global Variables------------->
# variable outside of a function
x="programming?"

def myfunc():
    print("Python is " + x)
myfunc()

#  variable inside a function
x="awesome"

def myfunc():
    x="fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x)

# --------------The global Keyword----------------

def myfunc():
    global x
    x="great"
myfunc()
print("Python is " + x)


