"""
matrix: AxBxCxD

((AxB)xC)xD
(AxB)x(CxD)
(Ax(BxC))xD
Ax(Bx(CxD))

which one is best?

recusion rule:
cost(i, j) = min cost for computing Ai, Ai+1,....Aj
           = root costs + left tree cost and right tree cost
           = m(i-1)m(l)m(j) + c(i, l) + c(l+1, j)

"""

def matrixmultiply(m):
    n = len(m)-1
    c = [[0]*n for i in range(n)]
    print(n, c)
    for s in range(1, n):
        for i in range(n-s):
            j = i + s  
            print(s, i, j)
            c[i][j] = min(m[i-1]*m[l]*m[j] + c[i][l] + c[l+1][j] for l in range(i, j))
    print(c)
    return c[0][n-1]

if __name__ == '__main__':
    print(matrixmultiply([1,1000,1,1000]))
    print(matrixmultiply([50,20,1,10,100]))