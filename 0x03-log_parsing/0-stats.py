#!/usr/bin/env python3

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
            continue

        status_code = int(parts[3])
        file_size = int(parts[6])

        total_size += file_size
        status_count[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print("Total file size: File size:", total_size)
            for code in sorted(status_count):
                if status_count[code] > 0:
                    print(f"{code}: {status_count[code]}")

except KeyboardInterrupt:
    print("Total file size: File size:", total_size)
    for code in sorted(status_count):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")
