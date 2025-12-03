#!/usr/bin/env python3
# OPS435 - Lab 2
# lab2d.py
# Author: Avraham Abel

import sys

if (len(sys.argv) != 3):
	print("Usage: ./lab2d.py name age")
	sys.exit()
	
name = sys.argv[1]
age = sys.argv[2]

print("Hi " + name + ", you are " + str(age) + " years old.")
