# cook your dish here
import numpy

I = input
T = int(I())
for i in range(T):
    n = int(I())
    b = list(map(int, I().split()))
    sumOfList = sum(b)
    countOfNonZero = numpy.count_nonzero(b)
    if sumOfList < 100 or (sumOfList-100)/countOfNonZero >= 1:
        print("NO")
    else:
        print("YES")