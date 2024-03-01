#------------ Loops--------

newlist = ['a','e','i','o','u']

# loop entire list and print every item
for letter in newlist:
    print(letter)

# Loop specific part of list
for letter in newlist[1:3]:
    print(letter)

# looping list using length of list & range
for index_number in range(len(newlist)):
    print(newlist[index_number])

# using if condition compare 2 variabbles

x = 5
y = 5

# comparing x & y

if x>y:
    print("x is greater than y")
elif x<y:
    print("x is less than y")
else:
    print("x is equal to y")


# using if condition and for loop concatenate items form two lists
# no of items to concatenate is equal to length of the list with least no of elements

student_first_name = ['first1','first2']
student_last_name = ['last1','last2','last3']

length_first = len(student_first_name)
length_last = len(student_last_name)

print(length_first,length_last)

# length_first == length_last
if length_first == length_last:
    length = len(student_first_name)
elif length_first > length_last:
    length = len(student_last_name)
else:
    length = len(student_first_name)

for index in range(length):
        print(student_first_name[index]+' - '+student_last_name[index])





# For Loop,Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# Looping Through a String
fruits = ["apple", "banana", "cherry"]
for x in "banana":
  print(x)
# The break Statement,Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# The continue Statement,Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
 if x == "banana":
    continue
 print(x)

# The range() Function
for x in range(6):
    print(x)
# Nested Loops,Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x,y)


        
# create if condition to print if a given number is positive/negative

n=int(input("Enter the number:"))
if n>0:
    print(n,"is a positive number")
elif n<0:
     print(n,"is a negative number")
else:
    print("Entered number is zero")

# create an example by compaining for loop & if condition

parent_name = ['cow','goat','cat','horse']
child_name = ['calf','kid','kitten','foal']

length_parent = len(parent_name)
length_child = len(child_name)
print(length_parent,length_child)

if length_parent==length_child:
    length=len(parent_name)
elif length_parent > length_child:
    length=len(child_name)
else:
    length=len(parent_name)
for animals in range(length):
    print(parent_name[animals]+'-'+child_name[animals])

    
