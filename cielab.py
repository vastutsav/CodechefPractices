# cook your dish here
a,b = map(int, input().split())
c = abs(a-b)
l = c%10
if l == 9:
    c-=1
else:
    c+=1
print(c)
