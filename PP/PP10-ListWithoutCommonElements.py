# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.
# Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of
# different sizes.  (Hint: Remember list comprehensions from Exercise 7).
# Extra:
# Randomly generate two lists to test this

c=[]
d=[]
# count1=enumerate(a)
# count2=enumerate(b)
# m=max(count1,count2)
for i in a:
    if a[i]==b[i]:
        c.append(i)
    else:
        d.append(i)

print("The common elements are :",c)
print("The numbers which are not common :",d)