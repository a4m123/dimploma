import RListenWater, RCloseValve, RSendEMail

resultWaterLeakage = 0
resultSendMail = 0
resultCloseValve = 0

resultWaterLeakage = RListenWater.main()
if (resultWaterLeakage == 1):
    resultCloseValve = RCloseValve.main(0)
    print(str(resultCloseValve) + "  resultClV")
    resultSendMail = RSendEMail.main(resultCloseValve)
    print(str(resultSendMail) + "  resultSendMail")
    information = {'waterLeakage': resultWaterLeakage, 'closedValve': resultCloseValve, 'sendedMail': resultSendMail}
    infoFile = open("info.json", "w")
    