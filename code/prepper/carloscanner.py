import minimalmodbus as mmb
import argparse
import serial

def scan(baud):
    print('scanning for baud',baud)
    instrument.serial.baudrate = baud # default 19200         # Baud
    instrument.serial.bytesize = 8
    instrument.serial.parity   = serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout  = 1

    for addr in range(0,10):
        try:
            #ctrl_id_code = instrument.read_register(0x000B)
            ctrl_id_code = instrument.read_register(0x5000)
            print(addr, ctrl_id_code)
        except mmb.NoResponseError:
            print('fail')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(prog='carloscanner.py')
    parser.add_argument('baud',default=None)

    instrument = mmb.Instrument('/dev/ttyUSB0', 1)  # port name, slave address
    args = parser.parse_args()

    if args.baud:
        bauds = args.baud.split(',')
    else:
        bauds = [9600]

    for baud in bauds:
        scan(baud)
