ranks = [3,4,3,0,2,2,3,0,0]

ranks = [0,1,1,1,2,4,4,4,5,1000,0,0,0]


def solution(ranks):
    # write your code in Python 3.6
    import collections

    c = 0
    count = collections.Counter(ranks)
    ranks = list(set(ranks))
    for i in ranks:
        # print(i+1)
        if i + 1 in ranks:
            c += count[i]
    return c


c = solution(ranks)
print(c)