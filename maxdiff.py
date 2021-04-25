# cook your dish here
t = int(input());

for i in range(t):
    n, k = list(map(int, input().split()))
    w = list(map(int, input().split()))
    w.sort()
    print (max(sum(w[k:]) - sum(w[:k]), sum(w[n-k:]) - sum(w[:n-k])))
