# A =[1,2,4,5,7,29,30]
A = [1, 2, 4, 10, 25, 26, 27, 28]


def solution(A):
    # write your code in Python 3.6
    costs = 0
    d = 1
    while d+6 <=29:
        # print(d, d + 6)
        B = [x for i,x in enumerate(A) if x >=d and x <= d+6]
        if len(B) >3:
            costs += 7
            d += 6
        elif len(B) > 0:
            costs += 2 *len(B)
            d += len(B)
        else:
            d += 1

        print(d, d + 6, B, costs)
        # print(costs)
    # print(costs)
solution(A)