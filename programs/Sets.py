# <-------Sets----------->

# Set---A set is a collection which is unordered, unchangeable, and unindexed,duplicates Not Allowed.
thisset={"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed:
thisset={"apple", "banana", "cherry","apple"}
print(thisset)

thisset={"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset={"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Get the Length of a Set:
thisset={"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# <--------Access Set Items-------->
thisset={"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#--------Add Items------->
thisset={"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# Add Sets---update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable
thisset={"apple", "banana", "cherry"}
tropical=["Bmw","Benz","Audi"]
thisset.update(tropical)
print(thisset)

# <-------Remove Set Items------>

# Remove Item---remove(), discard(),pop(),clear(),delete()

# remove()
#  If the item to remove does not exist, remove() will raise an error.
thisset={"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# discard()
# If the item to remove does not exist, discard() will NOT raise an error.
thisset={"apple", "banana", "cherry"}
thisset.discard("cherry")
print(thisset)

# pop()
thisset={"cricket","football","badminton"}
thisset.pop()
print(thisset)

# clear()
thisset={"car","jeep","auto"}
thisset.clear()
print(thisset)

# delete
thisset={"Ball","Pen","Paper"}
del thisset
# print(thisset)

# ---- Loop Sets----->
# Loop Items
thisset={"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# <-----Join Sets----->
# Join Two Sets---union()
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

# update()
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)

# Keep ONLY the Duplicates
# intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

# intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "banana"}
z=x.intersection(y)
print(z)

# Keep All, But NOT the Duplicates
# symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)

# symmetric_difference()
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "banana"}
c=a.symmetric_difference(b)
print(c)