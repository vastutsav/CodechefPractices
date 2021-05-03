import numpy as np
import sys

N,M = map(int,sys.stdin.readline().split())
L = np.zeros(N, dtype=bool)
for _ in range(M):
    p,x,y = map(int, sys.stdin.readline().split())

    if p == 0:
        L[x:y+1] = ~L[x:y+1]
    else:
        print(L[x:y+1].sum())
