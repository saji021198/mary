pin=int(input())
k=list(map(int,input().split()))
l=[]
sum=0
for i in range(0,pin):
    sum=sum+k[i]
    l.append(sum)
l=l[::-1]
print(*l)
