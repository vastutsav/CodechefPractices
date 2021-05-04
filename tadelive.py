N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# Sorting A,B by their difference in descending order. 
# The intent is to reduce loss. 
# So, the orders with the hughest losses will be handled first
tipSortedByDiffAmt = sorted(list(zip(A,B)), reverse=True, key=lambda x: abs(x[0]-x[1]))
aOrdCnt = 0
bOrdCnt = 0
answer = 0
for t in tipSortedByDiffAmt:
    if t[0] >= t[1] and aOrdCnt < X:
        aOrdCnt+=1
        answer+=t[0]
    elif t[1] >= t[0] and bOrdCnt < Y:
        bOrdCnt+=1
        answer+=t[1]
    else:
        break

print (answer)