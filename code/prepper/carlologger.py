#!/usr/bin/env python

import minimalmodbus as mmb
import argparse
import serial
import time

REGISTERS = [
    ('V_L1',0),
    ('V_L2',2),
    ('V_L3',4),
    ('A_L1',12),
    ('A_L2',14),
    ('A_L3',16),
    ('kWh_L1',64),
    ('kWh_L2',66),
    ('kWh_L3',68),
]

if __name__ == '__main__':
    instrument = mmb.Instrument('/dev/ttyUSB0', 1)  # port name, slave address
    instrument.serial.baudrate = 9600 # default 19200         # Baud
    instrument.serial.bytesize = 8
    instrument.serial.parity   = serial.PARITY_NONE
    instrument.serial.stopbits = serial.STOPBITS_ONE
    instrument.serial.timeout  = 1

    measurements=[]
    for name,regaddr in REGISTERS:
        measurements.append(
            instrument.read_register(regaddr)
        )
        time.sleep(0.5)

    s = ';'.join([str(m) for m in measurements])
    print(s)