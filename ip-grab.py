import sys
import re
from collections import Counter

# Regular expression pattern to match IP addresses
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

def analyze_log(log_file_path):
    # Read the log file
    with open(log_file_path, 'r') as file:
        log_data = file.read()

    # Find all IP addresses in the log
    ip_addresses = re.findall(ip_pattern, log_data)

    # Count the occurrences of each IP address
    ip_counter = Counter(ip_addresses)

    # Print the IP addresses and their counts
    for ip, count in ip_counter.items():
        print(f'{ip}: {count}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analysis.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    analyze_log(log_file_path)

