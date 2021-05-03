# cook your dish here
I = input
T = int(I())
for i in range(T):
    n = int(I())
    b = list(map(int, I().split()))
    s = sum(b)
    if s < 100 or (s-100)/n > 1:
        print("NO")
    else:
        print("YES")
    

