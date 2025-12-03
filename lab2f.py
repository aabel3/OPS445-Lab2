#!/usr/bin/env python3
# OPS435 - Lab 2
# lab2f.py
# Author: Avraham Abel

import sys

count = int(sys.argv[1])

while count > 0:
	print(str(count))
	count = count - 1

print("blast off!")
