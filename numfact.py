from functools import reduce
from math import sqrt

count = {}
def getNumFactors(num):
    f = 2
    while f*f <= num:
        while num%f==0:
            num = num // f;
            if f in count:
                count[f]+=1
            else:
                count[f]=1
        if f > 2:
            f+=2
        else:
            f+=1

    if num != 1:
        if num not in count:
            count[num] = 0
        count[num] += 1

T = int(input())
for i in range(T):
    count.clear()
    n = int(input())
    l = list(map(int,input().split()))
    for j in l:
        getNumFactors(j)

    #print (count)
    print(reduce(lambda a,b: a*b, map(lambda a:a+1,count.values())))
