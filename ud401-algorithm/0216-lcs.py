"""
longest common subsequence
find the length of the longest string which is a subsequence of both x&y
X = BCDBCDA
Y = ABECBAB
LCS = BCBA 

1st step: define subproblem in words
let L(i) = length of LCS in the first I characters of X and the first I characters of Y 
2nd step: state recursive relation
express L(i) in lens of L(1), L(2)... L(i-1)
We take the optimal solution for the subproblem of size i-1 and then we append on
the solution for xi and yi
two cases to consider: either the last character is the same or the are different

xi == yi last character same
X = BCDBCDAC
Y = ABECBABC
The longest common subsequence must include C
2nd step: state recursive relation
L(i) = 1 + L(i-1)

xi ^= yi last character different
X = BCDBCDA
Y = ABECBAB
The longest common subsequence does not include A or does not include B or both

let L(i, j) = the length of the longest common subsequence in X1 through Xi with
Y1 through Yj
2nd step: state recursive relation
base case: L(0,j) = 0, L(i, 0) = 0
unequal case: if Xi ^= Yj: either Xi and/or Yj not in the optimal solution
if drop Xi then L(i, j) = L(i-1, j)
if drop Yj then L(i, j) = L(i, j-1)
so L(i, j) = max{L(i-1, j), L(i, j-1)}
equal case: Xi = Yj: either drop Xi(Yj) or optimal solution ends at Xi = Yj
if drop Xi then L(i, j) = L(i-1, j)
if drop Yj then L(i, j) = L(i, j-1)
if optimal solution ends at Xi = Yj then L(i, j) = 1 + L(i-1, j-1)
L(i, j) = max{L(i-1, j), L(i, j-1), 1 + L(i-1, j-1)}
Xi = Yj, so further L(i, j) = 1 + L(i-1, j-1)

create 2-D matrix:
for i = 0 -> n, L(i, 0) = 0  # first col = 0
for j = 0 -> n, L(0, j) = 0  # first row = 0
for i = 1 -> n:
    for j = 1 -> n:
        if Xi = Yj then L(i, j) = 1 + L(i-1, j-1)
        else L(i, j) = max{L(i-1, j), L(i, j-1)}

example:
X = BCDBCDA
Y = ABECBA
 
   j  0  1  2  3  4  5  6 
 i       A  B  E  C  B  A
 0    0  0  0  0  0  0  0
 1 B  0  0  1  1  1  1  1
 2 C  0  0  1  1  2  2  2
 3 D  0  0  1  1  2  2  2
 4 B  0  0  1  1  2  3  3
 5 C  0  0  1  1  2  3  3
 6 D  0  0  1  1  2  3  3
 7 A  0  1  1  1  2  3  4

 The following diagram depicts how to extract the sequence from the DP table, 
 tracing back from the last matching cell.
 A -> B -> C -> B
 LCS = BCBA

"""

def lcs(x, y):
    if not x or not y:
        return 0
    lenx, leny = len(x), len(y)
    L = [[0]*(leny+1) for _ in range(lenx+1)]
    for i in range(1, lenx+1):
        for j in range(1, leny+1):
            if x[i-1] == y[j-1]:    # index in X and Y
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    for l in L: print(l)
    return L[lenx][leny]

def lcs(x, y):
    if not x or not y:
        return 0
    lenx, leny = len(x), len(y)
    L = [[0]*leny for _ in range(lenx)]
    def getL(x, y):
        if 0 <= x < lenx and 0 <= y < leny:
            return L[x][y]
        else:
            return 0
    for i in range(lenx):
        for j in range(leny):
            if x[i] == y[j]:
                L[i][j] = 1 + getL(i-1, j-1)
            else:
                L[i][j] = max(getL(i-1,j), getL(i, j-1))
    return L[lenx-1][leny-1]


print(lcs("bcdbcda","abecbabd"))