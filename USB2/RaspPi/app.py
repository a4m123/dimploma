from crypt import methods
from email.policy import default
from pickle import TRUE
import time
from unicodedata import name
from sqlalchemy import false, true
import cv2 
from flask import Flask, redirect, render_template, Response, request
import json
import RCloseValve
import flask_login
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import bcrypt
#from sqlalchemy import false, true

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
doWeHavePermission = false

#БД
#id name    password    isAllowedToClose
#0  Иван    1234        Yes
#1  Мария   2345        No
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(16), nullable = False)
    password = db.Column(db.Integer, nullable = False)
    isAllowedToClose = db.Column(db.Boolean, default = True)

def createUser():
    user = User(name = "Admin", password = bcrypt.hashpw(b"1qazxsw2", bcrypt.gensalt()))
    db.session.add(user)
    db.session.commit()

def checkUsers():
    users = User.query.order_by(User.id).all()
    return(users)

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

def controlUser(nameInput = "admin", passwordInput = b"1qazxsw2"):
    connectDB = sqlite3.connect("USB2/RaspPi/users.db")
    cursorDB = connectDB.cursor()

    for row in cursorDB.execute('SELECT * FROM user;'):
        if ((nameInput == row[1]) and bcrypt.checkpw(passwordInput, row[2].encode('utf-8'))):
            connectDB.close()
            return(True)
        else:
            pass
    connectDB.close()
    return(False)

@app.route('/login', methods=['POST','GET'])
def login():
    if (request.method != "POST"):
        return render_template('login.html')       

    elif (request.method == "POST"):
        name = request.form['name']
        password = request.form['password']
        if (controlUser(nameInput = name, passwordInput = password.encode('utf-8')) == True):
            doWeHavePermission = true
            return redirect('/')
        else:
            doWeHavePermission = false
            return render_template('login.html')  
                 
 
@app.route('/')
def index():
    if (doWeHavePermission == true):
        jsonOpen = open("info.json", "r")
        jsonStr = getInfoFromJSON(jsonOpen)
        waterLeakageInfo = "есть протечка" if (jsonStr[2] == str(1)) else "нет протечки"
        closedValveInfo = "закрыт" if (jsonStr[4] == str(1)) else "открыт"
        sendedMailInfo = "да" if (jsonStr[6] == str(1)) else "нет"
        webInterruptInfo = "есть вмешательство" if (jsonStr[8] == str(1)) else "нет вмешательства"
        return render_template('index.html', waterLeakage = waterLeakageInfo, closedValve = closedValveInfo, sendedMail=sendedMailInfo, webInterrupt=webInterruptInfo, users = checkUsers())       
    else:
        return render_template('index.html')

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