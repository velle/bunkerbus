import minimalmodbus as mmb
import argparse
import serial

parser=argparse.ArgumentParser(prog='R4DCB08_prepper.py')
parser.add_argument('newaddr')

instrument = mmb.Instrument('/dev/ttyUSB0', 1)  # port name, slave address

# addr, 0x06 write single register, register addr, setting content, crc16

#instrument.serial.port                     # this is the serial port name
instrument.serial.baudrate = 9600 # default 19200         # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1

instrument.write_register(0xFE,3)
