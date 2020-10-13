#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many
# copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

name=input("What's your name? ")
age=int(input("What is your age?" ))
repeat=int(input("How many times you want to repeat? "))
age_remain=100-age
for rep  in range(1,repeat+1):
    print(f"Hey {name} you have {age_remain}yrs to become 100yrs old")
