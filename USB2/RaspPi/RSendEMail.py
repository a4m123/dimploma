#!/usr/bin/env python3
import smtplib
import os
import time
from datetime import datetime
from email.mime.text import MIMEText
import socket

def send_email(message):  
    launch_webpage()
    reciever = "artem.malkin.2000@gmail.com"
    sender = "raspberrywaterleakage@gmail.com"
    password = "1324564"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        server.sendmail(sender, reciever, f"Subject: ACHTUNG!\n{msg.as_string()}")
        return(1)
    except Exception as _ex:
        return(-1)

def addEventLog(message):
    with open("eventLog.txt", "a+") as eventLog:
        eventLog.seek(0)
        data = eventLog.read()
        if len(data) > 0 :
            eventLog.write("\n")
        eventLog.write(message)

def launch_webpage():
    os.system("flask run")

def main(recievedCode):
    hostname=socket.gethostname()   
    IPAdrress=socket.gethostbyname(hostname)   
    message = ""
    if (recievedCode == 1):
        message = "WATER LEAKEGE! - Valve is closed - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S" + ". Check web-page: " + IPAdrress + ":5000/login")
    elif (recievedCode == -1):
        message = "WATER LEAKEGE! - VALVE IS NOT CLOSED! - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S" + ". Check web-page: " + IPAdrress + ":5000/login")    
    elif (recievedCode == 10):
        message = "No people in home. Valve is closed - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S" + ". Check web-page: " + IPAdrress + ":5000/login")
    elif (recievedCode == 11):
        message = "No people in home. Valve is not closed - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S" + ". Check web-page: " + IPAdrress + ":5000/login")
    elif (recievedCode == 20):
        message = "People are in home. Valve is opened - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S" + ". Check web-page: " + IPAdrress + ":5000/login")
    addEventLog(message)
    return(send_email(message))

if __name__ == "__main__":
    main()
