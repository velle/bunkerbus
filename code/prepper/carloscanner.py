#!/usr/bin/env python

import minimalmodbus as mmb
import argparse
import serial

#BAUD_VALS = [9600]
#BYTESIZE_VALS = [7,8]
#PARITY_VALS = [ serial.PARITY_EVEN, serial.PARITY_ODD,
                #serial.PARITY_MARK, serial.PARITY_NONE,  serial.PARITY_SPACE,]
#STOPBITS_VALS = [serial.STOPBITS_ONE, serial.STOPBITS_TWO, serial.STOPBITS_ONE_POINT_FIVE]
#TIMEOUT = 2

BAUD_VALS = [9600]
BYTESIZE_VALS = [8]
PARITY_VALS = [ serial.PARITY_NONE ]
STOPBITS_VALS = [serial.STOPBITS_ONE]
TIMEOUT = 2


def scan(baud, bytesize, parity, stopbits, timeout=TIMEOUT):
    instrument.serial.baudrate = baud # default 19200         # Baud
    instrument.serial.bytesize = bytesize
    instrument.serial.parity   = parity
    instrument.serial.stopbits = stopbits
    instrument.serial.timeout  = timeout

    for addr in range(1,2):
        print ("baudrate:%s bytesize:%s parity:%s stopbits:%s timeout:%ss addr:%d" % (baud, bytesize, parity, stopbits, timeout, addr))
        try:
            #ctrl_id_code = instrument.read_register(0x000B)
            #ctrl_id_code = instrument.read_register(0x5000)
            ctrl_id_code = instrument.read_register(0x0302) # Carlo Gavazzi, firmware version code
#            ctrl_id_code = instrument.read_register(0x0302) # Carlo Gavazzi, controls identification code
            print('SUCCESS: ctrl_id_code: ', ctrl_id_code)
        except mmb.NoResponseError:
            pass
            #print(addr, 'fail')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(prog='carloscanner.py')

    instrument = mmb.Instrument('/dev/ttyUSB0', 1)  # port name, slave address


    for baud in BAUD_VALS:
        for bytesize in BYTESIZE_VALS:
            for parity in PARITY_VALS:
                for stopbits in STOPBITS_VALS:
                    scan(baud,bytesize,parity,stopbits)

    #scan(baud=9600,bytesize=8,parity=serial.PARITY_NONE,stopbits=1)
    #scan(baud=9600,bytesize=8,parity=serial.PARITY_NONE,stopbits=1)
