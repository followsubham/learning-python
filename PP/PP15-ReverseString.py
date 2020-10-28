# Write a program (using functions!) that asks the user for a long string
# containing m#ultiple words. Print back to the user the same string,
# except with the words in backwards order.

long_string=input("Input a long sentence: ")
new=long_string.split(" ")
j=" ".join(new[:: -1])

print(j)