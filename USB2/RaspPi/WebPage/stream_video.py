# -*- coding: utf-8 -*-
import time
import cv2 
from flask import Flask, render_template, Response
from scipy import rand
import json

app = Flask(__name__)

@app.route('/')
def index():
    jsonOpen = open("info.json", "r")
    jsonLoad = (json.load(jsonOpen))
    return render_template('index.html', infoFile = json.dumps(jsonLoad, indent=4))


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
        

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')  

