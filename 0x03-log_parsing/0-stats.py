#!/usr/bin/python3
"""
This script parses a log file read from stdin
Lines are in this format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
import sys


def printLog(status_codes, total_size):
    """Prints the log to stdout"""
    log = ["File size: {}".format(total_size)]
    for code, occurrences in sorted(status_codes.items()):
        if occurrences > 0:
            log.append("{}: {}".format(code, occurrences))
    print("\n".join(log))


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_size = 0
lines = 0
try:
    for log_line in sys.stdin:
        try:
            url_separated = log_line.split("\"")
            status_file_size = url_separated[2].strip().split(" ")
            status_code = status_file_size[0]
            if status_code in status_codes:
                lines += 1
                file_size = int(status_file_size[1])
                total_size += file_size
                status_codes[status_code] = status_codes[status_code] + 1
        except (IndexError, ValueError):
            pass
        if lines % 10 == 0:
            printLog(status_codes, total_size)
            lines = 0
finally:
    printLog(status_codes, total_size)
