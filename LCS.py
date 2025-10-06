# Task 1

X = "AGCCCTAAGGGCTACCTAGCTT"
Y = "GACAGCCTACAAGCGTTAGCTTG"

m, n = len(X), len(Y)
dp = [[0] * (n + 1) for _ in range(m + 1)]
direction = [[""] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if X[i - 1] == Y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            direction[i][j] = "↖"
        elif dp[i - 1][j] >= dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j]
            direction[i][j] = "↑"
        else:
            dp[i][j] = dp[i][j - 1]
            direction[i][j] = "←"

i, j = m, n
lcs = []
while i > 0 and j > 0:
    if direction[i][j] == "↖":
        lcs.append(X[i - 1])
        i -= 1
        j -= 1
    elif direction[i][j] == "↑":
        i -= 1
    else:
        j -= 1

lcs.reverse()
print("Final LCS cost:", dp[m][n])
print("LCS:", "".join(lcs))
print("\nCost Matrix:")
for row in dp:
    print(row)
print("\nDirection Matrix:")
for row in direction:
    print(row)