# cook your dish here
T = int(input())
arr = [-1] * 2003
for i in range(T):
    arr = [-1] * 2003
    lst = 0
    fst = 0
    N = int(input())
    for j in range(N):
        x,y = map(int,input().split())
        arr[y] = max(arr[y], x)
        lst = max(lst, y)
        fst = min(fst, y)

    mx = -1
    ans = 0
    for i in range(fst, lst+1):
        if mx < arr[i] :
            mx = i
            ans += 1
    print(ans)
