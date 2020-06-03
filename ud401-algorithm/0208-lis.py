# longest increasing subsequence
# L(i) is the length of LIS in the first I elements in the input
# for i = 1....n
# subsequence is not necessary consecutive
"""
A = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
L = [1, 2, 2,  2, 3, 3,  4, 4, 4, 5, 6, 6]

LIS1 = [5, 7, 9, 10]
when i = 8, the longest subsequence changes to:
LIS2 = [-3, 1, 4, 5, 8, 9]
so need min ending character in LIS solution, so that we can know if we can add the number

# So, we add an extra condition:
1st step: define subproblem in words
let L(i) = the length of longest increasing subsequence in a1, a2, a3, a4...... ai 
which ends at ai !!
2nd step: state recursive relation
L(i) = 1 + max{L(j): aj < ai & j < i}
Taking the earlier subsequence ending at aj and append ai onto the end

A = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
L = [1, 2, 1,  1, 3, 2,  4, 3, 4, 5, 6, 3]

"""

def lis(a):
    n = len(a)
    L = [1]*n
    for i in range(n):
        for j in range(i):   # 0 to i-1
            # exclude n which is not smaller than ai
            # find the largest L before Li, then add 1
            if a[j] < a[i] and L[i] < 1+ L[j]:
                L[i] = 1 + L[j]
    print(L)
    return max(L)

def lis(a):
    size = len(a)
    L = [1]
    for i in range(1,size):
        Li = 1 + max([L[j] for j in range(i) if a[j] < a[i]], default = 0)
        L.append(Li)
    print(L) 
    return max(L)

def lis(a):
    n = len(a)
    L = [1]*n
    dp_loc = [-1]*n
    for i in range(n):
        for j in range(i):
            # exclude n which is not smaller than ai
            # find the largest L before Li, then add 1
            if a[j] < a[i] and L[i] < 1+ L[j]:
                L[i] = 1 + L[j]
                dp_loc[i] = j

    k = L.index(max(L))
    print(a)
    print(L)
    print(dp_loc)
    print(k)
    #a =      [ 5, 7,  4, -3, 9, 1,10, 4, 5, 8, 9, 3]
    #i =      [ 0, 1,  2,  3, 4, 5, 6, 7, 8, 9, 10,11]
    #L =      [ 1, 2,  1,  1, 3, 2, 4, 3, 4, 5, 6, 3]
    #dp_loc = [-1, 0, -1, -1, 1, 3, 4, 5, 7, 8, 9, 5]
    path = []
    while k != -1:
        path.append(k) 
        k = dp_loc[k]
        #print(k)
    print(path) # [10, 9, 8, 7, 5, 3] index 
    path.reverse()
    return [a[i] for i in path] # subsequence = [-3, 1, 4, 5, 8, 9]


print(lis([5,7,4,-3,9,1,10,4,5,8,9,3])) # L = 1,2,1,1,3,2,4,3,4,5,6,3