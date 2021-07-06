x=list(map(int,input().split()))
y=list(map(int,input().split()))
ans=0
for i in range(len(x)):
    ans+=x[i]*y[i]
print(ans)