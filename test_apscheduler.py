from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler


def foo():
    print("foo")


# sched = BackgroundScheduler()
sched = BlockingScheduler(daemon=True)
sched.add_job(foo, 'interval', seconds=1)
sched.start()  #啟動
