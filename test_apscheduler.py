from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler


#https://izsk.me/2017/09/27/python%E5%AE%9A%E6%97%B6%E6%A1%86%E6%9E%B6APScheduler(%E4%B8%80)/

def foo():
    print("foo")


# sched = BackgroundScheduler()
sched = BlockingScheduler(daemon=True)
sched.add_job(foo, 'interval', seconds=1)
sched.start()  #啟動
