def addEventLog():
    with open("sample2.txt", "a+") as eventLog:
        eventLog.seek(0)
        data = eventLog.read()
        if len(data) > 0 :
            eventLog.write("\n")
        eventLog.write()