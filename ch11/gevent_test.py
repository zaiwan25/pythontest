import gevent
from gevent import socket
hosts = ['www.google.co.kr', 'www.facebook.com', 'www.daum.net']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)