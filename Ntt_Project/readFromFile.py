import re
def readFile(path):
    # '../output.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines

def extractInfo(lines):

    log_pattern = re.compile(r'(\d{2}:\d{2}:\d{2}) - \[([A-Z]+)\] - (\w+) has (\w+) after (\d+)ms\.?.*')

    timestamps = []
    log_types = []
    apps = []
    statuses = []
    run_times = []
    for log_line in lines:
        match = log_pattern.match(log_line)
        if match:
            timestamp, log_type, app_name, status, runtime = match.groups()
            print(status)
            timestamps.append(timestamp)
            log_types.append(log_type)
            apps.append(app_name)
            statuses.append(status)
            run_times.append(runtime)
    print(log_types)
    return timestamps, log_types, apps, statuses, run_times


