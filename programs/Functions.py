# -------->Functions<--------------
# Creating a Function and Calling a Function
def my_function():
 print("Hello Mushtaque")
my_function()

# Arguments
def my_function(fname):
    print(fname + " mushtaque")
my_function("Email")
my_function("sheik")
my_function("Hai")

# Number of Arguments
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname,lname ):
    print(fname+" "+lname)
my_function("email","name")

# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(kids):
    print("The youngest child is "+kids[2])
my_function(["munna","chinna","kanna"])

# Keyword Arguments
def my_function(child3,child2,child1):
    print("The youngest child is "+child2)
my_function(child1="munna",child2="chinna",child3="kanna")

# Arbitrary Keyword Arguments, **kwargs
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
    print("His last name is " +kid["lname"])
my_function(fname="Rohit",lname="Sharma")

# Default Parameter Value
def my_function(country="Norway"):
    print("I am from " +country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
 for x in food:
  print(x)
fruits=["apple", "banana", "cherry"]
my_function(fruits)

# Return Values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# Positional-Only Arguments
def my_function(x, /):
  print(x)
my_function(3)

# Without the , / you are actually allowed to use keyword arguments 
def my_function(x):
  print(x)
my_function(x = 3)

# Keyword-Only Arguments
def my_function(*,x):
  print(x)
my_function(x = 3)


# # # EXERCISE1
# # def print_shape(length, width):
# #     if length == width:
# #         print("It's a square.")
# #     elif length != width:
# #         print("It's a rectangle.")
# # length = float(input("Enter the length: "))
# # width = float(input("Enter the width: "))
# # print_shape(length, width)


# # Exercise2
# def triangle_type(length, breadth, height):

#         if length == breadth == height:
#             return "Equilateral"
#         elif length == height :
#             return "Isosceles"
#         else:
#             return "Scalene"
   
# length = float(input("Enter the length of the triangle: "))
# breadth = float(input("Enter the breadth of the triangle: "))
# height = float(input("Enter the height of the triangle: "))

# triangle = triangle_type(length, breadth, height)
# print("The triangle is:", triangle)


# # EXERCISE3
# import random

# options=("rock","paper","scissors")

# player='User'
# computer=random.choice(options)

# while player not in options:
#   player=input("Enter a choice(rock,paper,scissors):")

# print(player)
# print(computer)

# # print(f"player:{player}")
# # print(f"computer:{computer}")

# if player==computer:
#   print("It's a tie!")
# elif player=="rock" and computer=="scissors":
#     print("You win!")
# elif player=="paper" and computer=="rock":
#     print("You win!")
# elif player=="scissors" and computer=="paper":
#     print("You win!")
# else:
#     print("You lose!")
