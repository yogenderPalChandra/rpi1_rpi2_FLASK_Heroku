

import psycopg2
import time
#connR = psycopg2.connect(database = "flow", user = "yogi", password = "bittoo", host = "10.208.8.121", port = "5432")
#print ("Opened database remotely successfully")
#cR = connR.cursor()
#cR.execute("SELECT * FROM flowReadings ORDER BY id DESC LIMIT 1")
#resultsR = cR.fetchall()
connFlowL = psycopg2.connect(database = "TemaccessToRemoteRp2", user = "yogi", password = "bittoo", host = "localhost", port = "5432")
CfL =   connFlowL.cursor()
while True:
    connR = psycopg2.connect(database = "flow", user = "yogi", password = "bittoo", host = "10.208.8.121", port = "5432")
    print ("Opened database remotely successfully")
    cR = connR.cursor()
    cR.execute("SELECT * FROM flowReadings ORDER BY id DESC LIMIT 1")
    resultsR = cR.fetchall()
    for rowR in resultsR:
        idR = str(rowR[0])
        dateTimeR = str(rowR[1])
        flowHP = rowR[2]
        flowLoad = rowR[3]
        CfL.execute("INSERT INTO flow (id, ts, flowhp, flowload) VALUES (%s, %s, %s, %s)", (idR,dateTimeR , flowHP, flowLoad))
        connFlowL.commit()
    time.sleep(1)
