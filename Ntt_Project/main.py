import re

timestamps = []
log_types = []
apps = []
statuses = []
run_times = []

with open('../output.txt', 'r') as file:
    lines = file.readlines()

log_pattern = re.compile(r'(\d{2}:\d{2}:\d{2}) - \[([A-Z]+)\] - (\w+) has (\w+) after (\d+)ms\.?.*')

for log_line in lines:
    match = log_pattern.match(log_line)
    if match:
        timestamp, log_type, app_name, status, runtime = match.groups()
        print(log_type)
        # Append the extracted values to their respective lists
        timestamps.append(timestamp)
        log_types.append(log_type)
        apps.append(app_name)
        statuses.append(status)
        run_times.append(runtime)

err = 0
warr = 0
info = 0

for info in log_type:
    if info == 'ERROR':
        err += 1
    elif info == 'DEBUG':
        warr += 1
    else:
        info += 1


