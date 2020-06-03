# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(n):
    # Your code here
    if n/5 == 0:
        if n/2 == 0:
            a,b,c = 0, 0, n
            return a,b,c
        a,b,c = 0, n/2, n%2
        return a,b,c
    else:
        a, res = n/5, n%5
        if res < 2:
            b, c = res, 0
            return a,b,c
        else:
            b, c = res/2, res%2
            return a,b,c

def stamps(n):
    # Your code here
    r1, n = divmod(n, 5)
    r2, n = divmod(n, 2)
    return (r1, r2, n)
        
        
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps