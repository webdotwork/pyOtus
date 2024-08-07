import os
import re
import json
import argparse
from collections import defaultdict, Counter
from operator import itemgetter

# Regular expression to parse the log lines
log_pattern = re.compile(
    r'^(?P<ip>\S+) - - \[(?P<date>[\w:/]+\s[+\-]\d{4})\] "(?P<method>\S+) (?P<url>\S+) HTTP/\S+" \d+ \d+ "(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)" (?P<duration>\d+)$')


def parse_log_file(filepath):
    stats = {
        'total_requests': 0,
        'method_counts': defaultdict(int),
        'ip_counts': defaultdict(int),
        'longest_requests': []
    }

    with open(filepath, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                ip = data['ip']
                method = data['method']
                url = data['url']
                duration = int(data['duration'])
                date = data['date']

                stats['total_requests'] += 1
                stats['method_counts'][method] += 1
                stats['ip_counts'][ip] += 1

                stats['longest_requests'].append({
                    'ip': ip,
                    'date': date,
                    'method': method,
                    'url': url,
                    'duration': duration
                })

    return stats


def process_logs(path):
    total_stats = {
        'total_requests': 0,
        'method_counts': defaultdict(int),
        'ip_counts': defaultdict(int),
        'longest_requests': []
    }

    if os.path.isfile(path):
        log_files = [path]
    elif os.path.isdir(path):
        log_files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    else:
        raise ValueError("Invalid path provided. It should be a file or directory.")

    for log_file in log_files:
        file_stats = parse_log_file(log_file)
        total_stats['total_requests'] += file_stats['total_requests']
        for method, count in file_stats['method_counts'].items():
            total_stats['method_counts'][method] += count
        for ip, count in file_stats['ip_counts'].items():
            total_stats['ip_counts'][ip] += count
        total_stats['longest_requests'].extend(file_stats['longest_requests'])

    total_stats['longest_requests'] = sorted(total_stats['longest_requests'], key=itemgetter('duration'), reverse=True)[
                                      :3]

    top_ips = dict(Counter(total_stats['ip_counts']).most_common(3))

    result = {
        'top_ips': top_ips,
        'top_longest': total_stats['longest_requests'],
        'total_stat': dict(total_stats['method_counts']),
        'total_requests': total_stats['total_requests']
    }

    return result


def main():
    parser = argparse.ArgumentParser(description='Parse web server logs.')
    parser.add_argument('path', type=str, help='Path to the log file or directory containing log files.')
    args = parser.parse_args()

    result = process_logs(args.path)

    # Output to terminal
    print(json.dumps(result, indent=2))

    # Output to JSON file
    with open('log_stats.json', 'w') as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    main()
