#-----------Lists----------

# grocery_list = ['choclates','fruits','vegetables','choclates','choclates']
# quantity_list = [1,3,4,5]
# price_list = [0.5,6.3,7.2]

# print entire list

# print(grocery_list)

# print 1st two items

# print(grocery_list[:2])

# print 3rd item

# print(grocery_list[2])

#  grocery_list[2]='Carrots'



# grocery_list[4]='Water bottle'
# print(grocery_list[4])

# print entire list

# print(grocery_list)

# print length of list

# print(len(grocery_list))

# remove last item and assign to new variable

# last_item = grocery_list.pop()
# print(last_item)
# print(grocery_list,last_item)

# insert an item at any given place

# grocery_list.insert(2,'pens')
# print(grocery_list)

#add new item at end

# grocery_list.append('water bottle')
# print(grocery_list)

# remove a specific item

# grocery_list.remove('choclates')
# print(grocery_list)
# print(grocery_list.count('choclates'))

# newlist = ['a','e','i','o','u']

# # delete specific index itex
# del newlist[3]

# # delete entire list
# del newlist

# # clear items in a list
# newlist.clear()
# print(newlist)


#----------->Lists<-----------
grocery_list=['choclates','fruits','vegetables','choclates']
# quantity_list = [1,3,4,5]
# price_list = [0.5,6.3,7.2]

# print entire list
print(grocery_list)

# print 1st two items
print(grocery_list[:2])

# print 3rd item
print(grocery_list[2])
grocery_list[2]="Carrot"
print(grocery_list)

# print length of list
print(len(grocery_list))

#remove last item and assign to new variable
last_item=grocery_list.pop()
print(last_item,grocery_list)

grocery_list.pop(2)
print(grocery_list)

# insert an item at any given place
grocery_list.insert(2,"watermelon")
print(grocery_list)

#add new item at end
grocery_list.append("pens")
print(grocery_list)

# remove a specific item
# If there are more than one item with the specified value,
# the remove() method removes the first occurance:
grocery_list.remove("pens")
print(grocery_list)

# delete specific index itex
del grocery_list[3]
print(grocery_list)

# delete entire list
del  grocery_list

# clear items in a list
grocery_list.clear()
print( grocery_list)





# List,Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Allow Duplicates,Lists allow duplicate values:
thislist = ["apple", "banana", "cherry","apple","cherry"]
print(thislist)

# List Length,Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List Items - Data Types,String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# type(),what is the data type of a list?
thislist = ["apple", "banana", "cherry"]
print(type(thislist))

# Access Items,Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing,Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes,Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Change Item Value,Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1]="blackcurrant"
print(thislist)

# Change a Range of Item Values,Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
thislist[1:3]=["blackcurrant","watermelon"]
print(thislist)

# Insert Items,Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"watermelon")
print(thislist)

# Append Items,Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List,Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove Specified Item,Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index pop(),emove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
