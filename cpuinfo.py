#!/usr/bin/env python3
import sys
import os
if __name__ == "__main__":
    if os.path.exists("/proc/cpuinfo"):
        with open("/proc/cpuinfo") as cpuinfo:
            for line in cpuinfo:
                print(line,end = '')
    else:
        sys.exit(-1)
    sys.exit(0)
