import sqlite3
import bcrypt
from sqlalchemy import false, true
def controlUser(nameInput = "admin", passwordInput = b"1qazxsw2"):
    password = b"1qazxsw2"
    password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    connectDB = sqlite3.connect("USB2/RaspPi/users.db")
    cursorDB = connectDB.cursor()

    for row in cursorDB.execute('SELECT * FROM user;'):
        print (row[2])
        if ((nameInput == row[1]) and bcrypt.checkpw(passwordInput, row[2].encode('utf-8'))):
            connectDB.close()
            print("true")
            return(True)
        else:
            pass
    connectDB.close()
    print("false")
    return(false)

if (__name__ == "__main__"):
    controlUser()