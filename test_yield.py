# Coroutine
'''Coroutine，就是可以暫時中斷，之後再繼續執行的程序
Python最基礎的Coroutine也就是generator'''

def foo():
    for i in range(10):
        # 丟資料並且把主控權交給呼叫者
        yield i
        print (u'foo: 主控又回到我手上了，打我阿笨蛋')


bar = foo()
# 執行coroutine
print(next(bar))
print(u'main: 現在主控權在我們手上，做點雜事')
print ('main:hello baby!')
# 回到剛才foo這個coroutine中斷的地方繼續執行
print(next(bar))
print(next(bar))