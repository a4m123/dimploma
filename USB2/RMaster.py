import RListenWater, RCloseValve, RSendEMail

resultWaterLeakage = 0
resultSendMail = 0
resultCloseValve = 0

resultWaterLeakage = RListenWater.main()
if (resultWaterLeakage == 1):
    resultCloseValve = RCloseValve.main()
    resultSendMail = RSendEMail.main(resultCloseValve)
    print(str(resultSendMail) + " - resultSendMail")