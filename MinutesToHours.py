#!/usr/bin/env python3
import sys
import os

def Hours(minutes):
    if minutes >= 0:
        print("{} H,{} M".format(minutes // 60,minutes % 60))
    else:
        raise ValuteError('输入的为负值！')
if __name__ == "__main__":
    minute = int(sys.argv[1])
    try:
        Hours(minute)
    except:
        print('是负值！')
    sys.exit(0)
