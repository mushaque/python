# ------------Tuples----------->
# ---Tuple  items are ordered, Unchangeable( immutable ), and allow duplicate values.
# ---Tuple  items are indexed, the first item has index [0], the second item has index [1]
thistuple=("apple", "banana", "cherry")
print(thistuple)

# Tuples allow duplicate values:
thistuple=("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length:
thistuple=("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item
thistuple=('Bmw',)
print(type(thistuple))

# #NOT a tuple
thistuple=("Audi")
print(type(thistuple))

# Tuple Items - Data Types
tuple1=("apple", "banana", "cherry")
tuple2=(1, 5, 7, 9, 3)
tuple3=(True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

tuple1=("abc", 34, True, 40, "male")
print(tuple1)

# type()
mytuple=("apple", "banana", "cherry")
print(type(mytuple))

# <-------Access Tuple Items------------->

# Access Tuple Items
thistuple=("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
thistuple=("apple", "banana", "cherry")
print(thistuple[-1])

# Range of Indexes
thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Range of Negative Indexes
mytuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(mytuple[-4:-1])


#<---------Update Tuples----------->
# Change Tuple Values
# Convert the tuple into a list to be able to change it:
x=("Bmw","Audi","Benz")
y=list(x)
y[1]="Honda city"
x=tuple(y)
print(x)

# Convert into a list:
thistuple=("apple", "banana", "cherry")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)

# Add tuple to a tuple:
thistuple=("apple", "banana", "cherry")
y=("pineapple",)
thistuple= thistuple + y
print(thistuple)

# Remove Items
thistuple=('apple', 'banana', 'cherry', 'pineapple')
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)

# <-------------Unpack Tuples----------------->
# Unpacking a Tuple
fruits=("apple", "banana", "cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

# Using Asterisk*
# number of variables is less than the number of values, you can add an * to the variable name 
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green,*tropic,red)=fruits
print(green)
print(tropic)
print(red)


#<------------Loop Tuples---------->
# Loop Through a Tuple
thistuple=("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Loop Through the Index Numbers--range() and len()
thistuple=("Bmw", "Audi", "Benz")
for i in range(len(thistuple)):
  print(thistuple[i])

# Using a While Loop
thistuple=["car", "bus", "auto"]
i=0
while i < len(thistuple):
    print(thistuple[i])
    i=i+1

#-<-------------Join Tuples------------>
# Join Two Tuples

# using the + operator.
tuple1=["a", "b", "c"]
tuple2=[1,2,3]
tuple3=tuple1+tuple2
print(tuple3)

# Multiply Tuples
fruits=("apple", "banana", "cherry")
mytuple=fruits*2
print(mytuple)