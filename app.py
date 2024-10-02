# Let's create a function that determines if a number is odd or even
'''x = 5
y = 200
if x % 2==0 and y % 2==0:
      print("both are even")
elif x % 2==0 or 2==0:
      print("one is even")
elif y % 2==0 or 2==0:
      print("one is even")
else:
      print("both are odd")'''

# Let's create a function to accept a "bill" value and offer a tip of 0%,
# 15%, 20% or 25% depending on if the service was "bad, okay, good , 
# or great ". 
'''pluh = input("service:")
if pluh == "bad":
    print("0%")
if pluh == "okay":
    print("15%")
if pluh == "good":
    print("20%")
if pluh == "great":
    print("25%")'''
# Using the "input" method in Python, ask a user to input a sentence. 
# Then develop a function that accepts the user input and will tell
# you how many words are in that string. First write out your plan in
# Pseudo-code using comments. Then craft the function. 
'''a = "skibidi toilet"
x = a.split (" ")
print(x)
print(len(x))'''
# Create a function that accepts an input and determines all
# factors of the number. 
'''a = 45
for i in range (2,a+1):
    if a % i ==0:
        print(i)'''
# Create a function that accepts 2 arguments. 
# Find the greatest common factor between those numbers.
a = 359
b = 548
for i in range (2,a+1):
    if a % i ==0:
        print(i)
# One day, there was a (noun) who was very (adjective). (noun) loved (food), it loved (food) very much, but so did (name). (name) was very (adjective2), and therefore didn't get along well with (noun). (noun) and (name) fought over (food), and they would (verb) around (name)s backyard. (noun) would usually win, and celebrate with (noun2), but one day (noun) realized it was making (name) very (adjective3). (noun) apoligized by giving (name) his pet (noun3).
'''print("start")
name = input("name:")
adjective = input("adjective:")
adjective2 = input("adjective2:")
adjective3 = input("adjective3:")
noun = input("noun:")
noun2 = input("noun2:")
noun3 = input("noun3:")
verb = input("verb:")
food = input("food:")
print("One day , there was a", noun, "who was very", adjective,".", noun, "loved", food, ", it loved", food, "very much .. but so did", name, ".", name, "was very", adjective2, "and therefore didn't get along well with", noun, ".", noun, "and", name, "fought over", food, "and they would", verb, "fight around", name,"s backyard .", noun, "would usually win , and celebrate with", noun2, "but one day", noun, "realized it was making", name, "very", adjective3, ".", noun, "apoligized by giving", name, "his pet", noun3, ".")'''