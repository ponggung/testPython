import logging
import json

'''不同使用裝飾器的方法'''

def loop(func):
    def new_func():
        func()
        func()
        func()
    return new_func

@loop
def test0():
    print("hi")

# step1
def test1():
    def use_logging(func):
        logging . warn(" %s is running" % func . __name__)
        func()


    def foo():
        print('i am foo')
    use_logging(foo)

#step2
def test2():
    def use_logging(func):
        def wrapper():
            logging . warn(" %s is running" % func . __name__)
            return func()  # 把foo當做參數傳遞進來時，執行func()就相當於執行foo()
        return wrapper
    def foo():
        print('i am foo')


    # 因為裝飾器use_logging(foo)返回的時函數對象wrapper，這條語句相當於foo = wrapper
    foo = use_logging(foo)
    foo()  # 執行foo()就相當於執行wrapper()

#step3
def test3():
    def  use_logging ( func ):
        def  wrapper ():
            logging . warn ( " %s is running"  %  func . __name__ )
            return  func ()
        return  wrapper

    @use_logging
    def  foo ():
        print ( "i am foo" )
    foo ()



def test4():
    class Foo (object):
        def __init__(self,  func):
            self . _func = func

        def __call__(self):
            print('class decorator runing')
            self . _func()
            print('class decorator ending')
    @Foo
    def bar():
        print('bar')
    bar()

if __name__=="__main__":
    test0()
    # test1()
    # test2()
    # test3()
    # test4()
