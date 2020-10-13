# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num=int(input("Enter a number "))
check=int(input("Enter another number "))
rem=num1%check
if rem==0:
    print (f"{num} is divisible by {check}")
else:
        print(f"{num} is NOT divisible by {check}")
# divisible_by_4=number%4
# if divisible_by_4==0:
#     print("Number is divisible by 4")
# else:
#     print("Number is NOT divisible by 4")