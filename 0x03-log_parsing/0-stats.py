#!/usr/bin/python3

"""
    Write a script that reads stdin line by line and computes metrics:
    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
"""


import sys

counter = 0
total_size = 0
status_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

try:
    line_count = 0
    for line in sys.stdin:
        parts = line.split(" ")
        if len(parts) > 4:
            code = parts[-2]
            size = int(parts[-1])
            if code in status_count.keys():
                status_count[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print("File size: {}".format(total_size))
            for key, value in sorted(status_count.items()):
                if value != 0:
                    print("{}: {}".format(key, value))

except Exception as err:
    pass

finally:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_count.items()):
        if value != 0:
            print("{}: {}".format(key, value))
