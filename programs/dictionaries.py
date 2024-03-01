# Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict) 

# Dictionary Items
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict['brand'])

# Duplicates Not Allowed
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "year":2020
}
print(thisdict)

# Dictionary Length
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(len(thisdict))

# Dictionary Items - Data Types
thisdict={
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# type()
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(type(thisdict))

# <------------Access Dictionary Items----------->
# Accessing Items
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=thisdict['model']
print(x)

# get()
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=thisdict.get('brand')
print(x)

# Get Keys and Get Values
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=thisdict.keys()
y=thisdict.values()
print(x)
print(y)

#  new item to the original dictionary,see that the keys gets updated as well:
car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=car.keys()
y=car.values()
print(x) #before the change
print(y) #before the change

car['color']="white"
print(x)#after the change
print(y) #after the change

# Get Items--items()
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=thisdict.items()
print(x)

# change in the original dictionary, and see that the items list gets updated as well:
car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=car.items()
print(x)#before the change
car["year"]=2020
print(x)#after the change


car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=car.items()
print(x) #before the change
car['color']='red'
print(x)#after the change

# Change Values
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict['year']=2024
print(thisdict)

# Update Dictionary--update()
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict.update({"year":2018})
print(thisdict)

# Adding Items
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict["color"]="red"
print(thisdict)

# Update Dictionary
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color":"Green"
}
mydict.update({"color": "yellow"})

print(mydict)

# <-----Remove Dictionary Items------->
# Removing Items
# pop() 
mydict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict.pop('model')
print(mydict)

# popitem() method removes the last inserted item
thisdict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "yellow"
}
thisdict.popitem()
print(thisdict)

# delete--del
mydict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict['model']
print(thisdict)

# clear()
thisdict1={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.clear()
print(thisdict1)


# <-----Loop Dictionaries----->
# all key names in the dictionary,one by one:
thisdict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
 print(x)
# keys()
 thisdict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
 print(x)

# all values in the dictionary, one by one:
mydict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in mydict:
    print(mydict[x])
# using values()
thisdict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
    print(x)

# items()
mydict={
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x,y in mydict.items():
    print(x,y)