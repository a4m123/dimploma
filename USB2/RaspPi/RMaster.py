import json
import RListenWater, RCloseValve, RSendEMail

resultWaterLeakage = 0
resultSendMail = 0
resultCloseValve = 0

resultWaterLeakage = RListenWater.main()
if (resultWaterLeakage == 1):
    resultCloseValve = RCloseValve.main(0)
    information = {'waterLeakage': resultWaterLeakage, 'closedValve': resultCloseValve, 'sendedMail': resultSendMail}
    infoFile = open("info.json", "w")
    json.dump(information, infoFile)
    resultSendMail = RSendEMail.main(resultCloseValve)

    
