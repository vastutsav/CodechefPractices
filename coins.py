# cook your dish here
dp = {}
def recFun(num):
    if num < 12:
        return num
    elif num in dp:
        return dp[num]
    else:
        dp[num] = recFun(num//4) + recFun(num//3) + recFun(num//2)
        return dp[num]

while True:
    try:
        print(recFun(int(input())))
    except:
        break
