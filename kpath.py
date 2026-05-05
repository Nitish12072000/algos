MOD = 1000000007

def mul(a, b, n):
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[i][j] = (tmp[i][j] + a[i][k]*b[k][j]) % MOD
    return tmp

def exp(res, a, n, k):
    while k > 0:
        if k % 2:
            res = mul(res, a, n)
        a = mul(a, a, n)
        k //= 2
    return res

n, m, k = map(int, input().split())

mat = [[0]*n for _ in range(n)]
res = [[0]*n for _ in range(n)]

for i in range(n):
    res[i][i] = 1

for _ in range(m):
    a, b = map(int, input().split())
    mat[a-1][b-1] = 1

res = exp(res, mat, n, k)

fin = 0
for i in range(n):
    for j in range(n):
        fin = (fin + res[i][j]) % MOD

print(fin)