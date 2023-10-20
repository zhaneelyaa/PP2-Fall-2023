def isPrime(x):
    d = 2
    while x % d != 0 and pow(d,2) < x:
        d+=1
    if x % d != 0:
         return True
    else:
        return False
        
        def filt(n):
    list(map(lambda x : isPrime(x), n))
    print(*list(filter(isPrime,n)))
    
    n=list(map(int,input().split()))
