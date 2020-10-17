# Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Write one line of Python that takes this list a and makes a new list that
# has only the even elements of this list in it.
# even_list=[]
# for b in a:
#     if b %2==0:
#         even_list.append(b)
# print(even_list)

b = [number for number in a if number % 2 == 0]   #New Gyan
print(b)