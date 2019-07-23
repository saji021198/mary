pin=int(input())
k=list(map(int,input().split()))
l=[]
t=[]
sum=0
for i in range(0,pin):
    sum=sum+k[i]
    l.append(sum)
u=l[::-1]
for i in range(0,pin):
    t.append(l[i]+u[i])
print(*t)
