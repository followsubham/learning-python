#R and Python have some libraries (like numpy and pandas) compare each element of the list to 2 (i.e. do an 'element-wise' comparison) and give us a list of booleans like [False, False, True, True].
#Implement a function that reproduces this behaviour, returning a list of booleans corresponding to whether the corresponding element is greater than n.


"""Return a list with the same length as L, where the value at index i is
True if L[i] is greater than thresh, and False otherwise.

>>> elementwise_greater_than([1, 2, 3, 4], 2)
[False, False, True, True]
"""
return [iter > thresh for iter in L]


