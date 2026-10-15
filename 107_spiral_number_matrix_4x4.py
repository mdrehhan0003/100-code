"""Problem 107: Spiral Number Matrix 4X4."""

n = 4
matrix = [[0]*n for _ in range(n)]
top, bottom, left, right = 0, n-1, 0, n-1
value = 1
while top <= bottom and left <= right:
    for j in range(left, right+1): matrix[top][j] = value; value += 1
    top += 1
    for i in range(top, bottom+1): matrix[i][right] = value; value += 1
    right -= 1
    if top <= bottom:
        for j in range(right, left-1, -1): matrix[bottom][j] = value; value += 1
        bottom -= 1
    if left <= right:
        for i in range(bottom, top-1, -1): matrix[i][left] = value; value += 1
        left += 1
for row in matrix: print(*row)
