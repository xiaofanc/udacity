# Question 1: Pick One

# Define a procedure, pick_one, that takes three inputs: a Boolean 
# and two other values. If the first input is True, it should return 
# the second input. If the first input is False, it should return the 
# third input.

# For example, pick_one(True, 37, 'hello') should return 37, and
# pick_one(False, 37, 'hello') should return 'hello'.

def pick_one0(boolean, a, b):
    if boolean:  
        return a
    else:
        return b

def pick_one1(boolean, a, b):
    if boolean == "True":    # not equal 
        return a
    else:
        return b

def pick_one2(boolean, a, b):
    if boolean is True:  
        return a
    else:
        return b

#print pick_one(True, 37, 'hello')
#>>> 37

#print pick_one(False, 37, 'hello')
#>>> hello

print pick_one0(True, 'red pill', 'blue pill')
print pick_one1(True, 'red pill', 'blue pill')
print pick_one2(True, 'red pill', 'blue pill')
#>>> red pill

#print pick_one(False, 'sunny', 'rainy')
#>>> rainy