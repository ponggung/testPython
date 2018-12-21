def foo(k, v, dic={}):
    dic[k] = v
    print(dic)

d = {}
foo("one", 1, d)
foo("two", 2, d)
foo("three", 3, {})
