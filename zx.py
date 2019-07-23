p=int(input())
k=list(map(int,input().split()))
lin=[]
sum=0
for i in range(0,p):
    sum=sum+k[i]
    lin.append(sum)
print(*lin)
