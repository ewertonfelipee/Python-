import os
import sys

print(os.getpid())

print(sys.platform)

for dir in os.listdir():
    print(dir)