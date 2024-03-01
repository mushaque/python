# i = 1
# while i < 6:
#   print(i)
#   i=i+ 1
#   if i==9:
#   break

telephone_directory = {
    "A": {"name":"munna","phone": "9191919191", "address": "Hyderabad"},
    "B": {"name":"chinna","phone": "9292929292", "address": "Germany"},
    "C": {"name":"kanna","phone": "9393939393", "address": "France"},
    "D": {"name":"Bobby","phone": "9494949494", "address": "Spain"},
    "E": {"name":"Gandi","phone": "9595959595", "address": "Chennai"}
}

def starting_with(alphabet):
    for name, details in telephone_directory.items():
        if name.startswith(alphabet):
            print("name:", details["name"])
            print("phone:", details["phone"])
            print("address:", details["address"])
            

alphabet_input = input("Enter an alphabet: ")
starting_with(alphabet_input)


#--------->Dictionary<------------------
thisdict={"brand":"Ford","model":"Mustang","year":1964}
print(thisdict)

# Dictionary Items
thisdict={"brand":"Ford","model":"Mustang","year":1964}
print(thisdict["brand"])

# Duplicates Not Allowed
thisdict={"brand":"Ford","model":"Mustang","year":1964,"year":2002}
print(thisdict)

# Dictionary Length
print(len(thisdict))

# Dictionary Items - Data Types
thisdict1 = {"brand": "Ford","electric": False,"year": 1964,"colors": ["red", "white", "blue"]}
print(thisdict1)

# type()
print(type(thisdict1))

# The dict() Constructor
thisdict2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict2)

# Accessing Items
thisdict={"brand":"Ford","model":"Mustang","year":1964}
x=thisdict["model"]
print(x)

# using get
y=thisdict.get("year")
print(y)

# Get Keys
thisdict={"brand":"Ford","model":"Mustang","year":1964}
z=thisdict.keys()
print(z)

# new item to the original dictionary
car = {"brand": "Ford","model": "Mustang","year": 1964}
x=car.keys()
print(x)
car["colors"]="white"
print(x)
print(car)

# Get Values
thisdict={"brand":"Ford","model":"Mustang","year":1964}
x=thisdict.values()
print(x)

car = {"brand": "Ford","model": "Mustang","year": 1964}
x=car.values()
print(x)
car["year"]="2024"
print(x)

# new item to the original dictionary
car = {"brand": "Ford","model": "Mustang","year": 1964}
x=car.values()
print(x)
car["colors"]="red"
print(x)
print(car)

# Get Items
thisdict={"brand":"Ford","model":"Mustang","year":1964}
x=thisdict.items()
print(x)

# Change Values
thisdict={"brand":"Ford","model":"Mustang","year":1964}
thisdict["year"]="2018"
print(thisdict)

# Update Dictionary
thisdict={"brand":"Ford","model":"Mustang","year":1964}
thisdict.update({"year":2020})
print(thisdict)

# Adding Items
thisdict={"brand":"Ford","model":"Mustang","year":1964}
thisdict["color"]="Black"
print(thisdict)

# Removing Items
thisdict={"brand":"Ford","model":"Mustang","year":1964}
thisdict.pop("model")
print(thisdict)

# Loop Through a Dictionary
# Print all key names in the dictionary, one by one:
thisdict={"brand":"Ford","model":"Mustang","year":1964}
# for x in thisdict:
#     print(x)
for x in thisdict.keys():
    print(x)
# Print all values in the dictionary, one by one:
thisdict={"brand":"Ford","model":"Mustang","year":1964}

# # for x in thisdict: 
#  print(thisdict[x])
for x in thisdict.values():
    print(x)
    
# Loop through both keys and values, by using the items() method:
thisdict={"brand":"Ford","model":"Mustang","year":1964}
for x,y in thisdict.items():
    print(x,y)

# Nested Dictionaries
myfamily = {"child1" : {"name" : "Emil", "year" : 2004},"child2" : {"name" : "Tobias", "year" : 2007},"child3" : {"name" : "Linus","year" : 2011}}
print(myfamily)

# Access Items in Nested Dictionaries
myfamily = {"child1" : {"name" : "Emil", "year" : 2004},"child2" : {"name" : "Tobias", "year" : 2007},"child3" : {"name" : "Linus","year" : 2011}}
print(myfamily["child2"]["name"])