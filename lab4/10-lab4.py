n,k=[int(i) for i in input().split()]
weekends=set(range(6,n+1,7))
weekends.update(set(range(7,n+1,7)))
strike=set()
for i in range(k):
    a,b=[int(j) for j in input().split()]
    A=set(range(a,n+1,b))
    strike.update(A)
strike-=weekends
print(len(strike))




