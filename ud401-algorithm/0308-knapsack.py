"""
knapsack
weights w1, w2, .... wn
values  v1, v2, .... vn
substring: fit total capacity B, maximum total value

a. without repetition
b. unlimited supply?

Greedy: sort by value per unit of weights

DP:
K(i, b): max value available under the total capacity using object 1, 2, ..i & total weight <= b

"""
# a. without repetition
def knapsack(w, v, B):
    K = [[0]*(B+1) for _ in range(len(v))]
    n = len(v)
    for b in range(B+1):
        if w[0] <= b:
            K[0][b] = v[0]

    for i in range(1,n):
        for b in range(1, B+1):
            if w[i] <= b: # include or not include
                K[i][b] = max(v[i]+K[i-1][b-w[i]], K[i-1][b])
            else: # not include object i 
                K[i][b] = K[i-1][b]
    for k in K: print(k)
    return K[-1][-1]

print(knapsack([15,12,10,5],[15,10,8,1],22))

# b. unlimited supply?
# K[i][b] = max(no repeat, with repeat)
def knapsack(w, v, B):
    K = [[0]*(B+1) for _ in range(len(v))]
    n = len(v)
    for b in range(B+1):
        if w[0] <= b:
            K[0][b] = v[0]

    for i in range(1,n):
        for b in range(1, B+1):
            if w[i] <= b: 
                # max(no repeat, with repeat)
                # use object i multiple times
                K[i][b] = max(v[i]+K[i][b-w[i]], K[i-1][b])
    for k in K: print(k)
    return K[-1][-1]

print(knapsack([15,12,10,5],[15,10,8,1],22))















