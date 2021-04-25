from functools import reduce
from math import sqrt

count = {}
def getNumFactors(n):
    for i in range(2, int(sqrt(n)) + 2):
        if n % i == 0 and i not in count:
            count[i] = 0
        while n % i == 0:
            n //= i
            count[i] += 1
    if n != 1:
        if n not in count:
            count[n] = 0
        count[n] += 1

T = int(input())
for i in range(T):
    count.clear()
    n = int(input())
    l = list(map(int,input().split()))
    for j in l:
        getNumFactors(j)

    print(reduce(lambda a,b: a*b, map(lambda a:a+1,count.values())))
