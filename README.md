Flask application.

Whats is going on here?

There are two Raspberry Pis lets call them Rpi1 and Rpi2, running their own PostgresSQL servers (I choose postgres because Heroku is compatible with postgres). 

Both Rpis are popiulating their own postgresSQL servers with the data from theor GPIOS in the form of Temperature and flow rates of a heating system.

For example, Rpi1 is taking Temeperaure data from heat pump device which has a asource tank and a testing tank. In total it is taking 19 Temperature values via 

SPI slave devices in the form of PT100 RTD sensors

RPi2 takes 2 Flow rate values via I2C communication from 2 current loops (siemes FMAG magnetic flwo meter)

Rpi1 is main primary engine (lets say) running flask server and heroku server too.

Rpi1 remotly access the RPi2s poastgres database and stored teh table locally and also throws it to heroku server to access.

https://raspi-flask.herokuapp.com/
