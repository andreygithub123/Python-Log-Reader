import operator


def ex1(log_types):
    numberOfErrors = 0
    numberOfDebugs = 0
    numberOfInfos = 0

    for log in log_types:

        log = log.upper()
        if log == 'ERROR':
            numberOfErrors += 1
        elif log == 'DEBUG':
            numberOfDebugs += 1
        elif log == 'INFO':
            numberOfInfos += 1

    #########################################################
    # Number of errors: 3240        |
    # Number of warnings: 3383      |=>13377
    # Number of infos: 6754         |
    print('Number of errors: ' + str(numberOfErrors))
    print('Number of warnings: ' + str(numberOfDebugs))
    print('Number of infos: ' + str(int(numberOfInfos/2)))
    #########################################################
    return

def ex2(descriptions):
    # for performance -> verify log_types first
    typeOfApp = []
    time = []
    front = 0
    frontTime = 0
    end = 0
    endTime = 0
    api = 0
    apiTime = 0

    # split the successful processes from the rest
    for process in descriptions:
        # we could add another condition to check if the process have also "ms"
        if "successfully" in process and "SYSTEM" not in process:
            process = process.split(" ")
            typeOfApp.append(process[0])
            time.append(int(process[len(process) - 1].strip("ms")))

    for i in range(len(typeOfApp)):
        if "front" in typeOfApp[i].lower():
            front += 1
            frontTime += time[i]
        elif "end" in typeOfApp[i].lower():
            end += 1
            endTime += time[i]
        elif "API" in typeOfApp[i].upper():
            api += 1
            apiTime += time[i]

    print("Front: " + str(front) + " - " + str(frontTime/front))
    print("End: " + str(end) + " - " + str(endTime/end))
    print("API: " + str(api) + " - " + str(apiTime/api))
    return

def ex3(descriptions):
    # for performance -> verify log_types first
    failedFrontNumber = 0
    failedEndNumber = 0
    failedAPINumber = 0
    failedSystemNumber = 0

    for process in descriptions:
        if "failed" in process:
            print(process)
            process = process.split(" ")
            if "front" in process[0].lower():
                failedFrontNumber += 1
            elif "end" in process[0].lower():
                failedEndNumber += 1
            elif "API" in process[0].upper():
                failedAPINumber += 1
            else:
                failedSystemNumber += 1

    print("Failed front: " + str(failedFrontNumber))
    print("Failed end: " + str(failedEndNumber))
    print("Failed API: " + str(failedAPINumber))
    print("Failed system: " + str(failedSystemNumber))

    return


def ex4(descriptions, log_types):
    apiFailsNumber = 0
    backendFailsNumber = 0
    frontendFailsNumber = 0
    sysFailsNumber = 0
    for i in range(len(log_types)):
        if log_types[i].lower() == "error":
            process = descriptions[i].split(" ")
            if process[0].lower() == "api":
                apiFailsNumber += 1
            elif "front" in process[0].lower():
                frontendFailsNumber += 1
            elif "back" in process[0].lower():
                backendFailsNumber += 1
            else:
                sysFailsNumber += 1

    my_dict = {}
    my_dict["API"] = apiFailsNumber
    my_dict["Frontend"] = frontendFailsNumber
    my_dict["System"] = sysFailsNumber
    my_dict["Backend"] = backendFailsNumber

    sorted_dict = dict(sorted(my_dict.items(), key = operator.itemgetter(1), reverse = True))
    print(sorted_dict)
    print(next(iter(sorted_dict)), sorted_dict.get(next(iter(sorted_dict))))

    return

def ex5(descriptions, log_types):
    apiSucNumber = 0
    backendSucNumber = 0
    frontendSucNumber = 0
    sysSucNumber = 0
    for i in range(len(log_types)):
        if log_types[i].lower() == "info":
            if "successfully" in descriptions[i]:
                process = descriptions[i].split(" ")
                if process[0].lower() == "api":
                    apiSucNumber += 1
                elif "front" in process[0].lower():
                    frontendSucNumber += 1
                elif "back" in process[0].lower():
                    backendSucNumber += 1
                else:
                    sysSucNumber += 1

    my_dict = {}
    my_dict["API"] = apiSucNumber
    my_dict["Frontend"] = frontendSucNumber
    my_dict["System"] = sysSucNumber
    my_dict["Backend"] = backendSucNumber

    sorted_dict = dict(sorted(my_dict.items(), key = operator.itemgetter(1), reverse = True))
    # print(sorted_dict)
    print(next(iter(sorted_dict)), sorted_dict.get(next(iter(sorted_dict))))

    return
