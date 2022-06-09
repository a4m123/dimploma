import time
import cv2 
from flask import Flask, render_template, Response, request
import json
import RCloseValve

app = Flask(__name__)
def gen():
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (0,0), fx=2, fy=2) 
            frame = cv2.imencode('.jpg', img)[1].tobytes()
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

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                   mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/button', methods = ['POST', 'GET'])
def button():
    #считывание текущей информации
    jsonOpen = open("info.json", "r")
    jsonStr = getInfoFromJSON(jsonOpen)
    if(jsonStr[4] == str(0)):
        action = RCloseValve.main(0)
        pass
    elif(jsonStr[4] == str(1)):
        action = RCloseValve.main(1)
        pass
    action = 1
    if ((action == -2) or (action == -1)):
        closedValveInfoNew = int(jsonStr[4])
    elif (action == 1):
        closedValveInfoNew = 1
    elif (action == 2):
        closedValveInfoNew = 0
    #обновление информации о webInterrupt
    information = {'waterLeakage': int(jsonStr[2]), 'closedValve': closedValveInfoNew, 'sendedMail': int(jsonStr[6]), 'webInterrupt': 1}
    jsonOpen.close()

    #заносим актуальную информацию 
    infoFile = open("info.json", "w")
    json.dump(information, infoFile)

    #обработка информации
    waterLeakageInfo = "есть протечка" if (jsonStr[2] == str(1)) else "нет протечки"
    closedValveInfo = "закрыт" if (jsonStr[4] == str(1)) else "открыт"
    sendedMailInfo = "да" if (jsonStr[6] == str(1)) else "нет"
    webInterruptInfo = "есть вмешательство" if (jsonStr[8] == str(1)) else "нет вмешательства"
    return render_template('index.html', waterLeakage = waterLeakageInfo, closedValve = closedValveInfo, sendedMail=sendedMailInfo, webInterrupt=webInterruptInfo)       
