# Implement a function that takes as input three variables, and returns the
# largest of the three. Do this without using the Python max() function!
# The goal of this exercise is to think about some internals that Python
# normally takes care of for us. All you need is some variables and if statements!

num1 = int(input("FIRST number: "))
num2 = int(input("SECOND number: "))
num3 = int(input("THIRD number: "))
if num1 > num2 > num3:
        max=num1
elif num1 > num3 > num2:
        max=num1
elif num2 > num3 > num1:
    max = num2
elif num2 > num1 > num3:
    max = num2
elif num3 > num1 > num2:
    max = num3
elif num3 > num2 > num1:
    max = num3
print(max)