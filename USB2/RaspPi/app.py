import time
import cv2 
from flask import Flask, render_template, Response, request
import json
import RCloseValve

app = Flask(__name__)
def generateVideo():
    cameraCapture = cv2.VideoCapture(-1)
    while(cameraCapture.isOpened()):
        returnStatus, image = cameraCapture.read()
        if returnStatus == True:
            image = cv2.resize(image, (0,0), fx=2, fy=2) 
            frame = cv2.imencode('.jpg', image)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
        else: 
            break

def getInfoFromJSON(jsonFile):
    jsonLoad = (json.load(jsonFile))
    jsonDumps = json.dumps(jsonLoad, indent=4) 
    jsonTempStr = jsonDumps.replace(",", "")
    jsonStr = jsonTempStr.split()
    return jsonStr

@app.route('/')
def index():
    jsonOpen = open("info.json", "r")
    jsonStr = getInfoFromJSON(jsonOpen)
    waterLeakageInfo = "есть протечка" if (jsonStr[2] == str(1)) else "нет протечки"
    closedValveInfo = "закрыт" if (jsonStr[4] == str(1)) else "открыт"
    sendedMailInfo = "да" if (jsonStr[6] == str(1)) else "нет"
    webInterruptInfo = "есть вмешательство" if (jsonStr[8] == str(1)) else "нет вмешательства"
#    return render_template('index.html', waterLeakage = jsonStr[2], closedValve = jsonStr[4], sendedMail=jsonStr[6], webInterrupt=jsonStr[8])       
    return render_template('index.html', waterLeakage = waterLeakageInfo, closedValve = closedValveInfo, sendedMail=sendedMailInfo, webInterrupt=webInterruptInfo)       

@app.route('/video')
def video():
    return Response(generateVideo(),
                   mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/button', methods = ['POST', 'GET'])
def button():
    #считывание текущей информации
    jsonOpen = open("info.json", "r")
    jsonStr = getInfoFromJSON(jsonOpen)
    print("jsonStr[4] = " +str(jsonStr[4]))
    if(jsonStr[4] == str(0)): #если кран не закрыт
        action = RCloseValve.main(0) #закрываем кран
        pass
    elif(jsonStr[4] == str(1)):
        action = RCloseValve.main(1)
        pass
    if ((action == -2) or (action == -1)):
        closedValveInfoNew = int(jsonStr[4])
    elif (action == 1):
        closedValveInfoNew = 0
    elif (action == 2):
        closedValveInfoNew = 1
    print ("app: closeVINew = " +str(closedValveInfoNew))
    #обновление информации о webInterrupt
    information = {'waterLeakage': int(jsonStr[2]), 'closedValve': int(closedValveInfoNew), 'sendedMail': int(jsonStr[6]), 'webInterrupt': 1}
    print ("app: closeVINew = " +str(information))
    print (jsonOpen.close())
    print ("app - ive tried to close jsonOpen")

    #заносим актуальную информацию 
    infoFile = open("info.json", "w")
    json.dump(information, infoFile)

    #обработка информации
    waterLeakageInfo = "есть протечка" if (jsonStr[2] == str(1)) else "нет протечки"
    closedValveInfo = "закрыт" if (jsonStr[4] == str(1)) else "открыт"
    sendedMailInfo = "да" if (jsonStr[6] == str(1)) else "нет"
    webInterruptInfo = "есть вмешательство" if (jsonStr[8] == str(1)) else "нет вмешательства"
    return render_template('index.html', waterLeakage = waterLeakageInfo, closedValve = closedValveInfo, sendedMail=sendedMailInfo, webInterrupt=webInterruptInfo)       
