from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
from flask import Flask, render_template, send_file, make_response, request
#app = Flask(__name__)
#import sqlite3

#import mysql.connector
#import MySQLdb as dB
import os
print ('ok')
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###Postgres shit@@@@@@@@@@@@@@
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import sensors
from models import flow

#import os.path
#########################################################
####fetching flowrates by remotly connecting to RP2######
#########################################################
##@@@@@@@@@@@@@@@@@@@@@
##Postgres in app.py@@@
##@@@@@@@@@@@@@@@@@@@@@

import sys
#import RPi.GPIO as GPIO
#import sqlite3
from time import sleep

#import board
#import busio
#import digitalio

#import adafruit_max31865

import psycopg2

#import mysql.connector

print ('ok')
#@app.route("/data/db")

#import psycopg2
from psycopg2 import Error

#print(db_connection)
#conn = psycopg2.connect(database = "TemaccessToRemoteRp2", user = "yogi", password = "bittoo", host = "127.0.0.1", port = "5432")
#print ("Opened database successfully")
#c = conn.cursor()

def getLastData():
        #conn=sqlite3.connect(db_path, check_same_thread=False)
        #connectionR = dB.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
        #cR = connectionR.cursor()
        	#connR = psycopg2.connect(database = "TemaccessToRemoteRp2", user = "yogi", password = "bittoo", host = "localhost", port = "5432")
        DATABASE_URL = os.environ['DATABASE_URL']
        connR = psycopg2.connect(DATABASE_URL, sslmode='require')
        ###connR = psycopg2.connect(database = "TemaccessToRemoteRp2", user = "yogi", password = "bittoo", host = "localhost", port = "5432")
        print ("Opened database remotely successfully")
        cR = connR.cursor()
        cR.execute("SELECT * FROM flow ORDER BY id DESC LIMIT 1")
        resultsR = cR.fetchall()
        print (resultsR)
        for rowR in resultsR:
                idR = str(rowR[0])
                dateTimeR = str(rowR[1])
                flowHP = rowR[2]
                flowLoad = rowR[3]
                #print (flowLoad)
        connR.close()

        ###connL = psycopg2.connect(database = "TemaccessToRemoteRp2", user = "yogi", password = "bittoo", host = "localhost", port = "5432")
        DATABASE_URL = os.environ['DATABASE_URL']
        connL = psycopg2.connect(DATABASE_URL, sslmode='require')

        print ("Opened database locally successfully")
        cL = connL.cursor()
        cL.execute("SELECT * FROM sensors ORDER BY id DESC LIMIT 1")
        results  = cL.fetchall()
        print (results)
        for row in results:
                id = str(row[0])
                dateTime = str(row[1])
                #time = str(row[-1])
                tempAmbient = row[2]
                tempTopTestingHpCircuit = row[3]
                tempBottomTestingHpCircuit = row[4]
                tempTopSource = row[5]
                tempTLoadtank = row[6]
                tempTopTestingLoadCircuit = row[7]
                tempLoadMix= row[8]
                tempBottomSource = row[9]
                tempBottomLoadCircuit = row[10]
                temStrat1 =  row[11]
                temStrat3 =  row[12]
                temStrat5 =  row[13]
                temStrat7 =  row[14]
                temStrat9 =  row[15]
                temStrat11 =  row[16]
                temStrat13 =  row[17]
                temStrat15 =  row[18]
                temStrat17 =  row[19]
                temStrat19 =  row[20]
        connL.close()
        return id, dateTime, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1, temStrat3, temStrat5, temStrat7, temStrat9, temStrat11, temStrat13, temStrat15, temStrat17, temStrat19, flowHP, flowLoad

#getLastData()


def getHistData (numSamples):
	#curs.execute("SELECT * FROM temSensor ORDER BY id DESC LIMIT "+str(numSamples))
	###connL = psycopg2.connect(database = "TemaccessToRemoteRp2", user = "yogi", password = "bittoo", host = "localhost", port = "5432")
	DATABASE_URL = os.environ['DATABASE_URL']
	connL = psycopg2.connect(DATABASE_URL, sslmode='require')
	print ("Opened database locally successfully")
	cL = connL.cursor()
	cL.execute("SELECT * FROM sensors ORDER BY id DESC LIMIT "+str(numSamples))
	data = cL.fetchall()
	print (data)
	Id = []
	DateTime = []
	#Time = []
	TempAmbient = []
	TempTopTestingHpCircuit = []
	TempBottomTestingHpCircuit = []
	TempTopSource =  []
	TempTLoadtank = []
	TempTopTestingLoadCircuit = []
	TempLoadMix = []
	TempBottomSource = []
	TempBottomLoadCircuit = []
	TemStrat1 = []
	TemStrat3 = []
	TemStrat5 = []
	TemStrat7 = []
	TemStrat9 = []
	TemStrat11 = []
	TemStrat13 = []
	TemStrat15 = []
	TemStrat17 = []
	TemStrat19 = []

	for row in reversed(data):
		Id.append(row[0])
		DateTime.append(row[1])
		#Time.append(row[-1])
		TempAmbient.append(row[2])
		TempTopTestingHpCircuit.append(row[3])
		TempBottomTestingHpCircuit.append(row[4])
		TempTopSource.append(row[5])
		TempTLoadtank.append(row[6])
		TempTopTestingLoadCircuit.append(row[7])
		TempLoadMix.append(row[8])
		TempBottomSource.append(row[9])
		TempBottomLoadCircuit.append(row[10])
		TemStrat1.append(row[11])
		TemStrat3.append(row[12])
		TemStrat5.append(row[13])
		TemStrat7.append(row[14])
		TemStrat9.append(row[15])
		TemStrat11.append(row[16])
		TemStrat13.append(row[17])
		TemStrat15.append(row[18])
		TemStrat17.append(row[19])
		TemStrat19.append(row[20])
	#cR.execute("SELECT * FROM flowReadings  ORDER BY id DESC LIMIT "+str(numSamples))
	#dataR = cR.fetchall()
	##connR = psycopg2.connect(database = "TemaccessToRemoteRp2", user = "yogi", password = "bittoo", host = "localhost", port = "5432")
	DATABASE_URL = os.environ['DATABASE_URL']
	connR = psycopg2.connect(DATABASE_URL, sslmode='require')
	print ("Opened database remotely successfully")
	cR = connR.cursor()
	cR.execute("SELECT * FROM flow  ORDER BY id DESC LIMIT "+str(numSamples))
	resultsR = cR.fetchall()
	IdR = []
	DateTimeR = []
	flowHP = []
	flowLoad = []
	print (flowLoad)
	for rowR in reversed(resultsR):
		IdR.append(rowR[0])
		DateTimeR.append(rowR[1])
		#Time.append(row[-1])
		flowHP.append(rowR[2])
		flowLoad.append(rowR[3])
	return Id, DateTime, TempAmbient, TempTopTestingHpCircuit, TempBottomTestingHpCircuit , TempTopSource, TempTLoadtank, TempTopTestingLoadCircuit, TempLoadMix, TempBottomSource, TempBottomLoadCircuit , TemStrat1, TemStrat3, TemStrat5, TemStrat7, TemStrat9, TemStrat11, TemStrat13, TemStrat15, TemStrat17, TemStrat19, flowHP, flowLoad

#getHistData()


def maxRowsTable():
    #curs.execute("select COUNT(id) from  temSensor")
    #results  = curs.fetchall()
    ##connL = psycopg2.connect(database = "TemaccessToRemoteRp2", user = "yogi", password = "bittoo", host = "localhost", port = "5432")
    DATABASE_URL = os.environ['DATABASE_URL']
    connL = psycopg2.connect(DATABASE_URL, sslmode='require')

    print ("maxRowsTable Opened database locally successfully")
    cL = connL.cursor()
    cL.execute("select COUNT(id) from  sensors")
    results  = cL.fetchall()
    for row in results:
        maxNumberRows=row[0]
    return maxNumberRows
# define and initialize global variables
global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
	numSamples = 100

@app.route("/")
def index():
    id, dateTime, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19, flowHP, flowLoad = getLastData()
    templateData = {
        'id': id,
	'dateTime': dateTime,
	#'time' : time,
	'AmbientTem':tempAmbient,
	'TopTestingtemHPcircuit':tempTopTestingHpCircuit,
	'BottomtestingtemHPcircuit': tempBottomTestingHpCircuit,
	'TemTopSource': tempTopSource,
	'LoadtankTem': tempTLoadtank,
	'Toptemoftestingtankloadcircuit': tempTopTestingLoadCircuit,
	'Mixtematload': tempLoadMix,
	'sourcetankbottomtemp': tempBottomSource,
	'Testingbottomloadcircuit': tempBottomLoadCircuit,
	'StratT1': temStrat1,
	'StratT3': temStrat3,
	'StratT5':  temStrat5,
	'StratT7':  temStrat7,
	'StratT9':  temStrat9,
	'StratT11':  temStrat11,
	'StratT13':  temStrat13,
	'StratT15':  temStrat15,
        'StratT17':  temStrat17,
	'StratT19':  temStrat19,
        'FlowHP': flowHP,
        'FlowLoad': flowLoad
        }
    return render_template('index.html', **templateData)



@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    global numSamples

    numSamples = int (request.form['numSamples'])
    numMaxSamples = maxRowsTable()
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples-1)
    id, dateTime, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19, flowHP, flowLoad = getLastData()
    templateData = {
        'id': id,
        'dateTime': dateTime,
        #'time' : time,
        'AmbientTem':tempAmbient,
        'TopTestingtemHPcircuit': tempTopTestingHpCircuit,
        'BottomtestingtemHPcircuit': tempBottomTestingHpCircuit,
        'TemTopSource': tempTopSource,
        'LoadtankTem': tempTLoadtank,
        'Toptemoftestingtankloadcircuit': tempTopTestingLoadCircuit,
        'Mixtematload': tempLoadMix,
        'sourcetankbottomtemp': tempBottomSource,
        'Testingbottomloadcircuit': tempBottomLoadCircuit,
        'StratT1': temStrat1,
        'StratT3': temStrat3,
        'StratT5':  temStrat5,
        'StratT7':  temStrat7,
        'StratT9':  temStrat9,
        'StratT11':  temStrat11,
        'StratT13':  temStrat13,
        'StratT15':  temStrat15,
        'StratT17':  temStrat17,
        'StratT19':  temStrat19,
        'FlowHP': flowHP,
        'FlowLoad': flowLoad
        }
    return render_template('index.html', **templateData)



@app.route('/plot/temp')
def plot_temp():
        #times, temps, hums = getHistData(numSamples)
        #times, temps, hums = getHistData(numSamples)
        #flowHP, flowLoad] 'HP flow rate ','Load Flow Rate'
        id, dateTime, tempAmbient,tempTopTestingHpCircuit,tempBottomTestingHpCircuit, tempTopSource,tempTLoadtank,tempTopTestingLoadCircuit, \
        tempLoadMix,tempBottomSource,tempBottomLoadCircuit, temStrat1,temStrat3,temStrat5,temStrat7,temStrat9, temStrat11,temStrat13,temStrat15,temStrat17,temStrat19, flowHP, flowLoad = getHistData(numSamples)
        plot_var = [tempTopSource, tempBottomSource, tempTopTestingHpCircuit, tempBottomTestingHpCircuit, tempTopTestingLoadCircuit, tempBottomLoadCircuit, tempTLoadtank, tempLoadMix, flowHP, flowLoad]
        title_bar = ['Source tank top', 'Source tank bottom', 'Testing top HP Circuit', 'Testing bottom HP Circuit', 'Testing top Load Circuit', 'testing bottom load circuit', 'Load tank tem.', 'Mix Load tem.', 'HP flow rate ','Load Flow Rate']
        fig = plt.figure(figsize=(15,15))
        for i in  range (0, len(plot_var)):
            ys = plot_var[i]
            xs = range (numSamples)
            #print (ys)
            #ys = tempAmbient
            #fig = Figure()
            axis = fig.add_subplot(3,4, i+1)
            plt.subplots_adjust( wspace = 1.0, hspace = 1.0)
            #fig.tight_layout()
            axis.set_title(title_bar[i])
            axis.set_xlabel("Samples")
            axis.grid(True)
            #xs = range(numSamples)
            axis.plot(xs, ys)
            canvas = FigureCanvas(fig)
            output = io.BytesIO()
            canvas.print_png(output)
            response = make_response(output.getvalue())
            response.mimetype = 'image/png'
        return response



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=False)





