#!/usr/bin/python3
"""This module contains a script that reads stdin
line by line and computes metrics"""
import sys


def print_stats(status_codes, file_size):
    """
    prints stats

    Arguments:
        status_codes {dict} -- [dictionary of status codes]
        file_size {int} -- [file size]
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    LineCount = 0
    try:
        for line in sys.stdin:
            LineCount += 1
            data = line.split()
            try:
                total_size += int(data[-1])
            except [ValueError, IndexError]:
                pass
            try:
                status_codes[data[-2]] += 1
            except [KeyError, IndexError]:
                pass
            if LineCount % 10 == 0:
                print_stats(status_codes, total_size)
        print_stats(status_codes, total_size)
    except KeyboardInterrupt:
        print_stats(status_codes, total_size)
        raise
