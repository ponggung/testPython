# Find saddle point in a Matrix

A = [[0, 1, 9, 3], [7, 5, 8, 3], [9, 2, 9, 4], [4, 6, 7, 1]]

A=[1]
def solution(A):
    # write your code in Python 3.6
    n = len(A)
    m = len(A[0])
    
    if n == 1:
        return 0
    sandle = 0
    for i in range(1, n-1, 1):
        for j in range(1, m-1, 1):
            local_row = [A[i][j], A[i - 1][j], A[i + 1][j]]
            local_col = [A[i][j], A[i][j+1], A[i][j-1]]
            # print(local_row, local_col)
            if A[i][j] == max(local_row) and A[i][j] ==min(local_col):
                sandle += 1
            elif A[i][j] == min(local_row) and A[i][j] ==max(local_col):
                sandle += 1

    return sandle



a = solution(A)
print(a)
