# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list,
# and another using sets. Go back and do Exercise 5 using sets, and write the solution for
# that in a different function.

def remove_duplicates(a):
    b=[]
    for i in a:

        if i not in b:
            b.append(i)
    return b

print(remove_duplicates([1,2,3,4,3,2,1]))

