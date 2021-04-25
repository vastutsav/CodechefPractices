# cook your dish here
from operator import mul
from functools import reduce

def numOfComb(n,k):
    k = min(k, n-k)
    n = reduce(mul, range(n,n-k,-1), 1)
    d = reduce(mul, range(1, k+1), 1)
    return n//d
    
T = int(input())
for i in range(T):
    n, k = list(map(int, input().split()))
    print(numOfComb(n-1, k-1))
