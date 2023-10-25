#!/usr/bin/env python3
import minimalmodbus, serial

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)

## Read temperature (PV = ProcessValue) ##

#instrument.serial.port                     # this is the serial port name
instrument.serial.baudrate = 9600         # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
#instrument.serial.parity   = serial.PARITY_ODD # serial.PARITY_NONE
#instrument.serial.parity   = serial.PARITY_EVEN # serial.PARITY_NONE
#instrument.serial.parity   = serial.PARITY_ODD # serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 3.05          # seconds

#instrument.address                         # this is the slave address number
#instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
#instrument.clear_buffers_before_each_transaction = True

# 0-1650 er lig -40 til 125C
tempraw = instrument.read_register(0)
temp = tempraw/1650. * (125--40) + -40

hum = instrument.read_register(1,1)

print ('%4.1fC %4.1f%%' % (temp,hum))


## Change temperature setpoint (SP) ##
# NEW_TEMPERATURE = 95
# instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage
