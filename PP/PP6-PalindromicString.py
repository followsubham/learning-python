# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
str=input("Enter a string :")
b=0
if str==str[::-1]:
    print(f"The string {str} is PALINDROMIC")
else:
    print(f"{str} is NOT palindromic")
