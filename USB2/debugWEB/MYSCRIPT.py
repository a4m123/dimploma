import json
import os

information = {'waterLeakage': 1, 'closedValve': 2, 'sendedMail': 3}
infoFile = open("info24.json", "w")
json.dump(information, infoFile)