# ------------For Loops----------


fruits=["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String:Loop through the letters in the word "banana":

for a in "Mushtaque":
 print(a)

# The break Statement:With the break statement we can stop the loop before it has looped through all the items:
fruits=["Bmw", "Audi", "Benz"]
for y in fruits:
    print(y)
    if y=="Audi":
     break
   
fruits = ["Car", "Bus", "Auto"]
for x in fruits:
  if x == "Bus":
    break
  print(x)

#The continue Statement:With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits=["apple", "banana", "cherry"]
for z in fruits:
    if x=="banana":
        continue
    print(z)

#The range() Function:range() function returns a sequence of numbers, starting from 0 by default, 
for x in range(6):
    print(x)

#range(2, 6)
for x in range(2, 6):
  print(x)

# range(2, 30, 3):Increment the sequence with 3 (default is 1):
for y in range(2,30,3):
 print(y)

#Else in For Loop:Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x==3:
        break
    print(x)
else:
     print("Finally finished!")

# Nested Loops:A nested loop is a loop inside a loop.
adj=["red", "big", "tasty"]
fruits=["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

