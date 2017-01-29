from datetime import datetime
import json
import requests
import smtplib


URL = requests.get("https://uthgard.org/api/serverstatus")


def getServerStatus():
    server_status = URL.text
    server_status = json.loads(server_status)
    return server_status

def getPlayerCount():
    server_status = getServerStatus()
    player_count = server_status["Players"]  
    return player_count

def emailMe(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("", "")
    
    msg = message
    server.sendmail("", "", msg)
    server.quit()

def populationCheck():
    player_count = getPlayerCount()

    if player_count <= 4000:
        emailMe(str(player_count) + "\nPlay time!")
        print(str(player_count) + "\nPlay time!")
    else:
        print(str(player_count) + "\nCan't play.")
    

populationCheck()


''' Add sqlite3 db to track time trends '''
# TIME_TRENDS = {}
# time = datetime.now().isoformat()
# TIME_TRENDS.append(time. = getPlayerCount())
# print(TIME_TRENDS)
