# <--------------Lists----------->

# ---List items are ordered, changeable(mutable), and allow duplicate values.
# ---List items are indexed, the first item has index [0], the second item has index [1]
thislist=["apple", "banana", "cherry"]
print(thislist)

# Lists allow duplicate values:
thislist=["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length
thislist=["apple", "banana", "cherry"]
print(len(thislist))

# List Items - Data Types--String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

# type()
thislist=["apple", "banana", "cherry"]
print(type(thislist))

# The list() Constructor
thislist=list(("apple", "banana", "cherry"))
print(thislist)

# <----------Access List Items------------>
thislist=["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
thislist=["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

# Range of Negative Indexes
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# <---------Change List Items------------>
# Change Item Value
thislist=["apple", "banana", "cherry"]
thislist[1]='blackcurrant'
print(thislist)

# Change a Range of Item Values
thislist=["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3]=['blackcurrant', "watermelon"]
print(thislist)
# Change the second value by replacing it with two new values
thislist=["apple", "banana", "cherry"]
thislist[1:2]=['blackcurrant', "watermelon"]
print(thislist)
# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Items
thislist=["apple", "banana", "cherry"]
thislist.insert(2,'watermelon')
print(thislist)

thislist=["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# <---------------Add List Items-------------->
# Append Items
thislist=["apple", "banana", "cherry"]
thislist.append('Orange')
print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# <----------------Remove List Items------------------>
# Remove Specified Item
thislist=["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist=["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index--pop()
thislist=["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# not specify the index, the pop() method removes the last item.
thislist=["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Delete Specified Index
thislist=["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist=["apple", "banana", "cherry"]
del thislist
# print(thislist)

# Clear the List
thislist=["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# <-------------- Loop Lists------------->
# Loop Through a List
thislist1=["apple", "banana", "cherry"]
for x in thislist1:
  print(x)

# Loop Through the Index Numbers--range() and len()
thislist=["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist=["apple", "banana", "cherry"]
thislist= len(thislist)
print(thislist)

# Using a While Loop
thislist=["Bmw", "Benz", "Audi"]
i=0
while i < len(thislist):
    print(thislist[i])
    i=i+1

# <------------Sort Lists----------------->
# Sort List Alphanumerically
thislist=["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist=[100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending--reverse = True:
thislist=["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist=[100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Case Insensitive Sort
thislist=["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist=["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
thislist=["Bmw", "Benz", "Audi"]
thislist.reverse()
print(thislist)

# <-------------Copy Lists--------------->
# Copy a List
thislist=["apple", "banana", "cherry"]
mylist=thislist.copy()
print(mylist)

thislist=["mango", "grapes", "watermelon"]
mylist=list(thislist)
print(mylist)

# <------------Join Lists------------>
# Join Two Lists
# using the + operator.
list1=["a", "b", "c"]
list2=[1,2,3]

list3=list1 + list2
print(list3)

# using append
list1=["A", "B", "C"]
list2=[1,2,3]

for  x in list2:
    list1.append(x)
print(list1)

# using extend
list1=["m", "n", "o"]
list2=[7,8,6]

list1.extend(list2)
print(list1)