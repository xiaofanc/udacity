# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(a,b):
    if b in a:
        return a.index(b)
    return -1

# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(a,b):
    for i in b:
        if i not in a:
            a.append(i)
    return a 


a = [1,2,3]
b = [2,4,6]
print union(a,b)
#>>> [1,2,3,4,6]



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1