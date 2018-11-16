import asyncio
import time

def test1():
    @asyncio.coroutine
    def hello():
        print("Hello world!")
        # 异步调用asyncio.sleep(1):
        r = yield from asyncio.sleep(1)
        print("Hello again!")


    # 獲取EventLoop:
    loop = asyncio.get_event_loop()
    # 執行coroutine
    loop.run_until_complete(hello())
    loop.close()


def test2():
    now = lambda: time.time()


    async def do_some_work(x):
        print('Waiting: ', x)


    start = now()

    coroutine = do_some_work(2)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)

    print('TIME: ', now() - start)


# test1()
test2()