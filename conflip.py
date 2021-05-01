# cook your dish here
T = int(input())
for i in range(T):
    G = int(input())
    for j in range(G):
        N, I, Q = map(int, input().split())
        if N==Q:
            print(I//2)
        else:
            print((I+1)//2)
