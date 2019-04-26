#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import time

time_start = time.time()
x = -100
y = 0
z = 0
t = 0
while x < 100000:
    x = x + 1
    y = math.sqrt(x + 100)
    z = math.sqrt(x + 100 + 168)
    if y-(int(y)) == 0 and z-(int(z)) == 0:
        print(x)
time_end = time.time()
print't =',time_end-time_start