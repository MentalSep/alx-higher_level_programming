#!/usr/bin/python3
"""This module contains a script that reads stdin
line by line and computes metrics"""
import sys


def print_stats(file_size, status_codes):
    """Prints the stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def main():
    """Main function"""
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    try:
        for i, line in enumerate(sys.stdin, 1):
            tokens = line.split()
            file_size += int(tokens[-1])
            status_codes[tokens[-2]] += 1
            if i % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise


if __name__ == "__main__":
    main()
