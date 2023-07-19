#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = {}

    try:
        for line_number, line in enumerate(sys.stdin, 1):
            try:
                _, _, _, _, _, status_code_str, file_size_str = line.split()
                status_code = int(status_code_str)
                file_size = int(file_size_str)
            except (ValueError, IndexError):
                continue

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_number % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # If a keyboard interrupt (CTRL + C) is detected, print the current stats.
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
