# cook your dish here
T = int(input());
for i in range(T):
    N = int(input())
    ans = 0
    for j in range(N):
        id, sum = map(int,input().split())
        ans = ans + id - sum 
    print(ans)
