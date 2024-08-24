N = int(input())
domino = []
row = input().strip().split(' ')
row = [int(x) for x in row]
domino.append(row)
row = input().strip().split(' ')
row = [int(x) for x in row]
domino.append(row)

dp = [0] * (N + 1)

for i in range(0, N + 1):
    if i == 0:
        continue
    
    vertical_score = abs(domino[0][i - 1] - domino[1][i - 1]) + dp[i - 1]
    
    if i > 1:
        horizontal_score = abs(domino[0][i - 1] - domino[0][i - 2]) + abs(domino[1][i - 1] - domino[1][i - 2]) + dp[i - 2]
    else:
        horizontal_score = 0
    dp[i] = max(vertical_score, horizontal_score)    

print(dp[-1])
    