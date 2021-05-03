# cook your dish here
import numpy as np
n,q = map(int,input().split())
c = np.zeros(n, dtype=bool)
for _ in range(q):
    d,a,b = map(int,input().split())
    if d:
        print(np.count_nonzero(c[a:b+1]))
    else:
        c[a:b+1]=~c[a:b+1]
