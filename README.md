## Flask application deployed on Heroku.

* There are two Raspberry Pis Rpi1 and Rpi2, running their own PostgresSQL servers (I choose postgres because Heroku is compatible with postgres). 
* Both Rpis are populating their own postgresSQL servers with the data from theor GPIOS in the form of Temperature and flow rates of a heating system.
* For example, Rpi1 is taking Temeperaure data from heat pump device which has a source tank and a testing tank. In total it is taking 19 Temperature values via 
* SPI slave devices in the form of PT100 RTD sensors
* RPi2 takes 2 Flow rate values via I2C communication from 2 current loops (siemes FMAG magnetic flwo meter)
* Rpi1 is main primary engine (lets say) running flask server and heroku server too.
* Rpi1 remotly access the RPi2s poastgres database and store the table locally and also dumps it to heroku server to access.


*web app is available here [Heroku page ] (https://raspi-flask.herokuapp.com/)*

![Screenshot](ModBUS.png)
![](out2.gif)
![Screenshot from 2020-12-03 17-41-47](https://user-images.githubusercontent.com/47416768/101060207-71286400-358f-11eb-9443-4cf3bb3b22c5.png)
![Screenshot from 2020-12-03 17-48-58](https://user-images.githubusercontent.com/47416768/101060566-d714eb80-358f-11eb-8aa6-ba4758201a39.png)
