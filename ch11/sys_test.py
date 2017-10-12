import subprocess
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4).pprint

hddInfos = str(subprocess.getoutput('df -h')).split('\n')[1:]
for hddInfo in hddInfos:
    pp(hddInfo)

import os
disk = os.statvfs('/')
capacity = disk.f_bsize * disk.f_blocks
available = disk.f_bsize * disk.f_bavail
used = disk.f_bsize * (disk.f_blocks - disk.f_bavail)
print(used / capacity * 100)