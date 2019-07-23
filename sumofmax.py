d=int(input())
p=list(map(int,input().split()))
sum=0
for i in range(1,d):
    sum=sum+p[i]
print(sum)
