#!/usr/bin/python3
"""This module contains a script that reads stdin
line by line and computes metrics"""
import sys


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
lineCount = 0

try:
    for line in sys.stdin:
        lineCount += 1
        data = line.split()
        status = data[-2]
        file_size = data[-1]
        if status in status_codes:
            status_codes[status] += 1
        total_size += int(file_size)
        if lineCount == 10:
            print("File size: {}".format(total_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            lineCount = 0
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
