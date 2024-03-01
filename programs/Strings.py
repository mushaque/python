# -------------Strings---------------
print("Hello")
print('Hello')

# Assign String to a Variable:
a="Kanna"
print(a)

# Multiline Strings
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# Strings are Arrays
a="Hello World"
print(a[1])

# Looping Through a String
for x in "banana ":
    print(x)

# String Length
a="Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# <-----------------Slicing Strings----------------->
# Slicing
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# <---------------Modify Strings-------------->
# Upper Case
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "HELLO, WORLD!"
print(a.lower())

# Remove Whitespace
a = " Hello, World "
print(a.strip())

# Replace String
a = "Hello, World!"
print(a.replace("H","D"))
print(a.replace("Hello","Hai"))

# Split String
a = "Hello, World!"
b = a.split(",")
print(b)

# <------------------String Concatenation------------->
a="Hello"
b="Kanna"
c=a+" "+b
print(c)

# <----------------Format - Strings-------------------->
# without format()

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# with format()
age = 36
txt = "My name is John, I am {} "
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
 
welcome_mail="Hi {},you will be working with {} Team"
name_team={'Rohit':'Mumbai','Kohli':'Rcb','Dhoni':'chennai'}
for key,value in name_team.items():
    print(welcome_mail.format(key,value))