import smtplib
import os

def send_email(message):
    reciever = "artem.malkin.2000@gmail.com"
    sender = "raspberrywaterleakage@gmail.com"
    password = "Zmpqfgh24"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, reciever, f"Subject: WATER LEAKAGE!\n{message}")
        return(1)
    except Exception as _ex:
        return(-1)
    
def main():
    message = "WATER LEAKEGE!"
    print(send_email(message))

if __name__ == "__main__":
    main()