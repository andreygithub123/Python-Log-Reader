import operator

def ex1(logs):
    info_logs = [0, 0, 0, 0]
    debug_logs = [0, 0, 0, 0]
    error_logs = [0, 0, 0, 0]

    for log in logs:
        if log["log_type"] == "INFO":
            if log["app"] == "API":
                info_logs[0] += 0.5
            elif log["app"] == "FrontendApp":
                info_logs[1] += 0.5
            elif log["app"] == "BackendApp":
                info_logs[2] += 0.5
            elif log["app"] == "SYSTEM":
                info_logs[3] += 0.5

        elif log["log_type"] == "DEBUG":
            if log["app"] == "API":
                debug_logs[0] += 1
            elif log["app"] == "FrontendApp":
                debug_logs[1] += 1
            elif log["app"] == "BackendApp":
                debug_logs[2] += 1
            elif log["app"] == "SYSTEM":
                debug_logs[3] += 1

        elif log["log_type"] == "ERROR":
            if log["app"] == "API":
                error_logs[0] += 1
            elif log["app"] == "FrontendApp":
                error_logs[1] += 1
            elif log["app"] == "BackendApp":
                error_logs[2] += 1
            elif log["app"] == "SYSTEM":
                error_logs[3] += 1

    dict1 = {   "API": int(info_logs[0]),
                "Frontend": int(info_logs[1]),
                "Backend": int(info_logs[2]),
                "System": int(info_logs[3])}
    dict2 = {   "API": int(debug_logs[0]),
                "Frontend": int(debug_logs[1]),
                "Backend": int(debug_logs[2]),
                "System": int(debug_logs[3])}
    dict3 = {   "API": int(error_logs[0]),
                "Frontend": int(error_logs[1]),
                "Backend": int(error_logs[2]),
                "System": int(error_logs[3])}
    dict = {"INFO": dict1,
            "DEBUG": dict2,
            "ERROR": dict3}

    # print(dict)

    return dict

def ex2(logs):
    front = 0
    frontTime = 0
    end = 0
    endTime = 0
    api = 0
    apiTime = 0

    for log in logs:
        if "run_time" in log:
            if "status" in log and log["status"] == 1:
                if "FrontendApp" == log['app']:
                    front += 1
                    frontTime += int(log['run_time'])
                elif "BackendApp" == log['app']:
                    end += 1
                    endTime += int(log['run_time'])
                elif "API" == log['app']:
                    api += 1
                    apiTime += int(log['run_time'])

    # print("Front: " + str(front) + " - " + str(frontTime/front))
    # print("End: " + str(end) + " - " + str(endTime/end))
    # print("API: " + str(api) + " - " + str(apiTime/api))

    return front, frontTime/front, end, endTime/end, api, apiTime/api

def ex3(logs):
    failed_front_number = 0
    failed_end_number = 0
    failed_api_number = 0
    failed_system_number = 0

    for log in logs:
        if "status" in log and log["status"] == -1:
            if "FrontendApp" == log['app']:
                failed_front_number += 1
            elif "BackendApp" == log['app']:
                failed_end_number += 1
            elif "API" == log['app']:
                failed_api_number += 1
            elif "SYSTEM" == log['app']:
                failed_system_number += 1

    # print("Failed front: " + str(failed_front_number))
    # print("Failed end: " + str(failed_end_number))
    # print("Failed API: " + str(failed_api_number))
    # print("Failed system: " + str(failed_system_number))

    return failed_front_number, failed_end_number, failed_api_number, failed_system_number


def ex4(logs):
    api_fails_number = 0
    backend_fails_number = 0
    frontend_fails_number = 0
    sys_fails_number = 0

    for log in logs:
        if "status" in log and log["status"] == -1:
            if "FrontendApp" == log['app']:
                frontend_fails_number += 1
            elif "BackendApp" == log['app']:
                backend_fails_number += 1
            elif "API" == log['app']:
                api_fails_number += 1
            elif "SYSTEM" == log['app']:
                sys_fails_number += 1

    my_dict = {"API": api_fails_number,
               "Frontend": frontend_fails_number,
               "System": sys_fails_number,
               "BackendApp": backend_fails_number}

    sorted_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))
    # print(next(iter(sorted_dict)), sorted_dict.get(next(iter(sorted_dict))))

    return next(iter(sorted_dict)), sorted_dict.get(next(iter(sorted_dict)))

def ex5(logs):
    api_suc_number = 0
    backend_suc_number = 0
    frontend_suc_number = 0
    sys_suc_number = 0

    for log in logs:
        if "status" in log and log["status"] == 1:
            if "FrontendApp" == log['app']:
                frontend_suc_number += 1
            elif "BackendApp" == log['app']:
                backend_suc_number += 1
            elif "API" == log['app']:
                api_suc_number += 1
            elif "SYSTEM" == log['app']:
                sys_suc_number += 1

    my_dict = {"API": api_suc_number,
               "Frontend": frontend_suc_number,
               "System": sys_suc_number,
               "BackendApp": backend_suc_number}

    sorted_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))
    # print(next(iter(sorted_dict)), sorted_dict.get(next(iter(sorted_dict))))

    return next(iter(sorted_dict)), sorted_dict.get(next(iter(sorted_dict)))
def ex6(logs):
    fails = [0, 0, 0]

    for log in logs:
        if "status" in log and log["status"] == -1:
            if log["timestamp"] < "08:00:00":
                fails[0] += 1
            elif log["timestamp"] < "16:00:00":
                fails[1] += 1
            else:
                fails[2] += 1

    if max(fails) == fails[0]:
        print("Most fails in: 00:00:00 - 07:59:59 in total: " + str(fails[0]))
        return fails[0]
    elif max(fails) == fails[1]:
        print("Most fails in: 08:00:00 - 15:59:59 in total: " + str(fails[1]))
        return fails[1]
    elif max(fails) == fails[2]:
        print("Most fails in: 16:00:00 - 23:59:59 in total: " + str(fails[2]))
        return fails[2]

def ex7(logs):
    shortest_runtime_api = []
    shortest_runtime_backend = []
    shortest_runtime_frontend = []
    longest_runtime_api = []
    longest_runtime_backend = []
    longest_runtime_frontend = []

    min_api = -1
    min_backend = -1
    min_frontend = -1

    max_api = -1
    max_backend = -1
    max_frontend = -1

    sorted_log_entries = sorted(logs, key=lambda x: int(x.get('run_time', 0)))

    for log in sorted_log_entries:
        if "status" in log and log["status"] == 1:
            if log["app"] == "API":
                if min_api == -1:
                    min_api = int(log['run_time'])
                    shortest_runtime_api.append(log)
                elif min_api == int(log['run_time']):
                    shortest_runtime_api.append(log)
                elif min_api > int(log['run_time']):
                    min_api = int(log['run_time'])
                    shortest_runtime_api.clear()
                    shortest_runtime_api.append(log)
                if max_api < int(log['run_time']):
                    max_api = int(log['run_time'])
                    longest_runtime_api.clear()
                    longest_runtime_api.append(log)
                elif max_api == int(log['run_time']):
                    longest_runtime_api.append(log)
            elif log["app"] == "FrontendApp":
                if min_frontend == -1:
                    min_frontend = int(log['run_time'])
                    shortest_runtime_frontend.append(log)
                elif min_frontend == int(log['run_time']):
                    shortest_runtime_frontend.append(log)
                elif min_frontend > int(log['run_time']):
                    min_frontend = int(log['run_time'])
                    shortest_runtime_frontend.clear()
                    shortest_runtime_frontend.append(log)
                if max_frontend < int(log['run_time']):
                    max_frontend = int(log['run_time'])
                    longest_runtime_frontend.clear()
                    longest_runtime_frontend.append(log)
                elif max_frontend == int(log['run_time']):
                    longest_runtime_frontend.append(log)
            elif log["app"] == "BackendApp":
                if min_backend == -1:
                    min_backend = int(log['run_time'])
                    shortest_runtime_backend.append(log)
                elif min_backend == int(log['run_time']):
                    shortest_runtime_backend.append(log)
                elif min_backend > int(log['run_time']):
                    min_backend = int(log['run_time'])
                    shortest_runtime_backend.clear()
                    shortest_runtime_backend.append(log)
                if max_backend < int(log['run_time']):
                    max_backend = int(log['run_time'])
                    longest_runtime_backend.clear()
                    longest_runtime_backend.append(log)
                elif max_backend == int(log['run_time']):
                    longest_runtime_backend.append(log)

    # for log in shortest_runtime_api:
    #     print("API shortest runtime: " + log["timestamp"] + " - " + log["run_time"])
    # for log in shortest_runtime_frontend:
    #     print("Frontend shortest runtime: " + log["timestamp"] + " - " + log["run_time"])
    # for log in shortest_runtime_backend:
    #     print("Backend shortest runtime: " + log["timestamp"] + " - " + log["run_time"])
    #
    # for log in longest_runtime_api:
    #     print("API longest runtime: " + log["timestamp"] + " - " + log["run_time"])
    # for log in longest_runtime_frontend:
    #     print("Frontend longest runtime: " + log["timestamp"] + " - " + log["run_time"])
    # for log in longest_runtime_backend:
    #     print("Backend longest runtime: " + log["timestamp"] + " - " + log["run_time"])

    return shortest_runtime_api, shortest_runtime_backend, shortest_runtime_frontend, longest_runtime_api, longest_runtime_backend, longest_runtime_frontend

def ex8(logs):
    sorted_log_entries = sorted(logs, key=lambda x: x.get('timestamp'))

    api = 0
    backend = 0
    frontend = 0
    max_log_hour = 0
    most_log_hour = ""

    present_hour = sorted_log_entries[0]["timestamp"][:2]
    for log in sorted_log_entries:
        if log["timestamp"][:2] != present_hour:
            if max_log_hour < api + backend + frontend:
                max_log_hour = api + backend + frontend
                most_log_hour = present_hour

            api = 0
            backend = 0
            frontend = 0
            present_hour = log["timestamp"][:2]

        if log["app"] == "API" and log["log_type"] == "INFO":
            api += 0.5
        else:
            api += 1

        if log["app"] == "FrontendApp" and log["log_type"] == "INFO":
            frontend += 0.5
        else:
            frontend += 1
        if log["app"] == "BackendApp" and log["log_type"] == "INFO":
            backend += 0.5
        else:
            backend += 1

    # print("Busiest hour: " + most_log_hour + " with " + str(int(max_log_hour)) + " logs")

    return most_log_hour, max_log_hour

def ex9(logs):
    dict = ex1(logs)
    total_logs_front = dict["INFO"]["Frontend"] + dict["DEBUG"]["Frontend"] + dict["ERROR"]["Frontend"]
    total_logs_end = dict["INFO"]["Backend"] + dict["DEBUG"]["Backend"] + dict["ERROR"]["Backend"]
    total_logs_api = dict["INFO"]["API"] + dict["DEBUG"]["API"] + dict["ERROR"]["API"]
    total_logs_system = dict["INFO"]["System"] + dict["DEBUG"]["System"] + dict["ERROR"]["System"]

    # print("Frontend failure rate: " + str(dict["ERROR"]["Frontend"] / total_logs_front * 100) + "%")
    # print("Backend failure rate: " + str(dict["ERROR"]["Backend"] / total_logs_end * 100) + "%")
    # print("API failure rate: " + str(dict["ERROR"]["API"] / total_logs_api * 100) + "%")
    # print("System failure rate: " + str(dict["ERROR"]["System"] / total_logs_system * 100) + "%")

    percentage = {"Frontend": dict["ERROR"]["Frontend"] / total_logs_front * 100,
            "Backend": dict["ERROR"]["Backend"] / total_logs_end * 100,
            "API": dict["ERROR"]["API"] / total_logs_api * 100,
            "System": dict["ERROR"]["System"] / total_logs_system * 100}

    return percentage

