## Flask application deployed on Heroku.

* There are two Raspberry Pis Rpi1 and Rpi2, running their own PostgresSQL servers (I choose postgres because Heroku is compatible with postgres). 
* Both Rpis are populating their own postgresSQL servers with the data from theor GPIOS in the form of Temperature and flow rates of a heating system.
* For example, Rpi1 is taking Temeperaure data from heat pump device which has a source tank and a testing tank. In total it is taking 19 Temperature values via 
* SPI slave devices in the form of PT100 RTD sensors
* RPi2 takes 2 Flow rate values via I2C communication from 2 current loops (siemes FMAG magnetic flwo meter)
* Rpi1 is main primary engine (lets say) running flask server and heroku server too.
* Rpi1 remotly access the RPi2s poastgres database and store the table locally and also dumps it to heroku server to access.

*web app is available here [Heroku page ] (https://raspi-flask.herokuapp.com/)*

*gif looks like this:*

![](out2.gif)


*This is the work flow*


![Screenshot](Modbuss.png)


*But wait a minute, whats the need of all this drama?  why not use just the conventional data acquisition system? as shown below?*

![test image size]<img src="ALMEMO.jpg" width="400" height="400">

