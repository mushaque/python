#----->Tuples<--------
# Create a Tuple:
thistuple=("apple","banana","cherry")
print(thistuple)

# Allow Duplicates
# Tuples allow duplicate values:
thistuple=("apple","banana","cherry","apple","cherry")
print(thistuple)

# Tuple Length
# Print the number of items in the tuple:
thistuple=("apple","banana","cherry")
print(len(thistuple))

# Create Tuple With One Item
# One item tuple, remember the comma:
thistuple=("apple",)
print(type(thistuple))

#NOT a tuple
thistuple=("apple")
print(type(thistuple))

# Tuple Items - Data Types
# String, int and boolean data types:
tuple1=("apple","banana","cherry")
tuple2=(1,5,7,9,3)
tuple3=(True,False,False)
print(tuple1)
print(tuple2)
print(tuple3)

# A tuple with strings, integers and boolean values:
tuple1=("abc",34,True,40,"male")
print(tuple1)

# type()
# What is the data type of a tuple?
mytuple=("apple","banana","cherry")
print(type(mytuple))

# The tuple() Constructor
# Using the tuple() method to make a tuple:
thistuple=tuple(("apple","banana","cherry"))
print(thistuple)

# Access Tuple Items
# Print the second item in the tuple:
thistuple=("apple","banana","cherry")
print(thistuple[2])

# Negative Indexing
# Print the last item of the tuple:
thistuple=("apple","banana","cherry")
print(thistuple[-2])

# Range of Indexes
# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Change Tuple Values
# Convert the tuple into a list to be able to change it:
x=("apple","banana","cherry")
y=list(x)
y[1]="Kiwi"
x=tuple(y)
print(x)

# Add Items
# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple=("apple","banana","cherry")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)

# Create a new tuple with the value "orange", and add that tuple:
thistuple=("apple","banana","cherry")
y=("orange",)
thistuple+=y
print(thistuple)

# Remove Items
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple=("apple","banana","cherry")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

# Using Asterisk*
# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

# Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green,*tropic,red)=fruits
print(green)
print(tropic)
print(red)

# Loop Through a Tuple
# Iterate through the items and print the values:
thistuple=("apple","banana","cherry")
for x in thistuple:
    print(x)
    
# Loop Through the Index Numbers
#Print all items by referring to their index number:
thistuple=("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# Using a While Loop
# Print all items, using a while loop to go through all the index numbers:
thistuple=("apple","banana","cherry")
i=0
while  i < len(thistuple):
    print(thistuple[i])
    i=i+1
    
# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3=tuple1+tuple2
print(tuple3)

# Multiply Tuples
# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple=fruits*2
print(mytuple)