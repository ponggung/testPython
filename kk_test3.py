'''
Find wintter days' length
wintter's temperature must less than summer's temperature
wintter day's length is as shorter as better
'''

T = [5, -2, 3, 8, 6]
# T = [-5, -4, -3, -42, 1, -6, 2, 3, 6, 12,3]


def solution(T):

    if len(T) == 0:
        return 0

    winter_high = overall_high = T[0]

    for t in T:
        if t <= winter_high:
            winter_high = overall_high
        elif t > winter_high:
            overall_high = t
    print(winter_high, overall_high)
    length = 0
    for t in T:
        if t <= winter_high:
            length += 1

    return length
a = solution(T)
print(a)