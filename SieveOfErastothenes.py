import math

def prime(n):

    result = [True for i in range(n+1)]
    l=[]
    for p in range(2,int(math.sqrt(n))+1):
        if result[p]==True:
            for i in range(2*p, n+1, p):
                result[i]=False
    for i in range(2, n+1):
        if result[i]:
            l.append(i)
    return l

print(prime(10))
