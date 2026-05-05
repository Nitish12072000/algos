def mul(a,b,n):
    tmp=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[i][j]=a[i][k]*b[k][j]
    return tmp
def exp(res,a,n,k): 
        
        while k>0:
            if k%2:
                res=mul(res,a,n)
            a=mul(a,a,n)
            k//=2
    
    
n,m,k=map(int,input().split())
mat=[[0 for i in range(n)] for i in range(n)]
res=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
    res[i][i]=1
while m>0:
    a,b=map(int,input().split())
    mat[a-1][b-1]=1
    m-=1
exp(res,mat,n,k)
fin=0
for i in range(n):
    for j in range(n):
        fin+=res[i][j]
print(fin)