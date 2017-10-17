from multiprocessing import Process, freeze_support
import redis
import os
import time


def dryer():
    conn = redis.Redis()
    pid = os.getpid()
    timeout = 20
    print('Dryer process %s is starting ' % pid)
    while True:
        msg = conn.blpop('dishes', timeout)
        if not msg:
            break
        val = msg[1]
        if val == 'quit':
            break
        print('%s: dried %s' % (pid, val))
        time.sleep(0.1)
    print('Dryer process %s is done' % pid)

if __name__ == "__main__":
    freeze_support()
    DRYERS = 3
    for num in range(DRYERS):
        p = Process(target=dryer)
        p.start()

