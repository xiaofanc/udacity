def fibo(n, l=0):
    print("  "*l + "fibo(%d)" % n )
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1, l+1) + fibo(n-2, l+1)

memo = {0:0, 1:1}
def fibo(n, l=0):
    if n in memo: return memo[n]
    print("  "*l + "fibo(%d)" % n )
    memo[n] = fibo(n-1, l+1) + fibo(n-2, l+1)
    return memo[n]

def fibo(n):
    n0, n1 = 0, 1
    if n == 0: return 0
    for i in range(2,n+1):
        n0, n1 = n1, n0+n1
    return n1

def fibo(n):
    if n == 0: return 0
    F = [None] * (n+1)
    F[0], F[1] = 0, 1
    print(F)
    for i in range(2,n+1):
        F[i] = F[i-1] + F[i-2]
        print(F[i-2], F[i-1], F[i])
    return F[n]

print(fibo(2))
#for i in range(10):print(fibo(i))
