import minimalmodbus as mmb
import argparse

parser=argparse.ArgumentParser(prog='prepper')
parser.add_argument('slavetype')
parser.add_argument('currentaddr')
#parser.add_argument('currentaddr')

#(rtu,9600,even,

#https://en.wikipedia.org/wiki/8-N-1

#9600b 8e1




instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1)  # port name, slave address (in decimal)
