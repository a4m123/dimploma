#!/usr/bin/env python3
import smtplib
import os
import time
from datetime import datetime
from email.mime.text import MIMEText

def send_email(message):
    reciever = "artem.malkin.2000@gmail.com"
    sender = "raspberrywaterleakage@gmail.com"
    password = "Zmpqfgh24"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        server.sendmail(sender, reciever, f"Subject: ACHTUNG!\n{msg.as_string()}")
        return(1)
    except Exception as _ex:
        return(-1)
    
def main(recievedCode):
    message = ""
    if (recievedCode == 1):
        message = "WATER LEAKEGE! - Valve is closed - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    elif (recievedCode == -1):
        message = "WATER LEAKEGE! - VALVE IS NOT CLOSED! - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S")    
    elif (recievedCode == 10):
        message = "No people in home. Valve is closed - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    elif (recievedCode == 11):
        message = "No people in home. Valve is not closed - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    elif (recievedCode == 20):
        message = "People are in home. Valve is opened - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return(send_email(message))

if __name__ == "__main__":
    main()