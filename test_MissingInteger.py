import collections
# A = [1, 2, 3]
# A = [-1,-3]
A = [1, 3, 6, 4, 1, 2,1,3,2,4]
# A=[7]

def solution(A):
    # write your code in Python 3.6
    result = 1
    s = set(A)
    while result in s:
        result += 1
    return result


ans = solution(A)
print(ans)

# A = collections.Counter(A)
# B = collections.Counter(B)
# print(B & A == B)