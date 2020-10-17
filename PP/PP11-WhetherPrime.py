# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.). 4
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to
# practice using functions, described below.
fac=[]
usrnum=int(input("Enter a number :"))
for i in range(2,usrnum-1):
    if usrnum%i==0:
        fac.append(i)
if fac==[]:
    print("The number is PRIME")
else:
    print("The number is NOT PRIME")
