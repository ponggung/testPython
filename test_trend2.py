A = 5
B = 3
from itertools import permutations
from itertools import combinations

def solution(A, B):

    # write your code in Python 3.6

    C = A * "a" + B * "b"
    C = list(permutations(C))
    C = list(set(C))
    C = [''.join(x) for x in C]
    C =[x for x in C if "aaa" not in x]
    C =[x for x in C if "bbb" not in x]
    # filter(lambda k: 'aaa' in k, C)
    for item in C:
        print(item)
    #     return item

# c = solution(A, B)


# from itertools import product
# from itertools import permutations
# # for item in product("ABCD","xy"):
# #     print(item)
# # print(list(product('ab', range(3))))
# print(list(permutations('ABC')))

C = list(combinations("aaaaabbb",8))
print(C)