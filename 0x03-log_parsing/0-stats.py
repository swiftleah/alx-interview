#!/usr/bin/python3
"""
Log parsing
"""
import sys


def print_metrics(file_size, status_codes):
    """
    Print metrics
    """
    print("File size:", file_size)
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


def parse_line(line, codes_count):
    """
    Parse each line of the log
    """
    try:
        status_code = line.split()[-2]
        if status_code in codes_count:
            codes_count[status_code] += 1
        # Grab file size
        file_size = int(line.split()[-1])
        return file_size
    except Exception:
        return 0


if __name__ == "__main__":
    codes_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}
    file_size_total = 0
    count = 0
    try:
        for line in sys.stdin:
            file_size_total += parse_line(line, codes_count)
            count += 1
            # print metrics if 10 lines have been read
            if count == 10:
                print_metrics(file_size_total, codes_count)
                count = 0
    except KeyboardInterrupt:
        print_metrics(file_size_total, codes_count)
        raise
    print_metrics(file_size_total, codes_count)
