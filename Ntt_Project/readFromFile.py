import re
def readFile(path):
    # './output.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines

def extractInfo(log_data):
    timestamps = []
    log_types = []
    descriptions = []

    for entry in log_data:
        # we want to split the string into 3 parts: timestamp, log type, and description of log type
        parts = entry.split(' - ')

        timestamp = parts[0].strip()
        # we want to remove the brackets from the log type
        log_type = parts[1].strip("[]")
        description = parts[2].strip()

        timestamps.append(timestamp)
        log_types.append(log_type)
        descriptions.append(description)

    # for i in range(len(timestamps)):
    #     print(timestamps[i])
    #     print(log_types[i])
    #     # print(len(log_types[i]))
    #     print(descriptions[i])
    #     print('\n')

    return timestamps, log_types, descriptions



