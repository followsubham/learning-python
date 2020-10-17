import random as rand
usrnum=int(input("Enter a number between 1 & 9:"))
mgcnum=rand.randint(1,9)
if usrnum==mgcnum:
    print("You guessed correctly")
elif usrnum>mgcnum:
    print("Your guess is larger")
else:
    print("Magic number is larger")

cont=input("Do yo want to continue y or n :")
if cont=="y":
    continue()
else:
    exit