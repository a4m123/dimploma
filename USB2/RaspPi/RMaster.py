import json
import RListenWater, RCloseValve, RSendEMail

resultWaterLeakage = 0
resultSendMail = 0
resultCloseValve = 0
resultWebInterrupt = 0
flag = 0

def getInfoFromJSON(jsonFile):
    jsonLoad = (json.load(jsonFile))
    jsonDumps = json.dumps(jsonLoad, indent=4) 
    jsonTempStr = jsonDumps.replace(",", "")
    jsonStr = jsonTempStr.split()
    return jsonStr

def main():
    while True:
        resultWaterLeakage = RListenWater.main()
        if ((resultWaterLeakage == 1) and (flag == 0)):
            jsonOpen = open("info.json", "r")
            jsonStr = getInfoFromJSON(jsonOpen)
            if (jsonStr[8] == str(0)): #если нет веб-вмешательства на изменение состояния крана
                resultCloseValve = RCloseValve.main(0)
                information = {'waterLeakage': resultWaterLeakage, 'closedValve': resultCloseValve, 'sendedMail': resultSendMail, 'webInterrupt': resultWebInterrupt}
                infoFile = open("info.json", "w")
                json.dump(information, infoFile)
                resultSendMail = RSendEMail.main(resultCloseValve)
            flag = 1
        elif (resultWaterLeakage == 0):
            flag = 0

if __name__ == "__main__":
    main()