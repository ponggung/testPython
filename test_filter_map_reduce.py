# filter
def fn(x):
    return x if x > 5 else None

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = filter(fn, a)
print(list(b))


# map
def fn2(x):
    return x*2
c = map(fn2, a)

print(list(c))


# reduce
from functools import reduce
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def fn3(x,y):
    return x+y
d = reduce(fn3, a)

print(d)